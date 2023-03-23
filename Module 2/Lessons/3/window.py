from tkinter import *

main = Tk()
main.geometry("200x200")
main.resizable(False,True)
print(eval("(2+(2*4))/2"))
n1 = "2"
n2 ="32"
z= "+"
print(n1+z+n2,eval(n1+z+n2))
Button(main, text="Hello!").place(x=100,y=100)
main.mainloop()