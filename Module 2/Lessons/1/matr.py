import random
matr = []
n=5
for i in range(n):
    cash= []
    for j in range(n):
        cash.append(random.randint(-10,10))
        
    matr.append(cash)
    # print("Cash", cash, "Matr", matr)
print(matr)
print(matr[0][0])
for i in matr:
    for j in i:
        print(j, end = " ")
    print()