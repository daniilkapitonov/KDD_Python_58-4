from tkinter import *  
from tkinter import messagebox

def btn():
    messagebox.showinfo("Info","Text info")
    messagebox.showerror("Err","Text Err")
    messagebox.showwarning("Warn","Text Warn")
    print(messagebox.askretrycancel("Ask","Question"))
    

main = Tk()
main.geometry("200x200")
Button(main, text="MSG", command=btn).pack()
main.mainloop()