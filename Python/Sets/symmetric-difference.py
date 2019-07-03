# Enter your code here. Read input from STDIN. Print output to STDOUT

M_num = int(input())
M = set(map(int, input().split()))
N_num = int(input())
N = set(map(int, input().split()))

sym_N = list(map(int,M.difference(N))) 
sym_M = list(map(int, N.difference(M)))

diff = sorted(sym_N+sym_M)
print('\n'.join(map(str, diff)))