import random
n =9
mass = []
for i in range(n):
    cash = []
    for j in range(n):
        cash.append(random.randint(0,20))
    mass.append(cash)
    
for i in mass:
    print(i)
    
# cash = []
max = 0
for i in range(n):
    for j in range(n):
        if i>j and j!=0 and i!=n-1: #and (i<=n-1-j or i>=n-1-j):
            mass[i][j] = -1
            # cash.append(mass[i][j])
            if mass[i][j] > max:
                max = mass[i][j]
print("Max - ", max)
for i in mass:
    print(i)
input()
  