if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    s_scores = student_marks[query_name];
    avg = sum(s_scores)/len(s_scores);
    print("{:.2f}".format(avg))