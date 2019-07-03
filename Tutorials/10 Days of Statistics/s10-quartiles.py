# Enter your code here. Read input from STDIN. Print output to STDOUT


def find_median(arr,start, stop):

    median = 0
    n = stop-start+1
    m = start+n//2
    if (n % 2 == 0):
        median = (arr[m]+arr[m-1])/2
    else:
        median = arr[m]
    recasted_median = int(median)
    return recasted_median

def find_quartiles(nums):
    sorted_nums = sorted(nums)
    n = len(nums)
    Q2 = find_median(sorted_nums,0,(n-1))
    m = n//2

    if (n % 2 == 0):
        Q1 = find_median(sorted_nums,0, m-1)
        Q3 = find_median(sorted_nums, m, n-1)
    else:
        Q1 = find_median(sorted_nums,0, m-1)
        Q3 = find_median(sorted_nums, m+1, n-1)

    return Q1, Q2, Q3


n = int(input())
X = [int(item) for item in input().split()]

Q1,Q2,Q3 = find_quartiles(X)

print(Q1)
print(Q2)
print(Q3)
