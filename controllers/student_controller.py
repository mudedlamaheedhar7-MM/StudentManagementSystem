from services.student_service import StudentService


class StudentController:

    @staticmethod
    def save_student(student):

        return StudentService.create_student(
            student
        )