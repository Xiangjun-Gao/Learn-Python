#复选框
from tkinter import *

root=Tk()
root.title("复选框")
root.geometry("300x300")
time1=0
time2=0
def f1():
    global time1,l
    if time1%2==0:
        l['text']="Cletrics Wins"
        time1=time1+1
    else:
        l['text']="Cletrics Loses"
        time1=time1+1
def f2():
    global time2,l
    if time2%2==0:
        l['text']="Cavs Wins"
        time2=time2+1
    else:
        l['text']="Cavs Loses"
        time2=time2+1

c1=Checkbutton(root,text="Cletrics",command=f1)
c1.pack()
c2=Checkbutton(root,text="Cavaliars",command=f2)
c2.pack()

l=Label(root,text=" ")
l.pack()

root.mainloop()
