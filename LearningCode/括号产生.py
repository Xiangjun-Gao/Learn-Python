n=eval(input(""))
l=n
r=n
ls=[]
def judge(l,r,s):
    if l==0 and r==0:
        ls.append(s)
    elif l>r or l<0 or r<0:
        pass
    else:
        judge(l-1,r,s+'(')
        judge(l,r-1,s+')')

judge(l,r,'')
print(ls)
