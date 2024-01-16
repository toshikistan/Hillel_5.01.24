import random
import math

LIST_LEN = 20
numbers = []

for i in range(LIST_LEN):
    numbers.append(random.randint(-50, 50))

print(numbers)

# У списку цілих, заповненому випадковими числами обчислити:

# ■ Суму негативних чисел;
neg_num = []
for i in numbers:
    if i < 0:
        neg_num.append(i)

neg_num_summ = sum(neg_num)
print(neg_num_summ)
print("____" * 10)
# ■ Суму парних чисел;
even_num = []
for i in numbers:
    if i % 2 == 0:
        even_num.append(i)

even_num_summ = sum(even_num)
print(even_num_summ)
print("____" * 10)
# ■ Суму непарних чисел;
odd_num = []
for i in numbers:
    if i % 2 == 1:
        odd_num.append(i)

odd_num_summ = sum(odd_num)
print(odd_num_summ)
print("____" * 10)
# ■ Добуток елементів з кратними індексами 3; ########## Написал 2 способа
m3_mult = numbers[2::3]

# Способ 1
result = 1
for i in m3_mult:
    result *= i
print(result)

# Способ 2
m3_num_mult = math.prod(m3_mult)
print(m3_num_mult)
print("____" * 10)
# ■ Добуток елементів між мінімальним та максимальним елементом;
max_value = max(numbers)
min_value = min(numbers)
max_value_index = numbers.index(max_value)
min_value_index = numbers.index(min_value)
maxmin_list = numbers[min_value_index + 1:max_value_index]
if maxmin_list == []:
    maxmin_list = numbers[max_value_index + 1:min_value_index]
    mult = math.prod(maxmin_list)
    print(mult)
else:
    mult = math.prod(maxmin_list)
    print(mult)
print("____" * 10)
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
pos_num = []
for i in numbers:
    if i > 0:
        pos_num_index = numbers.index(i)
        pos_num += numbers[pos_num_index + 1:LIST_LEN]
        break
pos_num.reverse()

pos_num2 = []

for i in pos_num:
    if i > 0:
        pos_num2_index = pos_num.index(i)
        pos_num2 += pos_num[pos_num2_index + 1:LIST_LEN]
        break
pos_num2.reverse()
result_pos = sum(pos_num2)
print(result_pos)