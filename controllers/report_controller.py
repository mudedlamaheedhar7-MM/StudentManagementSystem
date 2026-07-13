from services.report_service import ReportService


class ReportController:

    # ==================================================
    # Dashboard Summary
    # ==================================================

    @staticmethod
    def get_dashboard_summary():
        return ReportService.get_dashboard_summary()

    # ==================================================
    # Attendance Summary
    # ==================================================

    @staticmethod
    def get_attendance_summary():
        return ReportService.get_attendance_summary()

    # ==================================================
    # Fee Summary
    # ==================================================

    @staticmethod
    def get_fee_summary():
        return ReportService.get_fee_summary()

    # ==================================================
    # Students by Department
    # ==================================================

    @staticmethod
    def get_students_by_department():
        return ReportService.get_students_by_department()

    # ==================================================
    # Courses by Department
    # ==================================================

    @staticmethod
    def get_courses_by_department():
        return ReportService.get_courses_by_department()