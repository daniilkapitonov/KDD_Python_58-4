f = open(r'C:\Users\dan-1\Desktop\Pr_2035\KDD_Python_58-4\Lessons\4\text.txt', "r")
s = f.read()
print(s)
s = s.replace("\n"," ")
print(s)
s = s.split(" ")
print(s)
sum = 0
for i in s:
    sum+=int(i)
print("Sum = ",sum)
f.close()