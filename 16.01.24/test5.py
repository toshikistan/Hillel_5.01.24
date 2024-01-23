import random
# Завдання 5

# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

list1 = [random.randint(1, 9) for i in range(10)]
list2 = [random.randint(1, 9) for i in range(10)]
print(list1)
print(list2)


def show_common(list1, list2):
    common = set(list1) & set(list2)
    return (list(common))


def merge_list(list1, list2):
    merged_list = list1 + list2
    return (merged_list)


merge = merge_list(list1, list2)
same_numbers = show_common(list1, list2)
print(same_numbers)
print(merge)
