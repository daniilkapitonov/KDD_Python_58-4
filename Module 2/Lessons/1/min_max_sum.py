import random
m = []
for i in range(10):
    m.append(random.randint(0,100))
print(m)
sum_m = 0
for i in m:
    sum_m+=i
print("Sum",sum_m, sum(m))

max_m = 0
for i in m:
    if i>max_m:
        max_m = i
print("Max", max_m, max(m))

min_m = 100
for i in m:
    if i<min_m:
        min_m = i
print("Min", min_m, min(m))

print(type(m[0]))