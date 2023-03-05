litters_points = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2, "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5, "JXШЭЮ": 8, "QZФЩЪ": 10}
print("Введите слово: ")
word = input()
print("Колличество набранных вами очков:", sum([i[1] for i in litters_points.items() for j in word if j.upper() in i[0]]))