'''3. Створіть програму, яка перевіряє текст на неприпустимі слова.

Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.

За підсумками роботи програми необхідно показати статистику дій.

Наприклад, якщо й у нас є такий текст:

To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep

Неприпустиме слово: die.

Результат:

To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To ***: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To ***, to sleep.

Статистика: 2 заміни слова die.'''

text = "It was a special pleasure to see things eaten, to see things blackened and changed. With the brass nozzle in his fists, with this great python spitting its venomous kerosene upon the world, the blood pounded in his head, and his hands were the hands of some amazing conductor playing all the symphonies of blazing and burning to bring down the tatters and charcoal ruins of history. With his symbolic helmet numbered 451 on his stolid head, and his eyes all orange flame with the thought of what came next, he flicked the igniter and the house jumped up in a gorging fire that burned the evening sky red and yellow and black. He strode in a swarm of fireflies. He wanted above all, like the old joke, to shove a marshmallow on a stick in the furnace, while the flapping pigeon-winged books died on the porch and lawn of the house. While the books went up in sparkling whirls and blew away on a wind turned dark with burning."
censored_word = "book"

with open("my_text.txt", "w") as text_file:
    text_file.write(text)

with open("my_text.txt", "r") as my_file:
    text_in_file = my_file.read()

count_words = text_in_file.count(censored_word)
new_text = text_in_file.replace(censored_word, "*" * len(censored_word))
new_text_count = new_text.count("*" * len(censored_word))

print(new_text)
print(new_text_count)

with open("censored_text.txt", "w") as censored_file:
    censored_file.write(new_text)
