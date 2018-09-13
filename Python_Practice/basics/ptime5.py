import time
class Timer:
    __begin = 0
    __end = 0
    def __init__(self):
        self.__begin = time.time()
        print('计时开始...')

    def stop_timer(self):
        self.__end = time.time()
        print('计时结束!')

    def __str__(self):
        return '我运行了%d秒'% (self.__end - self.__begin)

t = Timer()
t.stop_timer()
print(t)

