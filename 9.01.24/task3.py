text = input("Введите какое-то сообщение: \n")
find = input("Введите слово, которое хотите заменить: \n")
change = input("Введите новое слово, которое должно быть в тексте: \n")

text = text.replace(find, change)
print(text)