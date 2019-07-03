def interquartile_range(X,F,n):
    S = []
    for i in range(n):
        num = X[i]
        freq = F[i]
        for j in range(freq):
            S.append(num)
        
    S = sorted(S)

    Q = find_quartiles(S)
    inter = float(Q[2]-Q[0])
    return inter

def find_median(arr,start, stop):

    n = stop-start+1
    m = start+ n//2
    if (n % 2 == 0):
        return (arr[m]+arr[m-1])/2
    else:
        return arr[m]



def find_quartiles(nums):
    n = len(nums)
    nums = sorted(nums)
    Q2 = find_median(nums,0,(n-1))
    m = n//2

    if (n % 2 == 0):
        Q1 = find_median(nums,0, m-1)
        Q3 = find_median(nums, m, n-1)
    else:
        Q1 = find_median(nums,0, m-1)
        Q3 = find_median(nums, m+1, n-1)

    return Q1, Q2, Q3

n = int(input())
X = [int(item) for item in input().split()]
F = [int(item) for item in input().split()]

print(interquartile_range(X,F,n))

