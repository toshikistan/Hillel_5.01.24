##################### Фигуру Е не получилось реализовать, не понял, как.
LENGTH = 5
SYMBOL = '* '

choice = input(
    "Какую фигуру хотите нарисовать? Выберите букву: а, б, в, г, д, е, ж, з, и, к: \n").lower()
match choice:
    # а
    case "а":
        for i in range(LENGTH, 0, -1):
            print((SYMBOL * i).rjust(LENGTH * 2))
        print("а")
    # б
    case "б":
        for i in range(0, LENGTH + 1):
            print(SYMBOL * i)
        print("б")
    # в
    case "в":
        for i in range(LENGTH, 0, -2):
            print((SYMBOL * i).center(LENGTH * 2))
        print("в")
    # г
    case "г":
        for i in range(1, LENGTH + 1, 2):
            print((SYMBOL * i).center(LENGTH * 2))
        print("г")
    # д
    case "д":
        for i in range(LENGTH, 1, -2):
            print((SYMBOL * i).center(LENGTH * 2))
        for i in range(1, LENGTH + 1, 2):
            print((SYMBOL * i).center(LENGTH * 2))
        print("д")
    # ж
    case "ж":
        for i in range(1, LENGTH - 2, 1):
            print(SYMBOL * i)
        for i in range(LENGTH - 2, 0, -1):
            print(SYMBOL * i)
        print("ж")
    # з
    case "з":
        for i in range(1, LENGTH - 2, 1):
            print((SYMBOL * i).rjust(LENGTH * 2))
        for i in range(LENGTH - 2, 0, -1):
            print((SYMBOL * i).rjust(LENGTH * 2))
        print("з")
    # и
    case "и":
        for i in range(LENGTH, 0, -1):
            print(SYMBOL * i)
        print("и")
    # к
    case "к":
        for i in range(0, LENGTH + 1):
            print((SYMBOL * i).rjust(LENGTH * 2))
        print("к")
