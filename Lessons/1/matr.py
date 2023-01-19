import random
m = []
n=6
for i in range(n):
    cash = []
    for j in range(n):
        cash.append(random.randint(0,90))
    m.append(cash)
print(m)
    
for i in m:
    for j in i:
        print(j, end=' ')
    print(sum(m[i]))