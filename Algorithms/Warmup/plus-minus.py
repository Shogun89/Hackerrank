#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    my_len = len(arr)
    positive_num = len(list(filter(lambda x : x > 0, arr)))
    negative_num = len(list(filter(lambda x: x < 0, arr)))
    zero_num = len(list(filter(lambda x: x ==0, arr)))

    pos_ratio =  (positive_num/my_len)
    neg_ratio = (negative_num/my_len)
    zero_ratio = (zero_num/my_len)


    ans_array = [pos_ratio, neg_ratio, zero_ratio]
    ans_array = list(map(float, ans_array))
    ans_array = [ '%.6f' % num for num in ans_array]
    return ans_array

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res =plusMinus(arr)s
    print("\n".join(map(str, res)))
