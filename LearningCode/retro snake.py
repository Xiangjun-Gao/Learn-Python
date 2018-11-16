from tkinter import *
import tkinter.messagebox
from random import randint
import sys
import time

class Grid(object):
    def __init__(self,root=None,window_width=500,window_height=400,grid_width=20,offset=10):
        self.height=window_height
        self.width=window_width
        self.grid_width=grid_width
        self.offset=offset
        self.grid_x=self.width//self.grid_width
        self.grid_y=self.height//self.grid_width
        self.bg="gray"
        self.canvas=Canvas(root,width=self.width,height=self.height,bg=self.bg)
        self.canvas.pack()
        self.generate_grid_list()#产生网格坐标grid_list

    def draw(self,pos,color):#画出坐标点处对应的网格
        x=pos[0]*self.grid_width
        y=pos[1]*self.grid_width
        self.canvas.create_rectangle(x,y,x+self.grid_width,y+self.grid_width,fill=color,outline=self.bg)

    def generate_grid_list(self):#产生网格列表，变成属性
        grid_list=[]
        for y in range(0,self.grid_y):
            for x in range(0,self.grid_x):
                grid_list.append((x,y))
        self.grid_list=grid_list

class Food(object):#随机产生食物，并画在grid
    def __init__(self,Grid):
        self.grid=Grid
        self.color="#23d978"
        self.set_pos()#产生self.pos

    def set_pos(self):
        x=randint(0,self.grid.grid_x-1)
        y=randint(0,self.grid.grid_y-1)
        self.pos=(x,y)

    def display(self):
        #画布上画上食物
        self.grid.draw(self.pos,self.color)#

class Snake(object):
    def __init__(self,Grid):
        self.grid=Grid
        self.body=[(10,6),(10,7),(10,8)]
        self.direction="Up"
        self.status=['run','stop']
        self.speed=1000
        self.color='red'
        self.food=Food(self.grid)
        self.game_over=False
        self.score=0
        self.display_snake()
        self.display_food()

    def find_available_grid(self):
        available_grid=[]
        for i in self.grid.grid_list:
            if i not in self.body:
                available_grid.append(i)
        return available_grid
        #return [i for i in self.grid.grid_list if i not in self.body]#self.body需要时刻更新

    def display_food(self):
        '''排除失误出现在蛇的位置，直到出现合理的食物位置'''
        while(self.food.pos in self.body):
            self.food.set_pos()
        self.food.display()

    def display_snake(self):
        '''显示蛇的位置'''
        for (x,y) in self.body:
            print(1,(x,y))
            self.grid.draw((x, y), self.color)




    def change_direction(self,direction):#为什么这样写
        self.direction = direction

    def move(self):#snake_update：已知direction 和 food 位置，move一下并画出来,并产生新的food
        head = self.body[0]
        if self.direction == 'Up':
            new=(head[0],head[1]-1)
        elif self.direction =="Down":
            new=(head[0],head[1]+1)
        elif self.direction =="Left":
            new=(head[0]-1,head[1])
        else:
            new=(head[0]+1,head[1])
        print(head,new)
        if not self.food.pos == head:#此时，食物没出现在蛇头
            pop=self.body.pop()
            self.grid.draw(pop,self.grid.bg)#这条语句是为了，将蛇尾调成背景色，看起来就像消失了一样
        else:  #食物在蛇头，此时已经吃完
            self.display_food()     #显示新的符合坐标要求的食物
            self.score+=1   #分数加一

        self.body.insert(0,new)#根据 direction ，向队列中添加头部的食物

        if not new in self.find_available_grid():#此次移动完成后，判断游戏是否可以继续，若不可以
            self.status.reverse()#修改游戏继续参数 的值
            self.game_over = True
        else:
            self.grid.draw(new,color=self.color)#若可以继续，画出头部元素
'''
class SnakeGame(Frame):#获得键盘输入，并不断刷新界面，调用move函数
    def __init__(self,root=None,*args,**kwargs):
        Frame.__init__(self,root)
        self.grid=Grid(root=root,*args,**kwargs)
        self.snake=Snake(self.grid)
        self.bind_all('<KeyRelease>',self.key_release)#估计也是继承下来的

    def run(self):#未捕获按键时调用此函数->move
        if not self.snake.status[0] == 'stop':
            self.snake.move()
        if self.snake.game_over ==True:
            message = tkinter.messagebox.showinfo("Game Over","you score:{}".format(self.snake.score))
            if message=='ok':
                sys.exit()
        self.after(self.snake.speed,self.run)#父类继承下来的方法

    def key_release(self,event):#捕获按键时调用此函数->move
        key=event.keysym
        print(key)
        key_dict = {'Up':'Down','Down':'Up','Left':'Right','Right':'Left'}

        if key_dict.has_key(key) == True and not key == key_dict[self.snake.direction]:
            #捕获的按键是上下左右，而不是其他的   ；   按键不能是目前行进方向的反方向
            self.snake.change_direction(key)
            self.snake.move()
'''

if __name__=='__main__':
    root=Tk()
    root.title('greedy snake')
    grid=Grid(root)
    snake=Snake(grid)

    while(snake.game_over==True):
        time.sleep(0.5)
        snake.move()

    root.mainloop()
