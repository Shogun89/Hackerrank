k,arr = int(input()),list(map(int, input().split()))
result = (k*sum(set(arr)) - sum(arr))//(k-1)
print(result)

