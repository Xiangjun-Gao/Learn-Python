#继承和多态

class Animal(object):
    def run(self):
        print("Animal is running")
        
class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

class A(object):
    def run(self):
        print("A is running slowly")

def run_twice(animal):#Java是静态语言，使用的是Animal，python动态语言，不能使用Animal
    animal.run()#Java传入的对象，必须是Animal类型，Python传入的对象只要有一run方法就行
    animal.run()

dog=Dog()
cat=Cat()
animal=Animal()
a=A()

dog.run()
cat.run()


run_twice(dog)
run_twice(cat)
run_twice(animal)
run_twice(a)

