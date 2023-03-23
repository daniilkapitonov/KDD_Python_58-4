import random
matr = []
n=5
for i in range(n):
    cash= []
    for j in range(n):
        cash.append(random.randint(-10,10))
        
    matr.append(cash)
for i in matr:
    print(i, sum(i))