m = [1,2,3,4,5,6,7,8,9,0,10,12,2,3,12]
m1=[[1],[2],[3]]

print(m)
for i in range(len(m)):
    print("Index",i,"number -",m[i])
    m[i] *=10

for i in range(len(m)):
    print("Index",i,"number -",m[i])

for i in m:
    print(i, end = " ")
print() 
print(max(m))
print(min(m))
print(sum(m))
m.sort()
print(m)
    