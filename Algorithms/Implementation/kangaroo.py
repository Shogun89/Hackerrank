#!/bin/python3
import os
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    if(v1<v2):
        return "NO"
    else:
        
        if( (v1!=v2) and (x2-x1)%(v1-v2) ==0 ):
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1, v1, x2, v2 = list(map(int, input().split() ))

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
