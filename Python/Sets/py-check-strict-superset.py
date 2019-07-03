# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
t = 0
for _ in range(n):
    otherSet = set(map(int, input().split()))
    if (A.issuperset(otherSet)):
        t +=1
        

if (t == n):
    print("True")
else:
    print("False")
