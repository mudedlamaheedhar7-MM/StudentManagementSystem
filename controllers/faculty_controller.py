from services.faculty_service import FacultyService


class FacultyController:

    # ------------------------------------------
    # CREATE FACULTY
    # ------------------------------------------

    @staticmethod
    def save_faculty(faculty):
        return FacultyService.create_faculty(faculty)

    # ------------------------------------------
    # GET ALL FACULTY
    # ------------------------------------------

    @staticmethod
    def get_all_faculty():
        return FacultyService.get_all_faculty()

    # ------------------------------------------
    # SEARCH FACULTY
    # ------------------------------------------

    @staticmethod
    def search_faculty(keyword):
        return FacultyService.search_faculty(keyword)

    # ------------------------------------------
    # GET FACULTY BY ID
    # ------------------------------------------

    @staticmethod
    def get_faculty_by_id(faculty_id):
        return FacultyService.get_faculty_by_id(faculty_id)

    # ------------------------------------------
    # UPDATE FACULTY
    # ------------------------------------------

    @staticmethod
    def update_faculty(faculty):
        return FacultyService.update_faculty(faculty)

    # ------------------------------------------
    # DELETE FACULTY
    # ------------------------------------------

    @staticmethod
    def delete_faculty(faculty_id):
        return FacultyService.delete_faculty(faculty_id)

    # ------------------------------------------
    # GENERATE FACULTY ID
    # ------------------------------------------

    @staticmethod
    def generate_faculty_id():
        return FacultyService.generate_faculty_id()

    # ------------------------------------------
    # GENERATE EMPLOYEE ID
    # ------------------------------------------

    @staticmethod
    def generate_employee_id():
        return FacultyService.generate_employee_id()