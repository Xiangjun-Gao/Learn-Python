def triangle(n):
    L=[1]
    for j in range(n):
        yield L
        L.insert(0,0)
        L.append(0)
        L=[L[i]+L[i+1] for i in range(len(L)-1)]

for i in triangle(10):
    print(i)
    
