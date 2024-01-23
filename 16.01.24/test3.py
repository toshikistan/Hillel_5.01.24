import random
# Завдання 3

# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

# def count_simple(simple_list):
#     count = 0
#     for i in simple_list:
#         for i in nums_list:
#             if i % num != 0:
#                 count += 1
#     return count

# num = input("Через пробел введите числа, которые хотите перемножить: ").lstrip().rstrip()
# nums_list = num.split(' ')

# nums_list = [int(num) for num in nums_list]

# simple_res = count_simple(nums_list)
# print(simple_res)


#  def simple_num(num):
#         if num <= 2:
#             return False
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True


def count_simple(simple_list):
    def simple_num(num):
        if num <= 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True

    count = 0
    for num in simple_list:
        if simple_num(num):
            count += 1
    return count


nums_list = [random.randint(1, 20) for i in range(10)]
print(nums_list)

simple_res = count_simple(nums_list)
print(simple_res)
