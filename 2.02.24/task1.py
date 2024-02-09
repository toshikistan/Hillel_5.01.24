'''
1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.

2. Даний текстовий файл. Підрахувати кількість слів у ньому.

3. Створіть програму, яка перевіряє текст на неприпустимі слова.

Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.

За підсумками роботи програми необхідно показати статистику дій.

Наприклад, якщо й у нас є такий текст:

To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep

Неприпустиме слово: die.

Результат:

To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To ***: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To ***, to sleep.

Статистика: 2 заміни слова die.

Нотатка: 

Текст для всіх завдань можна написати самостійно або взяти з Інтернету.

Логіка має працювати з будь-яким текстом.
'''
import os

with open("words_list.txt", "w", encoding="utf-8") as my_file:
    my_file.write(
        "абажур\nаббревиатура\nаберрация\nабзац\nабилитация\nабордаж\nабрис\nабсурд\nабьюз\nАвгуст\nавиатор\nАвстралия\nавтограф\nагент\nагнозия\nадепт\nадмин\nакадемия\n")

with open("words_list.txt", "r", encoding="utf-8") as my_file:
    result = my_file.read()
    print(result)

for word in result.split():
    if len(word) >= 7:
        with open("word_list_len7_or_more.txt", "a", encoding="utf-8") as new_file:
            new_result = new_file.write(word + '\n')
            print(word)
