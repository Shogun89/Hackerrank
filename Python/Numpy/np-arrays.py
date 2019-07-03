import numpy

def arrays(arr):
    result = numpy.array(list(map(float, arr)))
    result = result[::-1]
    return result
arr = input().strip().split(' ')
result = arrays(arr)
print(result)