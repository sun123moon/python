#write a program to display the sin(x) value where x ranges from o to 360 in steps of 15
print("sine values")
import math
from fractions import Fraction
for x in range(0,360+1,15):
    m = x
    y = x/180*math.pi
    x = math.sin(y)
    x = Fraction(x)
    x = x.limit_denominator(10)
    print("sin of",m,"=",x)
