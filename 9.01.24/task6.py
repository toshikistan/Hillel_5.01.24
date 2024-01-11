LENGTH = 5
SYMBOL = '* '

# а
for i in range(LENGTH, 0, -1):
    print((SYMBOL * i).rjust(LENGTH * 2))
print("а")
# б
for i in range(0, LENGTH +1):
    print(SYMBOL * i)
print("б")
# в
for i in range(LENGTH, 0, -2):
    print((SYMBOL * i).center(LENGTH * 2))
print("в")
# г
for i in range(1, LENGTH +1, 2):
    print((SYMBOL * i).center(LENGTH * 2))
print("г")
# д
for i in range(LENGTH, 1, -2):
    print((SYMBOL * i).center(LENGTH * 2))
for i in range(1, LENGTH +1, 2):
    print((SYMBOL * i).center(LENGTH * 2))
print("д")
# ж
for i in range(1, LENGTH - 2, 1):
    print(SYMBOL * i)
for i in range(LENGTH - 2, 0, -1):
    print(SYMBOL * i)
print("ж")
# з
for i in range(1, LENGTH - 2, 1):
    print((SYMBOL * i).rjust(LENGTH *2))
for i in range(LENGTH - 2, 0, -1):
    print((SYMBOL * i).rjust(LENGTH *2))
print("з")
# и
for i in range(LENGTH, 0, -1):
    print(SYMBOL * i)
print("и")
# к
for i in range(0, LENGTH +1):
    print((SYMBOL * i).rjust(LENGTH * 2))
print("к")