def c2f(temp):
   return temp * 1.8 + 32

def f2c(temp):
   return (temp - 32) / 1.8

def test():
   print('摄氏0度转华氏温度是：{0:.2f}'.format(c2f(0)))
   print('华氏0度转摄氏温度是：{0:.2f}'.format(f2c(0)))

if __name__=='__main__':
   test()
