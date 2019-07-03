
def find_sd(X,n):
    mu = sum(X)/n
    
    s0 = list(map(lambda x:  (x-mu)**2, X))
    sigma = round((sum(s0)/n)**(0.5),1)

    return sigma

n = int(input())
X = [int(item) for item in input().split()]
sigma = find_sd(X,n)
print(sigma)
