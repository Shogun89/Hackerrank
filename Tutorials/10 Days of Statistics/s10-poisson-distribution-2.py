mu_X, mu_Y = [float(num) for num in input().split()]

def get_cost(a,b, mu):
    cost = a+b*(mu+mu**2)
    return cost
print("{0:.3f}".format(get_cost(160, 40, mu_X)))
print("{0:.3f}".format(get_cost(128, 40, mu_Y)))
