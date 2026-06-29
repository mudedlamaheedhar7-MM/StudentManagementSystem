from models.student import Student
from controllers.student_controller import StudentController


student = Student(
    student_id="SMS0001",
    admission_no="ADM2026001",

    first_name="Maheedhar",
    last_name="Mudedla",

    gender="Male",

    dob="1999-01-01",

    phone="9876543210",
    email="mahee@example.com",

    address="Visakhapatnam",

    course="BBA",
    department="HR",

    semester=1,
    batch="2026"
)

saved = StudentController.save_student(
    student
)

print("Student Saved:", saved)