# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split(" "))
grades = [map(float, input().split()) for _ in range(X)]
print_avg = lambda grades:  print(sum(grades)/len(grades)) 
[ print_avg(student) for student in zip(*grades)]
