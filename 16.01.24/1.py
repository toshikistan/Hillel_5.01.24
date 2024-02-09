num3 = int(input("Введите число из 3 символов: "))

n1 = num3 // 100
n2 = num3 // 10 % 10
n3 = num3 % 10

num3_sum = n1 + n2 + n3
num3_mult = n1 * n2 * n3
print(f"Сумма всех цифр равна {num3_sum}")
print(f"Произведение всех цифр равно {num3_mult}")

a = int(input("Введите длину одной диагонали: "))
b = int(input("Введите длину второй диагонали: "))
square = a * b / 2
print(f"Площадь ромба равна {square}")

# def mult_4(a):
#     result = 1
#     for num in str(a):
#         result *= int(num)
#     return result


# num = int(input("Введите число: "))

# result = mult_4(num)
# print(result)

num4 = int(input("Введите число из 4 знаков: "))

n1 = num4 // 1000
n2 = num4 // 100 % 10
n3 = num4 // 10 % 10
n4 = num4 % 10

num4_sum = n1 + n2 + n3 + n4
num4_mult = n1 * n2 * n3 * n4

print(f"Сумма всех цифр равна {num4_sum}")
print(f"Произведение всех цифр равно {num4_mult}")
