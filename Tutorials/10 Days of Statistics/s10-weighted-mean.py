# Enter your code here. Read input from STDIN. Print output to STDOUT

def weighted_mean(X, W,n):

    weighted_mean = 0
    for i in range(n):
        weighted_mean += X[i]*W[i]
    weighted_sum = sum(W)

    weighted_mean = weighted_mean/weighted_sum
    return round(weighted_mean,1)

n = int(input())
X = [int(item) for item in input().split()]
W = [int(item) for item in input().split()]


print(weighted_mean(X,W,n))
