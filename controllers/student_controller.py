from services.student_service import StudentService


class StudentController:

    # --------------------------------------------------
    # CREATE STUDENT
    # --------------------------------------------------

    @staticmethod
    def save_student(student):
        return StudentService.create_student(student)

    # --------------------------------------------------
    # GET ALL STUDENTS
    # --------------------------------------------------

    @staticmethod
    def get_all_students():
        return StudentService.get_all_students()

    # --------------------------------------------------
    # SEARCH STUDENTS
    # --------------------------------------------------

    @staticmethod
    def search_students(keyword):
        return StudentService.search_students(keyword)

    # --------------------------------------------------
    # GET STUDENT BY ID
    # --------------------------------------------------

    @staticmethod
    def get_student_by_id(student_id):
        return StudentService.get_student_by_id(student_id)

    # --------------------------------------------------
    # UPDATE STUDENT
    # --------------------------------------------------

    @staticmethod
    def update_student(student):
        return StudentService.update_student(student)

    # --------------------------------------------------
    # DELETE STUDENT
    # --------------------------------------------------

    @staticmethod
    def delete_student(student_id):
        return StudentService.delete_student(student_id)

    # --------------------------------------------------
    # GENERATE STUDENT ID
    # --------------------------------------------------

    @staticmethod
    def generate_student_id():
        return StudentService.generate_student_id()