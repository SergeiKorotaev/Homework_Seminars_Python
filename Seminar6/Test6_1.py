first_num = int(input("Введите первый элемент: "))
diff = int(input("Введите разность: "))
elements = int(input("Введите колличество элементов: "))
for i in range(1, elements + 1):
    result = first_num + (i - 1) * diff
    print(result)    