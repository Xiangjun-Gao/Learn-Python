from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
import random
import copy
import time
#################################
class Grid(object):#绘制画布，对画布进行装饰，显示：score，message，背景
    '''
    属性：window_width=500,window_height=400,grid_width=20
    方法：draw    generate_grid_list
    '''
    def __init__(self,root=None,window_width=400,window_height=500,grid_width=100,bg='gray'):
        self.width=window_width
        self.root=root
        self.height=window_height
        self.grid_width=grid_width
        self.bg="gray"
        self.canvas=Canvas(root,width=self.width,height=self.height,bg=self.bg)
        self.canvas.pack()
        self.value_color = {0: "gray", 2: "yellow", 4: "yellow", 8: "yellow", 16: "yellow", 32: "yellow",
                            64: "yellow", 128: "yellow", 256: "yellow", 512: "yellow", 1024: "yellow", 2048: "yellow"}
        self.grid_list=[[(0,0),(0,1),(0,2),(0,3)],
                        [(1,0),(1,1),(1,2),(1,3)],
                        [(2,0),(2,1),(2,2),(2,3)],
                        [(3,0),(3,1),(3,2),(3,3)]]

        self.grid_dict=self.generate_grid_dict()

    def generate_food(self):
        # 返回一个元祖，一个数值，来构成键值对
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        pos = (x, y)

        l = [2, 4]
        value = random.sample(l, 1)[0]
        return pos, value

    def generate_grid_dict(self):#初始化字典
        grid_dict = dict()
        for i in self.grid_list:
            for j in i:
                grid_dict[j] = 0

        for i in range(4):
            pos, value = self.generate_food()
            grid_dict[pos] = value

        return grid_dict

    def draw(self,pos,value):
        x=pos[0]*self.grid_width
        y=pos[1]*self.grid_width
        self.canvas.create_rectangle(y+3,x+3,y+self.grid_width-3,x+self.grid_width-3,
                                     outline='green',fill=self.value_color[value])
        ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
        if not value==0:
            self.canvas.create_text(y + self.grid_width / 2, x + self.grid_width / 2, text=value,
                                    font=ft)

