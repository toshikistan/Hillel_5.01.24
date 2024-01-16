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
# - вивести суму чисел головної діагоналі матриці
main_diagonal = []
for i in range(MATRIX_LENS):
    main_diagonal.append(matrix[i][i])
sum_main_diagonal = sum(main_diagonal)
print(sum_main_diagonal)
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
sub_diagonal = []
for i in range(MATRIX_LENS):
    sub_diagonal.append(matrix[i][MATRIX_LENS - 1 - i])

max_sub = max(sub_diagonal)
min_sub = min(sub_diagonal)
print(f"{max_sub} - максимальное число, а {min_sub} - минимальное в побочной диагонали.")
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
collumn = int(input("Введите номер столбика, числа которого вы хотите вывести: "))
collumn_int = []
for i in range(MATRIX_LENS):
    collumn_int.append(matrix[i][collumn - 1])
print(collumn_int)
row = int(input("Введите номер ряда, числа которого вы хотите вывести: "))
row_int = []
for i in range(MATRIX_LENS):
    row_int.append(matrix[row - 1][i])
print(row_int)
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю (аналогічно зробити з рядком)
collumn1 = int(input("Введите номер первого столбика: "))
collumn2 = int(input("Введите номер второго столбика: "))

for collumn in matrix:
    matrix[collumn1], matrix[collumn2] = matrix[collumn2], matrix[collumn1]
print(matrix)