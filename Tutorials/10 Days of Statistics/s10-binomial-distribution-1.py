import math

ratio = 1.09

p = ratio / (1 + ratio)
C = lambda n, k: math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
P = sum([C(6, i) * pow(p, i) * pow(1-p, 6-i) for i in range(3,7)])

print('{:.3f}'.format(P))
