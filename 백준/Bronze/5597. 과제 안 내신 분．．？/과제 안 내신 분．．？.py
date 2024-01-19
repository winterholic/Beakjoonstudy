students = {}

for i in range(1, 31) :
    students[i] = 0

for i in range(28) :
    stu = int(input())
    students[stu] = 1

for i in range(1, 31) :
    if(students[i] == 0) :
        print(i)