#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    d1 =0
    d2 =0 
    n = len(arr)
    for i in range(0,n):
        d1 += arr[i][i]
        d2 += arr[i][n-i-1]
    my_max = max(abs(d1-d2),abs(d2-d1))
    return my_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
