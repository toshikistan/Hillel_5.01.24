while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        if num1 == num2:
            print("Эти числа одинаковые!")
        elif num1 > num2:
            print(f"{num1} больше, чем {num2}")
            print(num2, num1)
        elif num2 > num1:
            print(f"{num2} больше, чем {num1}")
            print(num1, num2)
        else:
            print("Ошибка! Введите число.")
        break
    except ValueError as error:
        print(f"Ошибка {error}! Введите целое число в поле для ввода.")
