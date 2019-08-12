"""
def factorial(n):
    result=1
    for num in range(1,n+1):
        result*=num
    return result
print(factorial(7)//factorial(3)//factorial(4))
"""
"""
from random import randint
def roll(n=2):
    total=0
    for i in range(n):
        total+=randint(1,6)
    return total
def add(a=0,b=0,c=0):
    return a+b+c
print(roll())
print(roll(3))
"""
"""
def add(*num):
    result=1
    for i in num:
        result+=i
    return result
print(add())
print(add(1))
print(add(1,2,3,4))
"""

import module1 as m1
import module2 as m2
import module3 as m3
m1.care()
m2.hello()
m3.bar()

#////////def練習/////////
"""
def gcd(x,y):
    if x>y:
        x,y=y,x
    for factor in range(x,1,-1):
        if x%factor==0 and y%factor==0:
            return factor
def lcm(x,y):
    return x*y//gcd(x,y)
print(gcd(15,27))
print(lcm(15,27))
"""


