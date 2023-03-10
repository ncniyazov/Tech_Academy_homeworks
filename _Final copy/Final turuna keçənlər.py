n = abs(int(input()))
#marks_inform = ["A", "B", "C", "D", "E", "F"]
marks_inform = ["A", "B"]
for i in range(n):
    student_result  = input().split(" ")
    gpa = float(student_result[0])
    mark = student_result[1]
    if gpa >= 3.5 and mark in marks_inform:
        print(1)
    else:
        print(0)