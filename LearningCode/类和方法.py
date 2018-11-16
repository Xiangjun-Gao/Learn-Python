#类和实例
#类属性和对象属性（千万不能重名，引起错误）
class Student(object):
    
    num='freshman'#属性1
    
    def __init__(self,name,score):#属性2
        self.name=name
        self.score=score
        
    def print_score(self):
        print('%s,%s'%(self.name,self.score))
        
    def get_grade(self):
        if self.score>90:
            return 'A'
        elif self.score>60:
            return "C"
        else:
            return "D"


bart=Student("reed",99)

bart.score+=1#属性修改

bart.num='NO.2'
print("num:",bart.num)#实例属性优先级 > 类属性优先级
del bart.num
print("num:",bart.num)#删除实例属性后，得到的是类属性

bart.gender='men'#属性增加
print("score:",bart.print_score())#无返回值，返回None
print("grade:",bart.get_grade())
