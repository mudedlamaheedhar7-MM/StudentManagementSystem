from database.mongodb import mongodb


class StudentService:

    @staticmethod
    def get_collection():
        db = mongodb.get_database()
        return db.students

    # --------------------------------------------------
    # CREATE STUDENT
    # --------------------------------------------------

    @staticmethod
    def create_student(student):

        collection = StudentService.get_collection()

        existing = collection.find_one(
            {"student_id": student.student_id}
        )

        if existing:
            print("⚠️ Student already exists.")
            return False

        collection.insert_one(student.to_dict())

        print("✅ Student inserted successfully.")
        return True

    # --------------------------------------------------
    # GET ALL STUDENTS
    # --------------------------------------------------

    @staticmethod
    def get_all_students():

        collection = StudentService.get_collection()

        return list(
            collection.find(
                {},
                {"_id": 0}
            )
        )

    # --------------------------------------------------
    # SEARCH STUDENTS
    # --------------------------------------------------

    @staticmethod
    def search_students(keyword):

        collection = StudentService.get_collection()

        query = {
            "$or": [
                {
                    "student_id": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                },
                {
                    "admission_no": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                },
                {
                    "first_name": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                },
                {
                    "last_name": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                },
                {
                    "course": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                },
                {
                    "department": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                },
                {
                    "phone": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                },
                {
                    "email": {
                        "$regex": keyword,
                        "$options": "i"
                    }
                }
            ]
        }

        return list(
            collection.find(
                query,
                {"_id": 0}
            )
        )

    # --------------------------------------------------
    # GET STUDENT BY ID
    # --------------------------------------------------

    @staticmethod
    def get_student_by_id(student_id):

        collection = StudentService.get_collection()

        return collection.find_one(
            {"student_id": student_id},
            {"_id": 0}
        )

    # --------------------------------------------------
    # UPDATE STUDENT
    # --------------------------------------------------

    @staticmethod
    def update_student(student):

        collection = StudentService.get_collection()

        result = collection.update_one(
            {
                "student_id": student.student_id
            },
            {
                "$set": student.to_dict()
            }
        )

        return result.modified_count > 0

    # --------------------------------------------------
    # DELETE STUDENT
    # --------------------------------------------------

    @staticmethod
    def delete_student(student_id):

        collection = StudentService.get_collection()

        result = collection.delete_one(
            {
                "student_id": student_id
            }
        )

        return result.deleted_count > 0

    # --------------------------------------------------
    # GENERATE STUDENT ID
    # --------------------------------------------------

    @staticmethod
    def generate_student_id():

        collection = StudentService.get_collection()

        last_student = collection.find_one(
            {},
            sort=[("student_id", -1)]
        )

        if not last_student:
            return "SMS0001"

        last_id = last_student["student_id"]

        number = int(last_id.replace("SMS", ""))

        number += 1

        return f"SMS{number:04d}"