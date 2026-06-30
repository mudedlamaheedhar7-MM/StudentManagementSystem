from controllers.student_controller import StudentController

students = StudentController.get_all_students()

print("Total Students:", len(students))

for student in students:
    print(student)