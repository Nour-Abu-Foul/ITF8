import random

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(random.randint(1, 99999))
        self.course_name = course_name
        self.course_mark = course_mark

    def __str__(self):
        return f"Course ID: {self.course_id}\nCourse Name: {self.course_name}\nCourse Mark: {self.course_mark}"

class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_name = student_name
        self.student_age = student_age
        self.student_id = self.generate_student_id()
        self.student_number = student_number
        self.courses_list = []

        Student.total_students += 1

    def generate_student_id(self):
        return random.randint(1000, 9999)

    def __str__(self):
        courses_info = "\n".join([str(course) for course in self.courses_list])
        return f"Student ID: {self.student_id}\nStudent Name: {self.student_name}\nStudent Age: {self.student_age}\nStudent Number: {self.student_number}\nCourses:\n{courses_info}"

    def get_student_details(self):
        courses_info = "\n".join([f"Course Name: {course.course_name}, Course Mark: {course.course_mark}" for course in self.courses_list])
        student_details = {
            "Student ID": self.student_id,
            "Student Name": self.student_name,
            "Student Age": self.student_age,
            "Student Number": self.student_number,
            "Courses": courses_info
        }
        return student_details

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0

students_list = []

while True:
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        student_age = int(input("Enter Student Age: "))
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
                student.courses_list.append(new_course)
                print("Course Added Successfully")
                break
        else:
            print("Student Not Exist")
    else:
        print("Exiting the program.")
        break