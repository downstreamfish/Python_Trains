fo = open('cainiao.txt', 'w')
print('文件名:',fo.name)

seq = ['菜鸟教程1\n','菜鸟教程2']
fo.writelines(seq)
fo.flush()
fo.close()
