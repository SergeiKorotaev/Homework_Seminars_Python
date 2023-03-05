print("Введите колличество монет: ")
number_of_coins = int(input())
count0 = 0
count1 = 0
print("Введите стороны монет если орёл = 0, а решка = 1")
for i in range(number_of_coins):
    coins = int(input())
    if coins == 0:
        count0 += 1
    else:
        count1 += 1
if count1 > count0:
    print("Необходимо перевернуть", count0, "монет")
else:
    print("Необходимо перевернуть", count1, "монет")
