for i in range(1,10,2):
    for j in range(1,10):
        print(i,"*",j,"=",i*j, end="  ")
        print(i+1,"*",j,"=",(i+1)*j)
    print()