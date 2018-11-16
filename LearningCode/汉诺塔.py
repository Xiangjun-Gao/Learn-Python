def hano(n,a,b,c):
    global count
    if n==1:
        print("No.{}step".format(count)+a+"->"+c)
        count+=1
    else:
        hano(n-1,a,c,b)
        hano(1,a,b,c)
        hano(n-1,b,a,c)
count=1
hano(6,'A','B','C')
