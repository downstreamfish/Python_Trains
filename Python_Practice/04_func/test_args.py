#! /usr/local/bin/python3


def test(num):

    print('-' * 50)
    print("%d 在函数内的内存地址是 %x" % (num, id(num)))

    result = 100

    print("返回值 %d 在内存中的地址是 %x" % (result, id(result)))

    print('-' * 50)

    return result


a = 10

print("调用函数前a: %d内存地址是 %x" % (a, id(a)))

r = test(a)

print("调用函数后a: %d内存地址是 %x" % (a, id(a)))
print("调用函数后 返回值内存地址是 %x" % (id(r)))
