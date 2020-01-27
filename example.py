from tkinter import *

def hello():
    str=T.get((1.0,END))
    print(str)

root=Tk()
menubar = Menu()
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=hello)
filemenu.add_command(label="Open",command=hello)
filemenu.add_command(label="Save",command=hello)
filemenu.add_command(label="Save as",command=hello)
filemenu.add_command(label="Close",command=hello)
filemenu.add_command(label="Exit",command=root.quit)
root.config(menu=menubar)
S = Scrollbar(root)
T = Text(root,height=2, width=30)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
str="Just a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text WidgetJust a Text Widget"
T.insert(END,str)
root.mainloop()