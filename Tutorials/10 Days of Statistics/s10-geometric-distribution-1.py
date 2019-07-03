import math
numerator , denominator = list(map(int, input().split()))
x = float(input())

def geom_dist(n,p):

    q = 1.0- p
    prob = p * math.pow(q,n-1)
    return prob


p = numerator/denominator
print("{0:.3f}".format(geom_dist(x,p)))