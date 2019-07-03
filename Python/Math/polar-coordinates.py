# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath 
z = complex(input())
print('\n'.join(map(str,[abs(z),cmath.phase(z)])))
