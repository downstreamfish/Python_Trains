# 检测用户输入的组织是否为阿姆斯特丹数
# 如果一个n为正整数等于其各位数字的n次方之和,则称该数为阿姆斯特丹数

num= int(input("输入一个数字: "))
sum = 0
n = len(str(num))

tmp = num
while tmp > 0:
    digit = tmp % 10
    sum += digit ** n
    tmp //= 10

if num == sum:
    print(num, "是阿姆斯特丹数.")
else:
    print(num, "不是阿姆斯特丹数.")
