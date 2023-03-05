num = int(input("Введите число N: "))
array = []
for i in range(num):
    array.append(int(input("Ведите числа: ")))
find_num = int(input("Введите искомое число: "))

b=[abs(array[i]-find_num) for i in range(len(array))]
print(array[b.index(min(b))])