def exponentiation(a, b):
    if b == 0:
        return 1
    return a * exponentiation(a, b - 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(exponentiation(a, b))