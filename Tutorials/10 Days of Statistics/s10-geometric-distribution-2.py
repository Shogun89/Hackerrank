numerator , denominator = list(map(int, input().split()))
x = float(input())

p = numerator/denominator
prob = 1-(1-p)**x
print("{0:.3f}".format(prob))

