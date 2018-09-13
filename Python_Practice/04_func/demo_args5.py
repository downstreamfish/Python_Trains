#! /usr/local/bin/pyhton3


def print_info(name, title='', gender=True):
    """

    : param title:职位
    : param name: 姓名
    : param gender: True 男生 False 女生
    """
    gender_txt = "男生"

    if not gender:
        gender_txt = "女生"

    print("%s%s 是 %s" % (title, name, gender_txt))


# 提示: 在指定缺省参数的默认值时, 应该使用最常见的值作为默认值
print_info("小明")
print_info("老王", title="班长")
print_info("小美", gender=False)
