#递归函数
def rec(n):
    if n <= 1:
        return 1
    else:
        return n * rec(n-1)

m = rec(5)
print('5的阶乘是：', m)
