#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    diff = list(map(lambda i,j : i-j, a,b))
    alice_pts = len(list(filter(lambda x :  x >0 , diff)))
    bob_pts = len(list(filter(lambda x: x < 0, diff)))
    pts_array = [alice_pts, bob_pts]
    return pts_array
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
