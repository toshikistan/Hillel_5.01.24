# Завдання 4

# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.


# nums_list = [2, 4, 2, 5, 1, 1, 5, 7, 3, 2, 4, 1]
# print(nums_list)
# del_choice = int(input("Выберите, какое число из списка хотите удалить?: "))
# first_len = len(nums_list)


# def count_deleted():
#     for i in nums_list:
#         if del_choice in nums_list:
#             nums_list.remove(del_choice)
#     return first_len - len(nums_list)


# count = count_deleted()
# print(
#     f"Количество удаленных элементов равно {count}. \nТеперь список выглядит таким образом: {nums_list}")


nums_list = [2, 4, 2, 5, 1, 1, 5, 7, 3, 2, 4, 1]
print(nums_list)
del_choice = int(input("Выберите, какое число из списка хотите удалить?: "))


def count_deleted():
    del_choice_list = []
    new_list = []
    for i in nums_list:
        if i == del_choice:
            del_choice_list.append(i)
        elif i != del_choice:
            new_list.append(i)
    return len(del_choice_list), new_list


count, new_list = count_deleted()
print(
    f"Количество удаленных элементов равно {count}. \nТеперь список выглядит таким образом: {new_list}")
