#!/bin/python3

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
def bubble_sort(array):
    swap_count = 0
    l = len(array)-1
    for i in range(l, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap_count +=1
    return swap_count

print("Array is sorted in {swap_count} swaps.".format(swap_count = bubble_sort(a)))
print("First Element: {first}".format(first = a[0]))
print("Last Element: {last}".format(last = a[-1]))

