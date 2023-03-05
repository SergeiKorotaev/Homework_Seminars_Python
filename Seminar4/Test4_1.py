first_numbers = int(input("Введите колличество первого набора чисел: "))
second_numbers = int(input("Введите колличество второго набора чисел: "))
array1 = []
array2 = []
for i in range(first_numbers):
    array1.append(int(input("Введите числа первого набора: ")))
for j in range(second_numbers):
    array2.append(int(input("Введите числа второго набора: ")))
array1.extend(array2)
print(*sorted(set(array1)))