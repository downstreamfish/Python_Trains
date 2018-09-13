#斐波那契数列

def fabi1(n):
    result = 1
    previous = 0
    courrent = 1
    for i in range(1, n, 1):
        result = previous + courrent
        previous = courrent
        courrent = result
    return courrent

'''
def fab2(x):
    result = 0
    if x==1 or x == 2:
        result = 1
    else:
        result = fab2(x-1) + fab2(x-2)
    return result
'''
n = int(input('Enter a number:'))
m = fabi1(n)
print(m)
