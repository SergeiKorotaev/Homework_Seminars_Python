num = int(input("Введите колличество элементов списка: "))
array = []
for i in range(num):
    array.append(int(input("Введите элементы списка: ")))
min_number = int(input("Введите минимальное число диапазона: "))
max_number = int(input("Введите максимальное число диапазона: "))
for j in range(len(array)):
    if min_number <= array[j] <= max_number:
        print(j)
