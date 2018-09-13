#已知三条边的长,求三角形的面积
a = float(input("输入三角形的第一边长: "))
b = float(input("输入三角形的第二边长: "))
c = float(input("输入三角形的第三边长: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**0.5
print('三角形的面积为: {0:.2f}'.format(area))
