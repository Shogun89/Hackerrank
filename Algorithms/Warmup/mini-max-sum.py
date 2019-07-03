#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    my_sums = []
    my_len = len(arr)
    for i in range(my_len):
        arr_minus_1 = [x for j,x in enumerate(arr) if  j != i]
        this_sum = sum(arr_minus_1)
        my_sums.append(this_sum)

    my_max = max(my_sums)
    my_min = min(my_sums)
    minmaxarr = [my_min, my_max]
    return minmaxarr



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(" ".join(map(str, miniMaxSum(arr))))
