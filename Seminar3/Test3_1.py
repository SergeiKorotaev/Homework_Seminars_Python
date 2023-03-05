num = int(input("Введите число N: "))
count = 0
array = []
for i in range(num):
    array.append(int(input("Ведите числа: ")))
find_num = int(input("Введите искомое число: "))
for j in (array):
    if find_num == j:
        count += 1
print("В массиве", array, "число", find_num, "встречается", count, "раз.")