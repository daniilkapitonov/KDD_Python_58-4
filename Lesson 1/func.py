def count_args(*args):
    return len(args)

def ret():
    summ = 0
    for i in range(0,10):
        print(i,end = " ")
        summ +=i
    return summ

def mean(*a):
    summ = 0
    count = 0
    for item in a:
      if type(item) == int or type(item) == float:
          summ+=item
          count +=1
    if count == 0:
        return 0
    return summ/count

def greet(*a):
    text = "Hello, "
    for i in range(0,len(a)-1):
        text+=a[i]
        if i+1 == len(a)-1:
            text += " and "
        else:
            text +=", "
    text +=a[-1]+'!'
    return text


print(count_args(1,2,3,4,5,"asdasd",[1,2,3],{1:2,3:1}))
print(count_args())
print()
print(mean())
print(mean(True, ['Sergey'], 'Kotov', 2.5, (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(greet('Timur'))

