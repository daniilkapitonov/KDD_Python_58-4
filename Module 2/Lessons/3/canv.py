from tkinter import *  

def ch():
    global check
    if check:
        can.itemconfig(tr, fill="pink")
        check = False
    else:
        can.itemconfig(tr, fill="blue")
        check = True
check = True
main = Tk()
main.geometry("500x500")
can = Canvas(main, height=300, width=300, bg="red")
can.pack()
can.create_line(20,20,230,230, width=4)
can.create_rectangle(180,180, 290,200,width=4, activefill="black")
can.create_oval(100,80, 140,200,width=4, fill="yellow", dash=(10,10,10))
tr = can.create_polygon(280,280,200,10,170,230, width=4, fill="blue")
Button(main, text="BTN", command=ch).pack()
main.mainloop()