
"""ITF 08 Final Project
# Enter your name and submission date
Name : Nour Abu Foul
Delivery Date :
Eng.Mohanad Alkrunz
"""
import random


#  Define Course Class and define constructor with (course_id generated ,course name (user_input) and
# course mark
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(random.Random.randint())
        self.course_name = course_name
        self.course_mark = course_mark

        def __str__(self):
            return f"Course ID: {self.course_id}\nCourse Name: {self.course_name}\nCourse Mark: {self.course_mark}"
    course_name = input("Enter the course name: ")
    course_mark = float(input("Enter the course mark: "))


class Student:
    #  define static variable indicates total student count
    total_students = 0

    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age
        Student.total_students += 1

    #  define a constructor which includes
    def student_information(self, student_name, student_age, student_number, courses_list=[]):
        self.student_id = self.generate_student_id()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list
    # student_id (unique using random module)
    import random
    student_id = random.random
    # student_name (user input)
    student_name = input("Inter Your Name: ")
    # student_age (user_inout)
    student_age = int(input("Inter Your Age: "))
    # student_number (user_input)
    student_number = int(input("Inter Your Number: "))
    # courses_list (List of Course Objects)
    def __str__(self):
        courses_info = "\n".join([str(course) for course in self.courses_list])
        return f"Student ID: {self.student_id}\nStudent Name: {self.student_name}\nStudent Age: {self.student_age}\nStudent Number: {self.student_number}\nCourses:\n{courses_info}"

    def __init__(self):
        pass

    #  define a method to enroll new course to student courses list
    # method to get_student_details as dict
    def get_student_details(self):
        courses_info = [{"Course Name": course.course_name, "Course Mark": course.course_mark} for course in self.courses_list]
        student_details = {
            "Student ID": self.student_id,
            "Student Name": self.student_name,
            "Student Age": self.student_age,
            "Student Number": self.student_number,
            "Courses": courses_info
        }
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # print student courses with their marks
        return [{"Course Name": course.course_name, "Course Mark": course.course_mark} for course in self.courses_list]
        pass

    # method to get student_average as a value
    def get_student_average(self):
        # return the student average
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0


# in Global Scope
#  declare empty students list
students_list = []
while True:

    # handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))

    if selection == 1:
        student_number = input("Enter Student Number")
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        #  create student object and append it to students list
        student = [student_number,student_name,student_age]
        students_list.append(student)
        print("Student Added Successfully")
    elif selection == 2:
        student_number = input("Enter Student Number")
        if student.student_number == student_number:
            students_list.remove(student)
            print("Student Deleted Successfully")
            break
        else:
            print("Student Not Exist")
        #  find the target student using loops and delete it if exist , if not print ("Student Not Exist")
    elif selection == 3:
        student_number = input("Enter Student Number")
        # find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
        for student in students_list:
            if student.student_number == student_number:
                print(student.get_student_details())
                break
        else:
            print("Student Not Exist")
    elif selection == 4:
        student_number = input("Enter Student Number")
        #  find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
        for student in students_list:
            if student.student_number == student_number:
                print(f"Student Average: {student.get_student_average()}")
                break
        else:
                print("Student Not Exist")
    elif selection == 5:
        student_number = input("Enter Student Number")
        #  ask user to enter course name and course mark then create coures object then append it to target student courses
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
    #  call a function to exit the program
    else:
        print("Exiting the program.")
        break