#################################
class Grid_dict(object):
    def __init__(self,Grid):
        self.grid=Grid
        self.grid_dict={(0, 0): 0, (0, 1): 2, (0, 2): 2, (0, 3): 2,
                        (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 4,
                        (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0,
                        (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0}
        self.display_grid_dict()
        self.grid.root.bind('<Up>',self.Up)
        self.grid.root.bind('<Down>',self.Down)
        self.grid.root.bind('<Right>',self.Right)
        self.grid.root.bind('<Left>',self.Left)

    def display_grid_dict(self):
        print(self.grid_dict)
        for i in self.grid_dict:
            self.grid.draw(i,self.grid_dict[i])

    def Up(self,event):
        '''temp_dict =dict()'''
        print('Up')
        temp_dict = copy.copy(self.grid_dict)
        # 按照捕获的方向，想将所有格子按照方向移动
        for j in range(4):
            testlist = []
            for i in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])

            while (len(testlist) < 4):
                testlist.append(0)

            for i in range(4):
                self.grid_dict[(i, j)] = testlist[i]
        #对移动后的格子进行合并
        for j in range(4):
            if self.grid_dict[(0, j)] == self.grid_dict[(1, j)] and self.grid_dict[(2, j)] == self.grid_dict[(3, j)]:
                self.grid_dict[(0, j)] = self.grid_dict[(0, j)] * 2
                self.grid_dict[(1, j)] = self.grid_dict[(2, j)] * 2
                self.grid_dict[(2, j)] = 0
                self.grid_dict[(3, j)] = 0
            else:
                for i in range(3):
                    if self.grid_dict[(i, j)] == self.grid_dict[(i + 1, j)] and self.grid_dict[(i, j)]!=0:
                        self.grid_dict[(i, j)] = 0
                        self.grid_dict[(i + 1, j)] = self.grid_dict[(i + 1, j)] * 2
                        break
            testlist = []
            for i in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])

            while (len(testlist) < 4):
                testlist.append(0)

            for i in range(4):
                self.grid_dict[(i, j)] = testlist[i]
        #合并结束

        #合并结束后，grid_dict并不改变,则并不产生食物，else 产生食物
        if  temp_dict!=self.grid_dict:
            pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value
        else:
            pass

        self.display_grid_dict()
        time.sleep(0.3)

    def Down(self,event):
        '''temp_dict =dict()'''
        print('Down')
        temp_dict = copy.copy(self.grid_dict)
        for j in range(4):
            testlist = []
            for i in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])
            #print('testlist={}'.format(testlist))
            while (len(testlist) < 4):
                testlist.insert(0,0)

            for i in range(4):
                self.grid_dict[(i, j)] = testlist[i]

        for j in range(4):
            if self.grid_dict[(0, j)] == self.grid_dict[(1, j)] and self.grid_dict[(2, j)] == self.grid_dict[(3, j)]:
                self.grid_dict[(3, j)] = self.grid_dict[(3, j)] * 2
                self.grid_dict[(2, j)] = self.grid_dict[(0, j)] * 2
                self.grid_dict[(1, j)] = 0
                self.grid_dict[(0, j)] = 0
            else:
                for i in range(3):
                    if self.grid_dict[(i, j)] == self.grid_dict[(i + 1, j)] and self.grid_dict[(i, j)]!=0:
                        self.grid_dict[(i, j)] = 0
                        self.grid_dict[(i + 1, j)] = self.grid_dict[(i + 1, j)] * 2
                        break
            testlist = []
            for i in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])

            while (len(testlist) < 4):
                testlist.insert(0, 0)

            for i in range(4):
                self.grid_dict[(i, j)] = testlist[i]

        if temp_dict!=self.grid_dict:
            pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value
        else:
            pass

        self.display_grid_dict()
        time.sleep(0.3)
        print('Down')

    def Right(self,event):
        '''temp_dict =dict()'''
        print('Right')
        temp_dict = copy.copy(self.grid_dict)
        for i in range(4):
            testlist = []
            for j in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])

            while (len(testlist) < 4):
                testlist.insert(0,0)

            print('testlist[i]={}'.format(i,testlist))

            for j in range(4):
                self.grid_dict[(i, j)] = testlist[j]


        for i in range(4):
            if self.grid_dict[(i, 0)] == self.grid_dict[(i, 1)] and self.grid_dict[(i,2)] == self.grid_dict[(i,3)]:
                self.grid_dict[(i, 3)] = self.grid_dict[(i, 3)] * 2
                self.grid_dict[(i, 2)] = self.grid_dict[(i, 0)] * 2
                self.grid_dict[(i, 1)] = 0
                self.grid_dict[(i, 0)] = 0
            else:
                for j in range(3):#和Left的对应部分代码一毛一样
                    if self.grid_dict[(i, j)] == self.grid_dict[(i , j + 1)] and self.grid_dict[(i, j)]!=0:
                        self.grid_dict[(i, j)] = 0
                        self.grid_dict[(i , j + 1)] = self.grid_dict[(i, j + 1)] *2
                        break
            testlist = []
            for j in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])

            while (len(testlist) < 4):
                testlist.insert(0, 0)

            for j in range(4):
                self.grid_dict[(i, j)] = testlist[j]

        if temp_dict!=self.grid_dict:
            pos, value = self.grid.generate_food()
            while(self.grid_dict[pos]!=0):
                pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value

        else:
            pass

        self.display_grid_dict()
        time.sleep(0.3)

    def Left(self,event):
        '''temp_dict =dict()'''
        print('Left')
        temp_dict=copy.copy(self.grid_dict)
        for i in range(4):
            testlist = []
            for j in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])

            while (len(testlist) < 4):
                testlist.append(0)

            for j in range(4):
                self.grid_dict[(i, j)] = testlist[j]

        for i in range(4):
            if self.grid_dict[(i, 0)] == self.grid_dict[(i, 1)] and self.grid_dict[(i,2)] == self.grid_dict[(i,3)]:
                self.grid_dict[(i, 0)] = self.grid_dict[(i, 0)] * 2
                self.grid_dict[(i, 1)] = self.grid_dict[(i, 3)] * 2
                self.grid_dict[(i, 2)] = 0
                self.grid_dict[(i, 3)] = 0
            else:
                for j in range(3):
                    if self.grid_dict[(i, j)] == self.grid_dict[(i , j + 1)] and self.grid_dict[(i, j)]!=0:
                        self.grid_dict[(i, j)] = 0
                        self.grid_dict[(i , j + 1)] = self.grid_dict[(i, j + 1)] * 2
                        break
            testlist = []
            for j in range(4):
                if not self.grid_dict[(i, j)] == 0:
                    testlist.append(self.grid_dict[(i, j)])

            while (len(testlist) < 4):
                testlist.append(0)

            for j in range(4):
                self.grid_dict[(i, j)] = testlist[j]

        if temp_dict!=self.grid_dict:
            pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value
        else:
            pass

        self.display_grid_dict()
        time.sleep(0.3)


if __name__=='__main__':
    root=Tk()
    root.title='2048'
    grid=Grid(root)
    grid_dict=Grid_dict(grid)
    root.mainloop()

