'''
1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.


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
