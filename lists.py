students_count = int(input("Inter the Student Count"))
for i in range(0,students_count):
    total = 0
    my_marks = []
    marks_count = int(input("Inter the Mark Count: "))
    for i in range(0,marks_count):
        mark = float(input("Enter your Mark: "))
        my_marks .append(mark)
        total += mark
    average = sum(my_marks) /len(my_marks)
    print("Average: ",average)
    print("Max Mark: ",max(my_marks))
    print("Min Mark: ",min(my_marks))