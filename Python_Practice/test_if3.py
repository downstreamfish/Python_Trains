import random as r

player = int(input("请出拳 石头(1) 剪刀(2) 布(3): "))
computer = r.randint(1,3)

if ((player == 1 and computer == 2) or
    (player == 2 and computer == 3) or
    (player == 3 and computer == 1)):
    print("哈哈， 电脑也不过如此嘛！")

elif player == computer:
    print("心有灵犀， 再来一盘")

else:
    print("不行，我要和你决战到天明！")

print(computer)
