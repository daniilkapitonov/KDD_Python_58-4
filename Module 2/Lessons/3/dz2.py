def plus(n1,n2):
    return n1+n2

def minus(n1,n2):
    return n1-n2

def umn(n1,n2):
    return n1*n2

def delenie(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        print("Ошибка деления на ноль")
        return 0
    
c1 = 0
c2 = 0
while True:
    c1 = int(input("1 val "))
    c2 = int(input("2 val "))
    zn = input("Znak ")
    if zn=="+":
        print("result = ",plus(c1,c2))
    elif zn =="-":
        print("result = ",minus(c1,c2))
    elif zn=="*":
        print("result = ",umn(c1,c2))
    elif zn=="/":
        print("result = ",delenie(c1,c2))
    else:
        print("Такого знака нет")