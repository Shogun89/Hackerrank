# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b = int(input()), int(input())

print('\n'.join(map(str, [ a//b, a% b, divmod(a,b)])))