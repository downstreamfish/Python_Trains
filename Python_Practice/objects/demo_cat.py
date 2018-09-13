#! /usr/bin/python3


class Cat:

    """ 这是一个猫类
    """

    def __init__(self, name):
        print("这是一个初始化方法")
        self.name = name

    def eat(self):
        print("小猫%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫在喝水")


tom = Cat("Tom")
tom.drink()
tom.eat()
print("cat id %x" % id(tom))

lazy_cat = Cat("大蓝猫")

lazy_cat.drink()
lazy_cat.eat()
print('lazy_cat id %x' % id(lazy_cat))
