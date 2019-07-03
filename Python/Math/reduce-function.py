from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y  : x*y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':