#求二次方程的解 ax^2 + bx + c = 0
import cmath
a = float(input('输入a: '))
b = float(input('输入b: '))
c = float(input('输入c: '))
d = (b**2) - 4*a*c
sol1 = (-b - cmath.sqrt(d))/(2*a)
sol2 = (-b + cmath.sqrt(d))/(2*a)

print("方程{0}x^2 + {1}x + {2} = 0的解为: {3} 和 {4}".format(a, b, c, sol1, sol2))
