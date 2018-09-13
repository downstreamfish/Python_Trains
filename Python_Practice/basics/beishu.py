# 求最小公倍数
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcmer = greater
            break
        greater += 1

    return lcmer
num1 = int(input("输入第一个数字: "))
num2 = int(input('输入第二个数字: '))

print('{0} 和 {1} 的最小公倍数是: {2}'.format(num1, num2, lcm(num1, num2)))
