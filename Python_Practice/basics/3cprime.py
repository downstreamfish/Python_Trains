num = int(input('输入一个数字: '))
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print(num, '不是素数')
            print(i, ' x ', num // i, ' = ', num)
            break

    else:
        print(num, '是素数')

else:
    print(num, '不是质数')
