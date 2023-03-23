# a = input('Введите строку - ') #Первый вариант решения
# maxs = 0 
# flag = False
# count = 0
# for l in a:
#     if l == "Р":
#         flag = True
#         count +=1
#     else:
#         flag = False
#         if count>maxs:
#             maxs = count
#         count = 0
# if count>maxs:
#     maxs = count
# print(maxs)
a = input('Введите строку - ').split('О')
print(a)
s = max(a,key=len)
print(len(s))