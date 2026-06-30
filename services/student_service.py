from database.mongodb import mongodb


class StudentService:

    @staticmethod
    def get_collection():
        db = mongodb.get_database()
        return db.students

    @staticmethod
    def create_student(student):

        collection = StudentService.get_collection()

        # Check if student already exists
        existing = collection.find_one(
            {"student_id": student.student_id}
        )

        if existing:
            print("⚠️ Student already exists.")
            return False

        collection.insert_one(
            student.to_dict()
        )

        print("✅ Student inserted successfully.")
        return True

        return True 