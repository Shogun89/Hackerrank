import numpy as np
np.set_printoptions(sign=' ')

nums = np.array(input().split(),float)

print(np.floor(nums))
print(np.ceil(nums))
print(np.rint(nums))