#使用递归的方式实现斐波那契数列
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input('你要输出几项?'))
if nterms < 0:
    print('请输入正数.')
else:
    print('斐波那契数列: ')
    for i in range(1, nterms):
        print(recur_fibo(i), end=' ')
    print()
