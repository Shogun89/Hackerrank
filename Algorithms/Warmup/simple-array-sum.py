import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):


    my_sum = sum(ar)

    return my_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
