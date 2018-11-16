str1=input("")
for p in str1:
    if ord('a')<=ord(p)<=ord('z'):
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end="")
    elif ord('A')<=ord(p)<=ord('Z'):
        print(chr(ord("A")+(ord(p)-ord("A")+3)%26),end="")
    else:
        print(p,end="")
