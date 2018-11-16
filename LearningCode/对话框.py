#对话框
from tkinter.dialog import *
from tkinter import *

def xin():
    d=Dialog(None,title="NBA MVP",text="Who do you think is MVP?",#以下属性不可缺少
             bitmap=DIALOG_ICON,default=0,strings=("Stefen Curry","Lebron James","James Harden"))
    print(d.num)


t=Button(None,text="investagation",comman=xin)
t.pack()
b=Button(None,text="Close",command=t.quit)
b.pack()

t.mainloop()
