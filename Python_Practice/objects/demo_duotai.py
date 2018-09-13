class Dog:

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上玩耍" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s 和%s 愉快的玩耍" % (self.name, dog.name))

        dog.game()


wangcai = Dog('旺财')
feitian = XiaoTianDog("啸天旺财")

xiaoming = Person("小明")

xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(feitian)
