from tkinter import *

root=Tk()
root.title("简易菜单栏")
root.geometry("300x300")
menubar=Menu(root)

fmenu=Menu(menubar)
for item in["New File","Open","Save","Save as"]:
    fmenu.add_command(label=item)#贴一层菜单，add_command
emenu=Menu(menubar)
for item in["About IDLE","IDLE Help","Demo"]:
    emenu.add_command(label=item)
vmenu=Menu(menubar)
for item in["Copy","paste","Cut"]:
    vmenu.add_command(label=item)

menubar.add_cascade(label='File',menu=fmenu)#贴两层级联菜单，add_cascade(
menubar.add_cascade(label='Edit',menu=vmenu)
menubar.add_cascade(label='Help',menu=emenu)#做好子菜单，再做上层菜单
for item in["Run","Exit"]:
    menubar.add_command(label=item)#add_command用来添加菜单项
    
root['menu']=menubar#把menubar放在root的顶部
root.mainloop()
