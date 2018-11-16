import turtle

count=12
xscale=35#每个圆柱对应的宽度
yscale=0.7#没出现一次对应高度
datas=[]#每个单词对应出现次数
words=[]#前counts个单词
wordcounts={}#存储所有键值对

#####################Turtle Start#####################
#绘制直线段
def drawline(t, x1, y1, x2, y2):
    t.penup()
    t.goto (x1, y1)
    t.pendown()
    t.goto (x2, y2)

def drawtext(t,x,y,word):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(word)

#绘制一个柱体
def drawbar(t,x,y):#x,y is index
    x0=x
    x=x*xscale
    y=datas[y]*yscale
    drawline(t,x,0,x,y)
    drawline(t,x,y,x+xscale,y)
    drawline(t,x+xscale,y,x+xscale,0)
    drawline(t,x+xscale,0,x,0)

    drawtext(t,x+0.4*xscale,-20,words[x0])
    drawtext(t,x+0.4*xscale,y+15,datas[x0])

#绘制多个柱体
def drawsomebars(t):
    l=len(words)
    for x in range(l):
        y=x
        drawbar(t,x,y)

#绘制坐标系
def drawaxis(t,x,y):
    #x is 
    drawline(t,0,0,x*xscale,0)
    t.seth(-150)
    t.fd(xscale*0.5)
    drawline(t,0,0,x*xscale,0)
    t.seth(150)
    t.fd(xscale*0.5)
    
    drawline(t,0,0,0,1.3*datas[0]*yscale)
    t.seth(-60)
    t.fd(xscale*0.5)
    drawline(t,0,0,0,1.3*datas[0]*yscale)
    t.seth(-120)
    t.fd(xscale*0.5)
    
#画图
def drawgraph():
    t=turtle.Turtle()
    turtle.title('词频结果柱状图')
    turtle.setup(900, 750)
    #'Turtle' object has no attribute 'title'
    #不能写成t.setup()
    t.pensize(3)
    t.speed(200)
    drawaxis(t,count+2,200)
    drawsomebars(t)
    t.hideturtle()
    turtle.done()
#####################Turtle END#####################

#####################Calc Start#####################
def replacepunc(line):
    for ch in '!@#$%^&*()-_=+~`[{]}\|;:"/?.>,<':
        line.replace(ch,"")
    return line

def getText():
    #txt : 元素 为 字符串 的 列表 ["","",""]
    txt=open("hamlet.txt","r").readlines()
    return txt

def split_txt_to_dict(txt):
    excludes = ['the', 'and', 'of', 'you', 'a', 'i', 'my', 'in', 'to', 'it', 'is', 'not', 'his', 'this', 'but']
    for line in txt:
        line=replacepunc(line)
        line=line.lower()
        ls=line.split()
        for word in ls:
            if word in excludes:
                pass
            else:
                wordcounts[word]=wordcounts.get(word,0)+1
def main():
    txt=getText()

    split_txt_to_dict(txt)
                
    l=list(wordcounts.items())
    #[(),()]
    l=sorted(l,key=lambda x:x[1],reverse=True)
    #or l.sort(key=lambda x:x[1],reverse=True)
    
    for i in range(count):
        #将所有键值对，出现次数在最多的counts个提取
        words.append(l[i][0])
        datas.append(l[i][1])
    print(words)
    print(datas)
    drawgraph()
#####################Calc End  #####################
    
main()