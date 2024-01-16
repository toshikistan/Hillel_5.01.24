import random

# Додаткові завдання по матрицях (надіслати як завжди мені в лс після виконання основного дз):

# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
matrix = []
MATRIX_LENS = 10

for i in range(MATRIX_LENS):
    matrix.append([])
    for j in range(MATRIX_LENS):
        matrix[i].append(random.randint(10, 99))

# вивести на екран
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end =" ")
    print()
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)
    
    
# collumn1 = int(input("Введите номер столбика, числа которого вы хотите вывести: "))
# collumn2 = int(input("Введите номер столбика, числа которого вы хотите вывести: "))
# collumn_int1 = []
# collumn_int2 = []
# for i in range(MATRIX_LENS):
#     collumn_int1.append(matrix[i][collumn1 - 1])
# for i in range(MATRIX_LENS):
#     collumn_int2.append(matrix[i][collumn2 - 1])

# collumn_temp = collumn_int1
# collumn_int1 = collumn_int2
# collumn_int2 = collumn_temp
# print(collumn_int1)
# print(collumn_int2)
# column1 = int(input("Введите номер первого столбца: "))
# column2 = int(input("Введите номер второго столбца: "))

# for i in range(MATRIX_LENS):
#     temp = matrix[i][column1 - 1]
#     matrix[i][column1 - 1] = matrix[i][column2 - 1]
#     matrix[i][column2 - 1] = temp

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end =" ")
#     print()


row1 = int(input("Введите номер первого столбца: "))
row2 = int(input("Введите номер второго столбца: "))

for i in range(MATRIX_LENS):
    temp = matrix[row1 - 1][i]
    matrix[row1 - 1][i] = matrix[row2 - 1][i]
    matrix[row2 - 1][i] = temp

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end =" ")
    print()