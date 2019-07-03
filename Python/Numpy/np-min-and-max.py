import numpy as np

n, _ = map(int, input().split())
print(np.max(np.min(np.array([input().split() for _ in range(n)], int), axis=1), axis=None))
