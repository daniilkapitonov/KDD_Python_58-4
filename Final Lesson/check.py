# n = input("Введите числа через пробел - ").split(' ')
# a = list(map(lambda x: int(x)**3, n))
# print(sum(filter(lambda x: (x)>0, a)))

print(sum(filter(lambda x: x>0, list(map(lambda x: int(x)**3, 
        input("Введите числа через пробел - ").split(' '))))))