#! /usr/local/bin/python3

demo_list = [1, 2, 3]

print(demo_list)
print("定义后列表的内存地址 %d" % id(demo_list))

demo_list.append(999)
demo_list.pop(0)
demo_list.remove(2)
demo_list[0] = 10

print(demo_list)
print("修改数据后的内存地址 %d" % id(demo_list))

demo_dict = {'name': '小明'}

print(demo_dict)
print("定义字典后的内存地址 %d" % id(demo_dict))

demo_dict['age'] = 18
demo_dict.pop('name')
demo_dict['name'] = '老王'

print(demo_dict)
print("修改数据后的内存地址 %d" % id(demo_dict))
