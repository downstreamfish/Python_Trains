class Turtle:
    def __init__(self, cnt):
        self.num = cnt

class Fish:
    def __init__(self, cnt):
        self.num = cnt

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print('水池里面总共有乌龟%d只,小鱼%d条.' % (self.turtle.num, self.fish.num))

pool = Pool(1, 10)
pool.print_num()
