from tkinter import *

root=Tk()
root.title("人生苦短，要学python")
root.geometry('300x200')

Button(root,text="A").pack(side=LEFT,expand=YES,fill=Y)
Button(root,text="B",width=10,height=2).pack(side=TOP,expand=YES,fill=BOTH)


root.mainloop()


def entry_label():
    win=Tk()
    win.title("人生苦短，要学python")
    win.geometry("300x300")

    Label(win,text="ID:").grid(row=0,column=0,sticky=W) #左对齐
    Entry(win).grid(row=0,column=1,sticky=E)
    
    Label(win,text="Password:").grid(row=1,column=0,sticky=W) #左对齐
    Entry(win).grid(row=1,column=1,sticky=E)

    Button(win,text="Log In").grid(row=2,column=1,sticky=E)

    win.mainloop()
entry_label()

def winlabel():
    #按钮绑定函数：在主窗口上加一个标签
    global win
    s=Label(win,text="Learn English").grid(sticky=E)


    
    
    
    
"""
介绍以下几个控件的用法

Label
Frame
Entry
Text
Button
Listbox
Scrollbar
说明每个控件最后要加上pack().否则控件是无法显示的.
"""
