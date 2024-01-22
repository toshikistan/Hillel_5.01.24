# Завдання 2

# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

def list_min(min_list):
    for i in min_list:
        min_num = min(min_list)
    return min_num

nums = input("Через пробел введите числа, минимальное из которых хотите узнать: ").lstrip().rstrip()
nums_list = nums.split(' ')

nums_list = [int(num) for num in nums_list]
mini_num = list_min(nums_list)
print(mini_num)