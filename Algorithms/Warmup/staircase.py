#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
   
    for i in range(n):
        res = ' '*(n-i-1) + ('#')*(i+1)
        print(res)
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
