#!/bin/python3

import os
import sys
import math

#
# Complete the handshake function below.
#
def handshake(n):
    num_shakes = math.floor((n*(n-1))/2)
    return num_shakes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
