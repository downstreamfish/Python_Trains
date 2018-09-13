x = input('输入x的值: ')
y = input('输入y的值: ')
'''
tmp = x
x = y
y = tmp
'''
x, y = y, x

print('交换后 x 的值为:{0}'.format(x))
print('交换后 y 的值为:{0}'.format(y))
