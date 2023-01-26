from tkinter import *
# import tkinter
def f(e,l):
    t = e.get()
    l.config(text = t)

main = Tk()
main.title("Регистрация")
main.geometry("600x600")
Label(text = 'Введите ФИО').pack()
e1=Entry().pack()
l1 = Label(text = '').pack()
Button(text = 'ок',command=f(e1,l1)).pack()
Label(text = 'Введите номер телефона').pack()
e2=Entry().pack()
l2=Label(text = '').pack()
Button(text = 'ок',command=f(e2,l2)).pack()
Label(text = 'Введите эл. почту').pack()
e3=Entry().pack()
l3=Label(text = '').pack()
Button(text = 'ок',command=f(e3,l3)).pack()
main.mainloop()