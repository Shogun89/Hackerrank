# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = set(input().split())
b = int(input())
Y = set(input().split())

print(len(X.union(Y)))