#!/bin/python3


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    reversed_arr = arr[::-1]

    print(' '.join(map(str, reversed_arr)))
