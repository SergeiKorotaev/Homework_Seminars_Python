print("Введите длинну шоколадки: ")
Size1 = int(input())
print("Введите ширину шоколадки: ")
Size2 = int(input())
print("Сколько долек хотите отломить? ")
Quantity = int(input())
if Quantity  < Size2 * Size1 and (Quantity  % Size2 == 0 or Quantity  % Size1 == 0):
    print('YES')
else:
    print('NO')