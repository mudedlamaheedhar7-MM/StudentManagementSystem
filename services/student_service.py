from database.mongodb import mongodb


class StudentService:

    @staticmethod
    def get_collection():

        db = mongodb.get_database()

        return db.students

    @staticmethod
    def create_student(student):

        collection = StudentService.get_collection()

        collection.insert_one(
            student.to_dict()
        )

        return True