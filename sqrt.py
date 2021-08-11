import math
tedad_adad = int(input())
javab = dict()
for x in range (0,tedad_adad):
    adad = float(input())
    adad = math.sqrt(adad)
    #jazr adad ra ta 8 ragam ashar zakhire mikonad
    javab[x] = "%5.8f"%(adad)

for y in range (0,tedad_adad):
    print(javab[y][:-4])
#jazr ra ta 4 ragam ashar bdon round kardan chap mikonad
