#! /usr/local/bin/python3


def demo(num, num_list):

    print("函数内部代码")

    # num = num + num
    num += num

    # num_list.extend(num_list)由于是调用方法, 所有不会改变变量的引用
    # 函数执行结束后, 外部数据同样会发生变化
    num_list += num_list

    print(num)
    print(num_list)

    print("函数代码完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
