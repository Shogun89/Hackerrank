# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b,m = [int(input()) for i in range(3)]

print('\n'.join(map(str, [pow(a,b),pow(a,b,m)])))