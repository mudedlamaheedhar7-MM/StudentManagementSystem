from services.attendance_service import AttendanceService


class AttendanceController:

    # ------------------------------------------
    # CREATE ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def save_attendance(attendance):
        return AttendanceService.create_attendance(attendance)

    # ------------------------------------------
    # GET ALL ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def get_all_attendance():
        return AttendanceService.get_all_attendance()

    # ------------------------------------------
    # GET ATTENDANCE BY ID
    # ------------------------------------------

    @staticmethod
    def get_attendance_by_id(attendance_id):
        return AttendanceService.get_attendance_by_id(attendance_id)

    # ------------------------------------------
    # GET ATTENDANCE BY DATE
    # ------------------------------------------

    @staticmethod
    def get_attendance_by_date(date):
        return AttendanceService.get_attendance_by_date(date)

    # ------------------------------------------
    # UPDATE ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def update_attendance(attendance):
        return AttendanceService.update_attendance(attendance)

    # ------------------------------------------
    # DELETE ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def delete_attendance(attendance_id):
        return AttendanceService.delete_attendance(attendance_id)

    # ------------------------------------------
    # SEARCH ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def search_attendance(keyword):
        return AttendanceService.search_attendance(keyword)

    # ------------------------------------------
    # GENERATE ATTENDANCE ID
    # ------------------------------------------

    @staticmethod
    def generate_attendance_id():
        return AttendanceService.generate_attendance_id()