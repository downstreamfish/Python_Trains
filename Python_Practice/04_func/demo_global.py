#! /usr/local/bin/python3


gl_num = 10


def demo1():
    print("demo1" + '-' * 40)

    # global 关键字, 告诉Python解释器num是一个全局变量
    global num
    # 只是定义了一个局部变量, 不会修改到全局变量,只是变量名相同而已
    num = 100
    print(num)


def demo2():

    print("demo2" + '-' * 40)
    print(num)


demo1()
demo2()

print("over")
