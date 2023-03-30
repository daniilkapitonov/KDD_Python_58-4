def f(a,c,d):
    s = int(a)
    return c*d*s

fl = lambda a,c,d: a*c*d

print(f(1,2,3))
print(fl(1,2,3))

step = lambda a: a+1
def square(a):
    return a**2
a = [4,6,7,3,1,-1,0,-20,35]
a = list(map(step,a))
print(map(step,a))
# for i in range(0,len(a)):
#     a[i]+=1
print(a)
print()
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20,30]
numbers3 = [100, 200, 300, 400, 500]
def func(elem1, elem2, elem3):
    print(elem1,elem2,elem3)
    return elem1 + elem2 + elem3
print(list(map(func,numbers1,numbers2,numbers3)))
print()
circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]
result1 = list(map(round, circle_areas,[1]*len(circle_areas))) 
result2 = list(map(round, circle_areas,[i for i in range(1,len(circle_areas)+1)]))
print(circle_areas)
print(result1)
print(result2)
