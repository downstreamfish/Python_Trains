#实现简单的计算器,包括两个基本的加减乘除运算
def madd(x, y):
    return x + y

def msubtract(x, y):
    return x - y

def mmultiply(x, y):
    return x * y

def mdivide(x, y):
    if y == 0:
        return "被除数不能为零"
    else:
        return x / y

print('选择运算: ')
print('加法: 1')
print('减法: 2')
print("乘法: 3")
print("除法: 4")

choice = input('输入你的选择(1/2/3/4): ')
num1 = float(input("输入第一个数字: "))
num2 = float(input("输入第二个数字: "))

if choice == '1':
    print(num1, " + ", num2, ' = ', madd(num1, num2))
elif choice == '2':
    print(num1, ' - ', num2, ' = ', msubtract(num1, num2))
elif choice == '3':
    print(num1, " * ", num2, ' = ', mmultiply(num1, num2))
elif choice == '4':
    print(num1, ' / ', num2, ' = ', mdivide(num1, num2))
else:
    print("非法输入")
