def func(par1=2, par2=0,par3=""):
    print("Hello")
    print("Good")
    for i in range(par1):
        print(i, end = " ")
    print()
    return par2+20

print(func(10))


def hello(name, time):
    print("Hello", name)
    print("Cur time", time)
    return "Ok"


a = hello("daniil", "12:00")
print(hello("daniil", "12:00"))