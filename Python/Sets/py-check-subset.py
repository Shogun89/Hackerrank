# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))