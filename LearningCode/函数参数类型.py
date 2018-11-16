def person1(name,age,*args,**kw):#姓名，年龄必须输入，hobby选择输入，city，job，home+eles选择输入
	print("name:",name,'age:',age)
	print("hobby:",end="")
	for i in args:#列表
		print(i,end=" ")
	print("")
	print(kw)#字典
	print("")

def person2(name,age,*args,city,home):#姓名，年龄必须输入，hobby选择输入，关键字参数city，home必须输入且不能输入其他
	print("name:",name,'age:',age)
	print("hobby:",end="")
	for i in args:
		print(i,end=" ")
	print("")
	print("city:",city,'home:',home)
	print("")
def person3(name,age,*,city,home):#姓名，年龄必须输入，hobby不输入，关键字参数city，home必须输入且不能输入其他
	print("name:",name,'age:',age)
	print("")
	print("city:",city,'home:',home)
	print("")
	
extra={'city':'Beijing','home':'Qingdao'}#写了job，就无法运行
person1('gxj',20,'basketball','books',city="Beijing",home='Qingdao')#
person2('jack',20,**extra)
person2('jack',20,'basketball',**extra)
person3('jack',20,**extra)



