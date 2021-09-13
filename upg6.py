# 6. Write a Python function to find the greatest common divisor (gcd) of two integers.

import math


def gcd_calculator(x, y):
    """As the math.lib is in Python, this is the easiest way to find the gcd, by simply using
    the builtin function math.gcd, and give it the two arguments.
    """
    return math.gcd(x, y)


print(gcd_calculator(10, 20))





