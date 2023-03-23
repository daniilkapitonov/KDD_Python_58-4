a = int(input("Ведите число - "))
if a>=1 and a<=6:
    print("Принадлежит всем отрезкам")
else:
    print("Не принадлежит всем отрезкам")
    if a>=1 and a<=11:
        print(">=1 <=11")
    if a>=0 and a<=100:
        print(">=0 <=100")
    if a<=6:
        print("<=6")