# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A,B = [list(map(int, input().split())) for i in range(2)]

print(*product(A,B))
