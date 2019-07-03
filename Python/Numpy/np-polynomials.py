import numpy as np
coeff = np.array(input().split(" "),float)
x_val = int(input())
print(np.polyval(coeff, x_val))
