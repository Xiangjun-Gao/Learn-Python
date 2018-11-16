from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
import random
import copy

#################################
class Grid(object):#绘制画布，对画布进行装饰，显示：score，message，背景
    '''
    属性：window_width=500,window_height=400,grid_width=20
    方法：draw    generate_grid_list
    '''
    def __init__(self,root=None,window_width=400,window_height=500,grid_width=100,bg='white'):
        self.width=window_width
        self.root=root
        self.height=window_height
        self.grid_width=grid_width
        self.bg="gray"
        self.canvas=Canvas(root,width=self.width,height=self.height,bg=self.bg)
        self.ft = tkFont.Font(family='Fixdsys', size=25, weight=tkFont.BOLD)
        self.canvas.create_text(100,450,text="Time:",font=self.ft)
        self.canvas.create_text(300,450, text="Score:", font=self.ft)
        self.canvas.pack()
        self.value_color = {0: "white", 2: "yellow", 4: "yellow", 8: "yellow", 16: "yellow", 32: "yellow",
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
        self.canvas.create_rectangle(y+5,x+5,y+self.grid_width-5,x+self.grid_width-5,
                                     outline='green',fill=self.value_color[value])
        if not value==0:
            self.canvas.create_text(y + self.grid_width / 2, x + self.grid_width / 2, text=value,
                                    font=self.ft)

#################################
class Grid_dict(object):
    def __init__(self,Grid):
        self.grid=Grid
        self.grid_dict=self.grid.grid_dict
        self.grid_dict_expand()
        self.display_grid_dict()
        self.grid.root.bind('<Up>',self.Up)
        self.grid.root.bind('<Down>',self.Down)
        self.grid.root.bind('<Right>',self.Right)
        self.grid.root.bind('<Left>',self.Left)

    def grid_dict_expand(self):
        for i in range(4):
            self.grid_dict[(i,-1)]=-1
        for i in range(4):
            self.grid_dict[(-1,i)]=-1
        for i in range(4):
            self.grid_dict[(i,4)]=-1
        for i in range(4):
            self.grid_dict[(4,i)]=-1

    def display_grid_dict(self):
        print(self.grid_dict)
        for i in self.grid_dict:
            if 3>=i[0]>=0 and 3>=i[1]>=0:
                self.grid.draw(i, self.grid_dict[i])

    def judge_get_2048(self):
        '''判断是否达到2048，达到：True  未到达：FALSE'''
        for i in self.grid_dict:
            if self.grid_dict[i]==2048:
                return True
        return False

    def judge_go_on(self):
        '''可继续执行：true  不能继续：FALSE'''
        for i in range(4):
            for j in range(4):
                if self.grid_dict[(i,j)] in [self.grid_dict[(i,j-1)],self.grid_dict[(i,j+1)],
                                             self.grid_dict[(i-1,j)],self.grid_dict[(i+1,j)]]:
                    return True
        return False

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
            while (self.grid_dict[pos] != 0):
                pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value
        else:
            pass

        self.display_grid_dict()

        if self.judge_get_2048()==True:
            message = tkinter.messagebox.showinfo("Congratulations!")
            if message=='ok':
                sys.exit()

        if self.judge_go_on()==False:
            message = tkinter.messagebox.showinfo("Game Over")
            if message=='ok':
                sys.exit()

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
            while (self.grid_dict[pos] != 0):
                pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value
        else:
            pass

        self.display_grid_dict()

        if self.judge_get_2048()==True:
            message = tkinter.messagebox.showinfo("Congratulations!")
            if message=='ok':
                sys.exit()

        if self.judge_go_on()==False:
            message = tkinter.messagebox.showinfo("Game Over")
            if message=='ok':
                sys.exit()

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
            while (self.grid_dict[pos] != 0):
                pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value
        else:
            pass

        self.display_grid_dict()
        if self.judge_get_2048()==True:
            message = tkinter.messagebox.showinfo("Congratulations!")
            if message=='ok':
                sys.exit()

        if self.judge_go_on()==False:
            message = tkinter.messagebox.showinfo("Game Over")
            if message=='ok':
                sys.exit()

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
            while (self.grid_dict[pos] != 0):
                pos, value = self.grid.generate_food()
            self.grid_dict[pos] = value
        else:
            pass

        self.display_grid_dict()
        if self.judge_get_2048()==True:
            message = tkinter.messagebox.showinfo("Congratulations!")
            if message=='ok':
                sys.exit()

        if self.judge_go_on()==False:
            message = tkinter.messagebox.showinfo("Game Over")
            if message=='ok':
                sys.exit()

################################
if __name__=='__main__':
    root=Tk()
    root.title='2048'
    grid=Grid(root)
    grid_dict=Grid_dict(grid)
    root.mainloop()