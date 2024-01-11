text = input("Введите какое-то сообщение: \n")
symbol_text = input("Введите символ, который желаете найти: ")

count_symbol = 0
for symbol in text:
    if symbol == symbol_text:
        count_symbol += 1

print(f"Количество букв в строке: {count_symbol}")