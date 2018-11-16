from tkinter import *

def reg():
    content1=e1.get()
    content2=e2.get()
    t1=len(content1)
    t2=len(content2)

    if content1=="111" and content2=="222":
        c['text']="登陆成功"
    else:
        c['text']="登陆失败"
        e1.delete(0,t1)
        e2.delete(0,t2)
        

win=Tk()
win.title("人生苦短，要学python")
win.geometry("300x300")


Label(win,text="ID:").grid(row=0,column=0,sticky=W)
e1=Entry(win)
e1.grid(row=0,column=1,sticky=E)


Label(win,text="Password:").grid(row=1,column=0,sticky=W)
e2=Entry(win)
e2['show']="*"
e2.grid(row=1,column=1,sticky=E)


Button(win,text="Log In",command=reg).grid(row=2,column=1,sticky=E)


c=Label(win,text="1")#由此可见，command=reg语句是Button被按钮安国之后执行的
c.grid(row=3)


win.mainloop()
