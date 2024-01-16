import random
# Завдання 2

# Є список цілих, заповнений випадковими числами.

LIST_LEN = 20
numbers = []

for i in range(LIST_LEN):
    numbers.append(random.randint(-99, 99))

print(numbers)

# На підставі даних цього масиву потрібно:

# ■ Створити список цілих, що містить лише парні числа з першого списку;
even_num = []
for i in numbers:
    if i % 2 == 0:
        even_num.append(i)
print(even_num)
print("___" * 10)
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
odd_num = []
for i in numbers:
    if i % 2 == 1:
        odd_num.append(i)
print(odd_num)
print("___" * 10)
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
neg_num = []
for i in numbers:
    if i < 0:
        neg_num.append(i)
print(neg_num)
print("___" * 10)
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
pos_num = []
for i in numbers:
    if i > 0:
        pos_num.append(i)
print(pos_num)