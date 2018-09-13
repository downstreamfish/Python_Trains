from ctypes import *

adder = CDLL('./adder.so')

res_int = adder.add_int(4, 6)
print("sum of 4 and 6 = " + str(res_int))

a = c_float(5.5)
b = c_float(3.9)

add_float = adder.add_float

add_float.restype = c_float
print("sum of 5.5 and 3.9 = " + str(add_float(a,b)))
