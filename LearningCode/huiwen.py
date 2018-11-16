#huiwen.py
str=input("str=")
len=len(str)
i=0
while(i<len):
    if str[i]==str[-1-i]:
       i=i+1 
    else:
        print("No")
        break
    if i+1==len:
        print("Yes")
