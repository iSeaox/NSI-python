import matplotlib.pyplot as plt
import math


global compteur1
compteur1 = 0

global compteur2
compteur2 = 0

def puissance1(a, n):
    global compteur1

    compteur1 += 1
    if(n== 0):
        return 1
    compteur1 += 3
    return a * puissance1(a, n-1)

def puissance2(a, n):
    global compteur2

    compteur2 += 1
    if(n == 0):
        return 1
    compteur2 += 2
    if(n % 2 != 0):
        compteur2 += 5
        return a * puissance2(a*a, (n-1)//2)
    compteur2 += 3
    return puissance2(a*a, n // 2)

print(puissance1(10, 10), compteur1)
compteur1 = 0
print(puissance1(10, 20), compteur1)
compteur1 = 0
print(puissance1(10, 30), compteur1)
compteur1 = 0
print(puissance1(10, 40), compteur1)
print("_______________________________________________")

x = []
y = []
y_base = []
percent = 0
it = 400000

for i in range(10, it, 10):

    if(i % (it / 100) == 0):
        percent += 1
        print(percent, " / 100")

    puissance2(10, i)
    x.append(i)
    y.append(compteur2)
    compteur2 = 0
print("100 / 100")

for i in x:
    y_base.append(7.25 * math.log(i, 2));


plt.plot(x, y, label="nb opération en fonction de x")
plt.plot(x, y_base, label="log2(x)")
plt.legend()
plt.show()


