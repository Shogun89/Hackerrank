# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby 


print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


