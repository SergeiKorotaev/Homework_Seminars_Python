s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
answer = "Ответ отсутствует"

Dis = s ** 2 - 4 * p

if Dis >= 0:
    x = (s + Dis ** 0.5) // 2
    y = (s - Dis ** 0.5) // 2
    if x * y == p:
        answer = f"Загаданные числа: {x}, {y}"
print(answer)