while True:
    try:

        day = int(input("Введите номер дня недели: "))
        if 1 <= day <= 7:
            match day:
                case 1:
                    print("Понедельник")
                case 2:
                    print("Вторник")
                case 3:
                    print("Среда")
                case 4:
                    print("Четверг")
                case 5:
                    print("Пятница")
                case 6:
                    print("Суббота")
                case 7:
                    print("Воскресенье")
            break
        else:
            print("Ошибка! Введите число от 1 до 7.")

    except ValueError as error:
        print(f"Ошибка {error}! Введите число в поле для ввода.")
    except Exception as error:
        print(f"Ошибка {error}! Введите число в поле для ввода.")
