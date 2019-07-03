import numpy as np

N,M,_ = list(map(int, input().split()))

print(np.array([input().split() for _ in range(N+M)] ,int))
