#! /usr/local/bin/python3


def mutable(num_list):

    # num_list = [1, 2, 3]
    num_list.extend([1, 2, 3])

    print(num_list)


gl_list = [5, 6, 7]

mutable(gl_list)

print(gl_list)
