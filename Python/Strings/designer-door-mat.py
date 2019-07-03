

N, M = map(int, input().split())

pattern = [('.|.'*(2*i+1)).center(M,'-') for i in range(N//2)]
result = '\n'.join(pattern + ['WELCOME'.center(M,'-')] + pattern[::-1])
print(result)

