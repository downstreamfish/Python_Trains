#函数的全局变量与函数文档
def myfunc(price, rate):
    '计算打折后商品的价格'
    new_price = price * rate
    print("折扣前的价格是：", old_price)
    return new_price
old_price = int(input('请输入原价：'))
rate = float(input("请输入折扣："))
new_price = myfunc(old_price, rate)
print('折扣后的价格是：', new_price)
