has_ticket = True
knife_length = 20

if has_ticket:
    print("有车票，可以开始安检……")

    if knife_length >= 20:
        print("不允许携带{0}厘米长的刀上车。".format(knife_length))
    else:
        print("安检通过，祝你旅途愉快……")

else:
    print("请先购买车票！")
