# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    (command, newSet) = (input().split()[0],set(map(int, input().split())))
    getattr(A, command)(newSet)

print(sum(A))
    

