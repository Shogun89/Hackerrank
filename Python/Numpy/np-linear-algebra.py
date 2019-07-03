import numpy as np

N = int(input())
A = np.array([input().split(" ") for _ in range(N) ], float)

np.set_printoptions(legacy='1.13')
print(np.linalg.det(A))
