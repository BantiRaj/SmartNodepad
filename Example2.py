from tkinter import  *
from tkinter import  ttk
def func():
    l2.configure(text=cb.get())
root = Tk()
root.geometry('200x200')
course=("JAVA","Python","C & C++")
l1=Label(root,text="Choose Your Favourite Language")
l1.grid(column=0, row = 0)
cb = ttk.Combobox(root,values=course,width=10)
cb.grid(column=0, row = 1)
cb.current(0)
b = Button(root,text="click here",command=func)
b.grid(column = 0, row = 2)
l2=Label(root,text="")
l2.grid(column=0 ,row=3)
root.mainloop()