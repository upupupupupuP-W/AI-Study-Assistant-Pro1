1.
import calculator

print(calculator.add(10,5))
print(calculator.sub(10,5))
print(calculator.mul(10,5))
print(calculator.div(10,5))

2.
from calculator import add
print(add(100,200))

3.
from calculator import *
print(add(100,200))

from calculator import *
a=float(input("第一个数字是："))
b=float(input("第二个数字是："))

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))