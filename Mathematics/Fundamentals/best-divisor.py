#!/bin/python3

import math
import os
import random
import re
import sys

digitSum = lambda num: sum([int(d) for d in list(str(num))])


if __name__ == '__main__':
    n = int(input())
    D = []
    for num in range(1,n+1):
        if n % num == 0:
            D.append(num)

    print(max(D, key= lambda x : digitSum(x)))
