def find_degree(n, degree):
    if degree <= 1:
        return n

    return n * find_degree(n, degree - 1)


num = int(input("Введите число: "))
deg = int(input("Введите степень: "))
res = find_degree(num, deg)
print(res)
