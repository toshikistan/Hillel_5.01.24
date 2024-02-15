class Person:
    __name = "no name"
    __health = "",
    __damage = 1
    __defence = 0
    __weapon = "no weapon"
    __armor = "no armor"

    def __init__(self, name, health, damage, defence, weapon="Knuckles", armor=None):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__defence = defence
        self.__weapon = weapon if weapon else "no weapon"
        self.__armor = armor if armor else "no armor"

    def take_damage(self, damage):
        self.health -= damage - self.defence
        print(f"{self.name} loses {
              damage} health points! His health is {self.health} now!")

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


class Hero(Person):

    def attack(self, enemy):
        print(f"{self.name} attackes with {self.weapon}")
        enemy.take_damage(self.damage)


class Enemy(Person):

    def attack(self, hero):
        print(f"{self.name} attackes with {self.weapon}")
        hero.take_damage(self.damage)


''''''


class Weapon:
    pass


class Armor:
    pass


''''''


class Potion:
    pass


class HealPotion(Potion):
    pass


class BuffPotion(Potion):
    pass


hero = Hero("Arthur", 100, 20, 10)
enemy = Enemy("Orc", 80, 15, 5)

while hero.health > 0 and enemy.health > 0:
    hero.attack(enemy)
    enemy.attack(hero)

if hero.health > 0:
    print(f"{hero.name} победил!")
else:
    print(f"{enemy.name} победил!")
