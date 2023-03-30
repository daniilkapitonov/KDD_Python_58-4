def matrix(*a):
    l = len(a)
    if l==0:
        return [0]
    elif l==1:
        return [[0]*a[0]]*a[0]
    elif l==2:
        return [[0]*a[0]]*a[1]
    elif l==3:
        return [[a[2]]*a[0]]*a[1]

print(matrix())
print(matrix(3))
print(matrix(3,4))
print(matrix(5,6,7))

# [[a[2]]*a[0]]*a[1]
# mass = []
# for i in range(0,x):
#     cash = []
#     for j in range(0,x):
#         cash.append(0)
#     mass.append(cash)
