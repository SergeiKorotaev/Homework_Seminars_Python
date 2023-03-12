def rifma(chant):
    st = chant.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(st[0])
    if all([f(i) == tmp for i in st]):
        return 'Пам парам'
    return 'Парам пам-пам'
 
print(rifma(input("Стих: ")))