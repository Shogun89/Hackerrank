# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
prob, trials = list(map(int, input().split()))
p = prob/100

C = lambda n, k: math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
cdf = lambda n, p, a,b : sum([C(n, x) * pow(p, x) * pow(1-p, n-x) for x in range(a,b)])
print('{:.3f}'.format(cdf(trials, p, 0,3)))
print('{:.3f}'.format(cdf(trials, p, 2,trials+1)))
