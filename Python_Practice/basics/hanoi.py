#用递归解汉诺伊塔
def hanoi(n, a, b, c):
    if n == 1:
        print("%s => %s" %(a, c))
    else:
        hanoi(n-1,a,c,b)
        print("%s => %s" %(a, c))
        hanoi(n-1,b,a,c)
m = int(input('Enter a number:'))
hanoi(m, 'A','B','C')
