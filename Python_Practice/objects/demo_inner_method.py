#! /usr/bin/python3


class Cat:
    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    def __str__(self):
        return '我是小猫：%s' % self.name


# tom是一个全局变量
tom = Cat("Tom")
print(tom.name)
print(tom)

# del 关键字可以删除一个对象
del tom

print('-' * 40)
