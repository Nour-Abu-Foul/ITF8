import random
import string
import uuid


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark

    def __str__(self):
        return f"Course ID: {self.course_id}\nCourse Name: {self.course_name}\nCourse Mark: {self.course_mark}"


class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number, courses_list=[]):
        self.student_id = self.generate_student_id()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list
        Student.total_students += 1

    def generate_student_id(self):
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return f'ST-{random_chars}'

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        return [{"Course Name": course.course_name, "Course Mark": course.course_mark} for course in self.courses_list]

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0


students_list = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Value")
                continue

        student = Student(student_name, student_age, student_number)
        students_list.append(student)
        print("Student Added Successfully")
    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                students_list.remove(student)
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")
    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                print(student.get_student_details())
                break
        else:
            print("Student Not Exist")
    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                print(f"Student Average: {student.get_student_average()}")
                break
        else:
            print("Student Not Exist")
    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                new_course = Course(course_name, course_mark)
                student.enroll_course(new_course)
                print("Course Added Successfully")
                break
        else:
            print("Student Not Exist")
    else:
        print("Exiting the program.")
        break

