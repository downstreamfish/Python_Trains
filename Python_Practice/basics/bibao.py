#内部函数的闭包
'''
def funx(x):
    def funy(y):
        return x * y
    return funy

i = funx(4)
print(type(i))
print(i(8))
'''

def fun1():
    x = 6
    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()

m = fun1()
print(m)
