from tkinter import *

def plus():
    l['text'] = int(e1.get()) + int(e2.get())
    
main = Tk()
main.geometry("200x200")
e1 = Entry(main)
e1.pack()
e2 = Entry(main)
e2.pack()
l = Label(main)
l.pack()
b = Button(main, text="Summ", command=plus)
b.pack()
main.mainloop()