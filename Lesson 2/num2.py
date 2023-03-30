# def func(a, b):
#     s = a+b
#     if s%10 > 5:
#         return 'a'
#     elif s%10 <=5:
#         return 'b'
x = [5,7,3,6,8,0,3,4,7,9,0,2]
y = [9,6,3,6,8,3,6,8,4,5,7,4]
# res=[]
# for i in range(len(x)):
#     res.append(func(x[i], y[i]))
# print(res)
# print()
print(list(map(lambda a,b: 'a' if (a+b)%10>5 else 'b', x,y)))
