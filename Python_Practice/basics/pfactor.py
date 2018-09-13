# 计算一个数最大的约数,如果是素数,就返回它
def showmaxfact(num):
    cnt = num // 2
    while cnt > 1:
        if(num % cnt == 0):
            print("%d最大的约数是: %d"%(num, cnt))
            break
        cnt -= 1
    else:
        print("%d 是素数"% num)

num = int(input('请输入一个数:'))
showmaxfact(num)
