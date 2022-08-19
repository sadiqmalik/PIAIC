print("*********** Students Database ***********")

courses_list = ('AIC', 'IOT', 'Web 3.0', 'Blockchain')
students = []

def registerCourses():
    courses = []

    for course in courses_list:
        if (input(f'Do you want to register in {course}? y/n: ') == 'y'):
            courses.append(course)
    
    return courses

def registerStudent():
    student_record = {}
    student_record['Name'] = input("Enter student name: ")
    student_record['Age'] = input("Enter student age: ")
    student_record['Email'] = input("Enter student email: ")
    student_record['Phone'] = input("Enter student telephone: ")
    student_record['Courses'] = registerCourses()

    students.append(student_record)

def printStudentRecord():
    for student in students:
        for key, value in student.items():
            print(f'{key} : {value}')
        
        print("")

while True:
    registerStudent()
    choice = str(input("\nWant to add another student data? y/n: "))
    
    if (choice == 'y'):
        continue;
    
    printStudentRecord()
    break;
