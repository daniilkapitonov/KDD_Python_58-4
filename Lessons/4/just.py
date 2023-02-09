from random import randint
for i in range(9):
    for j in range(9):
        print(str(randint(0,120)).rjust(4), end="")
    print()
    
s = "1,2,3,4,5,6,7,8,9"
print(s.split(","))
s = s.split(",")
print(",".join(s))