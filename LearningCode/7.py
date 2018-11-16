l1=input("")
l2=[]
for i in l1:
    if i in["(",")"]:
        l2.append(i)
'''
def judge():
    if(l2[0]==")"):
        return 0
    j=0
    for i in l2:
        if j%2==1:
            pass
        else:
            if i=="(":
                if l2[j+1]==")":
                    pass
                else:
                    return 0
            else:
                    return 0
        j=j+1
        
    return 1
d={1:"配对成功",0:"配对不成功"}
print(d[judge()])
'''
def judge():
    s=0
    for i in l2:
        if i=="(":
            s=s+1
        else:
            s=s-1
        if s<0:
            return 0
    if s==0:
        return 1
    else:
        return 0
d={1:"配对成功",0:"配对不成功"}
print(d[judge()])
