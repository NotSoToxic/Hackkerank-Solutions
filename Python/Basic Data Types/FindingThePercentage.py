n = int(input())
global student_marks
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

def average_student(query_name):
    for clave,valor in student_marks.items():
        if clave==query_name:
            print("{:.2f}".format(sum(valor)/len(valor)))
average_student(query_name)