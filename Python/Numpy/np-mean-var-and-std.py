import numpy as np
n, _ = map(int, input().split())
np.set_printoptions(legacy='1.13')
arr =np.array([input().split() for _ in range(n)], int)
print('\n'.join(map(str, [np.mean(arr, axis=1), np.var(arr, axis=0), np.std(arr, axis=None)])))
