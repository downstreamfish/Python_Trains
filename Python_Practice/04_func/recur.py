#! /usr/local/bin/python3


def sum_numbers(num):
    if num == 1:
        return 1

    # 假设sum_numbers 能够完成num-1的累加
    temp = sum_numbers(num - 1)

    # 函数内部的核心算法就是 两个数字的相加
    return num + temp


print(sum_numbers(10))
