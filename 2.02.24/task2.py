import os

with open("words_list_count.txt", "w", encoding="utf-8") as my_file:
    result = my_file.write(
        "абажур\nаббревиатура\nаберрация\nабзац\nабилитация\nабордаж\nабрис\nабсурд\nабьюз\nАвгуст\nавиатор\nАвстралия\nавтограф\nагент\nагнозия\nадепт\nадмин\nакадемия\n")

with open("words_list_count.txt", "r", encoding="utf-8") as my_file:
    read_file = my_file.read()
    word_count = len(read_file.split())
    print(f"Количество слов в файле равно {word_count}")
