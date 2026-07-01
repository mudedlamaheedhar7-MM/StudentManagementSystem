from services.student_service import StudentService


class StudentController:

    @staticmethod
    def save_student(student):
        return StudentService.create_student(student)

    @staticmethod
    def get_all_students():
        return StudentService.get_all_students()

    @staticmethod
    def generate_student_id():
        return StudentService.generate_student_id()