''' 使用类属性来记录创建对象的个数
'''


class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        ''' 显示工具对象的总数 '''
        print("工具对象的总数 %d" % cls.count)


# 创建对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("鉄楸")

# 打印使用Tool类创建了多少个对象
print("现在创建了 %d 个工具" % Tool.count)
Tool.show_tool_count()
