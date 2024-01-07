while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        operation = input(
            "Какое действие вы желаете совершить? \n( +, -, *, / ): ")
        match operation:
            case "+":
                result = (num1 + num2)
                print(result)
            case "-":
                result = (num1 - num2)
                print(result)
            case "*":
                result = (num1 * num2)
                print(result)
            case "/":
                result = round(num1 / num2, 2)
                print(result)
            case _:
                print("Ошибка, попробуйте ещё раз.")
        restart = input(
            "Если хотите посчитать ещё раз, введите \"Да\", в противном случае нажмите Enter: ").lower()
        if restart != "да":
            break

    except ValueError as error:
        print(f"Ошибка {error}! Введите число в поле для ввода.")
    except ZeroDivisionError as error:
        print(f"Ошибка {error}! На 0 делить нельзя! Попробуйте ещё раз.")
    except Exception as error:
        print(f"Ошибка {error}! Введите число в поле для ввода.")
