students = []
name_of_se = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

all_score = []

for value in students:
    if value[1] not in all_score:
        all_score.append(value[1])
        all_score.sort()
    else:
        all_score = all_score

for value in students:
    if value[1] == all_score[1] :
        name_of_se.append(value[0])
        name_of_se.sort()
    else:
        name_of_se = name_of_se
for i in name_of_se:
    print(i)