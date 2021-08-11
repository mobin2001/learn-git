import math
tedad_adad = int(input())
javab = dict()
for x in range (0,tedad_adad):
    adad = float(input())
    adad = math.sqrt(adad)
    javab[x] = adad
for y in range (0,tedad_adad):
    print(javab[y])