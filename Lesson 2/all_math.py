import math

l = [True,True,True]
l1 = [0,-11,11]
print(all(l))
print(all(l1))
print(any(l1))
flag = True
for i in l:
    if i==False:
        flag = False
print(flag)

numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
result = all(map(lambda x: True if x > 10 else False, numbers))
if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')
    
print('Все числа больше 10' 
      if all(map(lambda x: True if x > 10 else False, numbers)) else
      'Хотя бы одно число меньше или равно 10')
