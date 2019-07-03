# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

s,k = input().split()
s = sorted(s)

print('\n'.join([''.join(i) for i in combinations_with_replacement(s, int(k))]))