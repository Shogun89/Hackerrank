N = int(input())

students = [[input(), float(input())] for i in range(N)]
grades = set([students[i][1] for i in range(N)])
grades = list(grades)
grades.sort()

students = [student[0] for student in students if student[1] == grades[1]]
students.sort()

print("\n".join(map(str, students)))
