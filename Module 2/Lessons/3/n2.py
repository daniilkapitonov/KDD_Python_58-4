from tkinter import *  
from tkinter import messagebox

def count(zn):
    if zn=="+":
        messagebox.showinfo("Result", int(e1.get())+int(e2.get()))
    elif zn =="-":
        messagebox.showinfo("Result", int(e1.get())-int(e2.get()))
    elif zn=="*":
        messagebox.showinfo("Result", int(e1.get())*int(e2.get()))
    elif zn=="/":
       if int(e2.get())!=0:
           messagebox.showinfo("Result", int(e1.get())/int(e2.get())) 
       else:
           messagebox.showerror("Err","Деление на 0")

main = Tk()
main.geometry("200x200")
e1 = Entry(main)
e1.pack()
e2 = Entry(main)
e2.pack()
Button(main, text="+",width=4, command=lambda:count("+")).pack(side=LEFT)
Button(main, text="-",width=4, command=lambda:count("-")).pack(side=LEFT)
Button(main, text="*",width=4, command=lambda:count("*")).pack(side=LEFT)
Button(main, text="/",width=4, command=lambda:count("/")).pack(side=LEFT)
main.mainloop()