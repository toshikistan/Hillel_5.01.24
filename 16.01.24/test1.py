# Завдання 1

# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

def list_mult(mult_list):
    result = 1
    for i in mult_list:
        result *= i
    return result

nums = input("Через пробел введите числа, которые хотите перемножить: ")
nums_list = nums.split(' ')

nums_list = [float(num) for num in nums_list]

mult_res = list_mult(nums_list)
mult_res = round(mult_res, 2)
print(mult_res)