# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mu = float(input())
x = int(input())
def poisson_pdf(mu,x):

    p = math.exp(-mu) * (mu**x) / math.factorial(x)
    return p

print("{0:.3f}".format(poisson_pdf(mu,x)))