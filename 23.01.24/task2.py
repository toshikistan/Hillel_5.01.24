def draw_stars(num_stars):
    if num_stars > 0:
        return print("*", end=" "), draw_stars(num_stars - 1)
    else:
        print(" ")


num = int(input("Введите число: "))
res = draw_stars(num)
