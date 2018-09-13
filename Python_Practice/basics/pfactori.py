'''
num = int(input('输入一个数字: '))
factorial = 1
if num < 0:
    print('抱歉,负数没有阶乘')
elif num == 0:
    print('0的阶乘为 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print('{0}的阶乘为 {1}'.format(num, factorial))
'''

def factorial(n):
    if n <= 1:
        factor = 1
    else:
        factor = n * factorial(n - 1)

    return factor
num = int(input('输入一个数字: '))
print('{0} 的阶乘是: {1}'.format(num, factorial(num)))
