from database.mongodb import mongodb


class ReportService:

    @staticmethod
    def get_database():

        return mongodb.get_database()

    # ------------------------------------------
    # Dashboard Counts
    # ------------------------------------------

    @staticmethod
    def get_dashboard_summary():

        db = ReportService.get_database()

        return {

            "students": db.students.count_documents({}),

            "faculty": db.faculty.count_documents({}),

            "courses": db.courses.count_documents({}),

            "attendance": db.attendance.count_documents({}),

            "fees": db.fees.count_documents({})
        }

    # ------------------------------------------
    # Attendance Summary
    # ------------------------------------------

    @staticmethod
    def get_attendance_summary():

        db = ReportService.get_database()

        return {

            "present": db.attendance.count_documents(
                {"status": "Present"}
            ),

            "absent": db.attendance.count_documents(
                {"status": "Absent"}
            ),

            "late": db.attendance.count_documents(
                {"status": "Late"}
            )
        }

    # ------------------------------------------
    # Fee Summary
    # ------------------------------------------

    @staticmethod
    def get_fee_summary():

        db = ReportService.get_database()

        return {

            "paid": db.fees.count_documents(
                {"status": "Paid"}
            ),

            "partial": db.fees.count_documents(
                {"status": "Partial"}
            ),

            "pending": db.fees.count_documents(
                {"status": "Pending"}
            )
        }
        # ==================================================
    # Students by Department
    # ==================================================

    @staticmethod
    def get_students_by_department():

        db = ReportService.get_database()

        pipeline = [
            {
                "$group": {
                    "_id": "$department",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]

        result = {}

        for row in db.students.aggregate(pipeline):
            result[row["_id"]] = row["count"]

        return result

    # ==================================================
    # Courses by Department
    # ==================================================

    @staticmethod
    def get_courses_by_department():

        db = ReportService.get_database()

        pipeline = [
            {
                "$group": {
                    "_id": "$department",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]

        result = {}

        for row in db.courses.aggregate(pipeline):
            result[row["_id"]] = row["count"]

        return result