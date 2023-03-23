from tkinter import *
# import tkinter

def func():
    print("Hello")
    print("Good")
    txt = e1.get()
    l1.config(text = txt)

main = Tk()
main.title("First app")
main.geometry("400x400")
l1 = Label(main,text="Я есть label", font = 20)
l1.pack()
e1 = Entry(main)
e1.pack()
Button(main,text="Кнопка",font = 20, bg="Red", activebackground="Blue", 
       command=func).pack()
# Label(text="Я есть label").pack()
# Entry().pack()
# Button(text="Кнопка").pack()
main.mainloop()
