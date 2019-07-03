# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

num_shoes = int(input())
shoe_sizes = collections.Counter(map(int, input().split()))
profit = 0

num_customer = int(input())

for _ in range(num_customer):
    size, price = map(int, input().split())
    if shoe_sizes[size] >0:
        profit += price
        shoe_sizes[size] -=1
    
print(profit)
