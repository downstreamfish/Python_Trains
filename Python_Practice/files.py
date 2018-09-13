fo = open('test.dat', 'r+')
name = fo.name
print('文件名:', name)
'''
no = fo.fileno()
print('文件no:',no)
line = fo.read()
print('读取的字符为：', line)
line = fo.readline()
print('第一行为:', line)
for i in range(5):
   line = next(fo)
   print('第 %d 行-%s' % (i, line))
while next(fo) != EOF:
   line = next(fo)
   print(line)
for line in fo.readlines():
   line = line.strip()
   print('读取的数据为：',line)
line = fo.readline()
print('第一次:', line)
pos = fo.tell()
fo.seek(0,0)
print('当前位置:',pos)
line2 = fo.readline()
print('第二次:', line2)
'''

str1 = '湖北集安堂药业'
fo.seek(0,2)
fo.write(str1)
fo.flush()
fo.seek(0,0)
for line in fo.readlines():
   line = line.strip()
   print(line)
fo.close()
