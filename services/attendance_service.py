from database.mongodb import mongodb


class AttendanceService:

    @staticmethod
    def get_collection():
        db = mongodb.get_database()
        return db.attendance

    # ------------------------------------------
    # CREATE ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def create_attendance(attendance):

        collection = AttendanceService.get_collection()

        existing = collection.find_one(
            {
                "student_id": attendance.student_id,
                "date": attendance.date
            }
        )

        if existing:
            return False

        collection.insert_one(
            attendance.to_dict()
        )

        return True

    # ------------------------------------------
    # GET ALL ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def get_all_attendance():

        collection = AttendanceService.get_collection()

        return list(
            collection.find(
                {},
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GET ATTENDANCE BY ID
    # ------------------------------------------

    @staticmethod
    def get_attendance_by_id(attendance_id):

        collection = AttendanceService.get_collection()

        return collection.find_one(
            {"attendance_id": attendance_id},
            {"_id": 0}
        )

    # ------------------------------------------
    # GET ATTENDANCE BY DATE
    # ------------------------------------------

    @staticmethod
    def get_attendance_by_date(date):

        collection = AttendanceService.get_collection()

        return list(
            collection.find(
                {"date": date},
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # UPDATE ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def update_attendance(attendance):

        collection = AttendanceService.get_collection()

        result = collection.update_one(
            {"attendance_id": attendance.attendance_id},
            {"$set": attendance.to_dict()}
        )

        return result.modified_count > 0

    # ------------------------------------------
    # DELETE ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def delete_attendance(attendance_id):

        collection = AttendanceService.get_collection()

        result = collection.delete_one(
            {"attendance_id": attendance_id}
        )

        return result.deleted_count > 0

    # ------------------------------------------
    # SEARCH ATTENDANCE
    # ------------------------------------------

    @staticmethod
    def search_attendance(keyword):

        collection = AttendanceService.get_collection()

        query = {
            "$or": [
                {"attendance_id": {"$regex": keyword, "$options": "i"}},
                {"student_id": {"$regex": keyword, "$options": "i"}},
                {"student_name": {"$regex": keyword, "$options": "i"}},
                {"course": {"$regex": keyword, "$options": "i"}},
                {"department": {"$regex": keyword, "$options": "i"}},
                {"status": {"$regex": keyword, "$options": "i"}},
                {"date": {"$regex": keyword, "$options": "i"}}
            ]
        }

        return list(
            collection.find(
                query,
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GENERATE ATTENDANCE ID
    # ------------------------------------------

    @staticmethod
    def generate_attendance_id():

        collection = AttendanceService.get_collection()

        last = collection.find_one(
            {},
            sort=[("attendance_id", -1)]
        )

        if not last:
            return "ATT0001"

        number = int(
            last["attendance_id"].replace(
                "ATT",
                ""
            )
        )

        number += 1

        return f"ATT{number:04d}"