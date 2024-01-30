def find_sum(a, b):
    if a > b:
        return 0
    else:
        return a + find_sum(a + 1, b)


print(find_sum(1, 11))
