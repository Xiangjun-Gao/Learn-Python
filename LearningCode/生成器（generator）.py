#生成器（generator）
[x**2 for x in range(10)]

def fib(max):
    n,a,b=0,0,1
    while(n<max):
        yield b
        a,b=b,a+b
        n+=1
    return 'done'

f=fib(10)        #f is a generator
next(f)
for n in fib(10):
    print(n,end="  ")#n是返回的 yield b 的值
    pass
