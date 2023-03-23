import n1_m
from random import randint

for i in range(10):
    n1 = randint(0,100)
    n2 = randint(0,100)
    print("- ", n1_m.minus(n1,n2), n1-n2)
input()