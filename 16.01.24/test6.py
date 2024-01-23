import random
# Завдання 6

# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.

list1 = [random.randint(1, 9) for i in range(10)]
print(list1)


def degree(num):
    num_degree_list = []
    for i in list1:
        num_degree = i ** num
        num_degree_list.append(num_degree)
    return num_degree_list


num_d = int(
    input("Введите степень, в которую желаете возвести числа из списка: "))
result = degree(num_d)
print(result)
