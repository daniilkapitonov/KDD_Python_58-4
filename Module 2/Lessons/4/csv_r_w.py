csv = open(r'C:\Users\dan-1\Desktop\Pr_2035\KDD_Python_58-4\Lessons\4\base.csv', "r")
# s = "a"
# while s!="":
#     s = csv.readline().replace("\n","")
#     print(s)
lines = csv.readlines()
print(lines)
# lines = [item.replace("\n","") for item in lines]
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n","")
for s in lines:
    for word in s.split(","):
        print(word.ljust(10), end="")
    print()
csv.close() 