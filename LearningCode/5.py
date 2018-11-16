l1=eval(input(""))
count={}

for word in l1:
    count[word]=count.get(word,0)+1
    
l2=list(count.items())
l2.sort(key=lambda x:x[1],reverse=True)


def select():
    max=l2[0][1]
    l3=[]
    for i in l2:
        if(i[1]==max):
            l3.append(i[0])
    for i in l1:
        if i in l3:
            return i

s=select()     
print(s)   
