from database.mongodb import mongodb


class StudentService:

    @staticmethod
    def get_collection():
        db = mongodb.get_database()
        return db.students

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