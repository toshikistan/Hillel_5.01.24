text = input("Введите какое-то сообщение с буквами и цифрами: \n")

count_letter = 0
count_digit = 0
for letter in text:
    if letter.isalpha():
        count_letter += 1
for digit in text:
    if digit.isdigit():
        count_digit += 1

print(f"Количество букв в строке: {count_letter}")
print(f"Количество цифр в строке: {count_digit}")