f = open(r'C:\Users\dan-1\Desktop\Pr_2035\KDD_Python_58-4\Lessons\4\t_w.txt', "a") 
#w - перезапись а - дозапись
f.write("Hello!")
txt = ["asd\n","qwe\n","dfh\n"]
f.writelines(txt)
f.close()