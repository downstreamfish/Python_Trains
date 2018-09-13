try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除 0 错误")
except Exception as error:
    print("未知错误 %s" % error)
else:
    print("正常执行")
finally:
    print("执行完成，但是不保证没有异常")
