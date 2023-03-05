n = int( input("Введите колличество кустов: ") )
bushes = [ int(x) for x in input("Введите колличество ягод на кустах через пробел: ").split() ]
n = len(bushes)
bushes = bushes + bushes[:2]
max_barries = 0
for i in range(n):
    max_barries = max( max_barries, bushes[i] + bushes[i+1] + bushes[i+2] )
print(max_barries)