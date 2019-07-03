import numpy as np

result = list(map(int,input().split()))
result = np.array(result)

print(np.reshape(result,(3,3)))



