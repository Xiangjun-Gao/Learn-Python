#螺旋矩阵
def huihuan(x1,y1,x2,y2,res,matrix):
    if x2-x1==0:
        for i in range(y2-y1+1):
            res.append(matrix[x1][y1+i])
    elif y2-y1==0:
        for i in range(x2-x1+1):
            res.append(matrix[x1+i][y1])
    elif x2-x1==1:
        for i in range(y2-y1):
            res.append(matrix[x1][y1+i])
        for i in range(x2-x1):
            res.append(matrix[x1+i][y2])
        for i in range(y2-y1):
            res.append(matrix[x2][y2-i])
        for i in range(x2-x1):
            res.append(matrix[x2-i][y1])
    elif y2-y1==1:
        for i in range(y2-y1):
            res.append(matrix[x1][y1+i])
        for i in range(x2-x1):
            res.append(matrix[x1+i][y2])
        for i in range(y2-y1):
            res.append(matrix[x2][y2-i])
        for i in range(x2-x1):
            res.append(matrix[x2-i][y1])
    else:
        for i in range(y2-y1):
            res.append(matrix[x1][y1+i])
        for i in range(x2-x1):
            res.append(matrix[x1+i][y2])
        for i in range(y2-y1):
            res.append(matrix[x2][y2-i])
        for i in range(x2-x1):
            res.append(matrix[x2-i][y1])
        huihuan(x1+1,y1+1,x2-1,y2-1,res,matrix)

def SpiralOrder(matrix):
    res=[]
    m=len(matrix)
    if m==0:
        return []
    n=len(matrix[0])
    huihuan(0,0,m-1,n-1,res,matrix)
    return res

matrix = eval(input())
res = SpiralOrder(matrix)
print(res)
 
