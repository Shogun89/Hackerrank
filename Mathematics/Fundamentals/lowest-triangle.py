#!/bin/python3

import sys
import math

def lowestTriangle(base, area):
    
    height = math.ceil(2*area/base)
    return height
base, area = list(map(int,input().strip().split(' ')))
height = lowestTriangle(base, area)
print(height)
