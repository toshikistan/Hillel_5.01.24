import time


class Person:
    __name = "no name"
    __health = "",
    __damage = 1
    __defence = 0
    __weapon = "no weapon"
    __armor = "no armor"

    def __init__(self, name, health, damage, defence, weapon=None, armor=None):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__defence = defence
        self.__weapon = weapon if weapon else "Knuckles"
        self.__armor = armor if armor else "no armor"

    def take_damage(self, damage):
        total_damage = damage - self.defence - Armor.armors.get(self.armor, 0)
        self.health -= total_damage
        print(f"{self.name} loses {
              total_damage} health points! His health is {self.health} now!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 5:
            self.__name = name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if health <= 0:
            print(f"{self.name} is gonna die!")
        self.__health = health

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.damage = damage

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, defence):
        self.__defence = defence

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, weapon):
        self.__weapon = weapon

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, armor):
        self.__armor = armor

    def show_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Damage: {self.damage}, Defence: {
              self.armor}, Weapon: {self.weapon}, Armor: {self.armor}")


class Hero(Person):
    def __init__(self, name, health, damage, defence, weapon=None, armor=None):
        super().__init__(name, health, damage, defence, weapon, armor)
        self.__small_potion_used = False
        self.__big_potion_used = False

    def attack(self, enemy):
        print(f"{self.name} attackes with {self.weapon}")
        total_damage = self.damage + Weapon.weapons.get(self.weapon, 0)
        enemy.take_damage(total_damage)

        if self.health < 60 and not self.__small_potion_used:
            self.use_potion("Small potion")
            self.__small_potion_used = True

        if self.health <= 20 and not self.__big_potion_used:
            self.use_potion("Big potion")
            self.__big_potion_used = True

    def use_potion(self, potion_name):
        if potion_name in Potion.potions:
            heal_amount = Potion.potions[potion_name]
            self.health += heal_amount
            print(f"{self.name} used {
                  potion_name} and got +{heal_amount} health! His health now is {self.health}")


class Enemy(Person):
    def attack(self, hero):
        print(f"{self.name} attackes with {self.weapon}")
        total_damage = self.damage + Weapon.weapons.get(self.weapon, 0)
        hero.take_damage(total_damage)


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    weapons = {
        "Sword": 15,
        "Axe": 20,
        "Bow": 10,
    }


class Armor:
    def __init__(self, name, defence):
        self.name = name
        self.defene = defence

    armors = {
        "Shield": 5,
        "Helmet": 10,
        "Corselet": 15,
    }


class Potion:
    def __init__(self, name, heal):
        self.name = name
        self.heal = heal

    potions = {
        "Small potion": 20,
        "Big potion": 60,
    }


hero = Hero("Arthur", 100, 22, 11, "", "Corselet")
enemy = Enemy("Orc", 80, 20, 5, "Axe", "Helmet")

while hero.health > 0 and enemy.health > 0:
    time.sleep(1)
    hero.attack(enemy)
    enemy.attack(hero)

if hero.health > 0:
    print(f"{hero.name} wins!")
elif enemy.health > 0:
    print(f"{enemy.name} wins!")
else:
    print(f"{hero.name} and {enemy.name} died.")


hero.show_info()
enemy.show_info()
print(hero.name)
print(enemy.weapon)
print(hero.health)
print(enemy.armor)
print(hero.defence)
