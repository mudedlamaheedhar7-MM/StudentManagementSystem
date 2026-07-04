from database.mongodb import mongodb


class FacultyService:

    @staticmethod
    def get_collection():
        db = mongodb.get_database()
        return db.faculty

    # ------------------------------------------
    # CREATE FACULTY
    # ------------------------------------------

    @staticmethod
    def create_faculty(faculty):

        collection = FacultyService.get_collection()

        existing = collection.find_one(
            {"faculty_id": faculty.faculty_id}
        )

        if existing:
            print("⚠️ Faculty already exists.")
            return False

        collection.insert_one(
            faculty.to_dict()
        )

        print("✅ Faculty inserted successfully.")

        return True

    # ------------------------------------------
    # GET ALL FACULTY
    # ------------------------------------------

    @staticmethod
    def get_all_faculty():

        collection = FacultyService.get_collection()

        return list(
            collection.find(
                {},
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GET FACULTY BY ID
    # ------------------------------------------

    @staticmethod
    def get_faculty_by_id(faculty_id):

        collection = FacultyService.get_collection()

        return collection.find_one(
            {"faculty_id": faculty_id},
            {"_id": 0}
        )

    # ------------------------------------------
    # UPDATE FACULTY
    # ------------------------------------------

    @staticmethod
    def update_faculty(faculty):

        collection = FacultyService.get_collection()

        result = collection.update_one(
            {"faculty_id": faculty.faculty_id},
            {"$set": faculty.to_dict()}
        )

        return result.modified_count > 0

    # ------------------------------------------
    # DELETE FACULTY
    # ------------------------------------------

    @staticmethod
    def delete_faculty(faculty_id):

        collection = FacultyService.get_collection()

        result = collection.delete_one(
            {"faculty_id": faculty_id}
        )

        return result.deleted_count > 0

    # ------------------------------------------
    # SEARCH FACULTY
    # ------------------------------------------

    @staticmethod
    def search_faculty(keyword):

        collection = FacultyService.get_collection()

        query = {
            "$or": [
                {"faculty_id": {"$regex": keyword, "$options": "i"}},
                {"employee_id": {"$regex": keyword, "$options": "i"}},
                {"first_name": {"$regex": keyword, "$options": "i"}},
                {"last_name": {"$regex": keyword, "$options": "i"}},
                {"department": {"$regex": keyword, "$options": "i"}},
                {"designation": {"$regex": keyword, "$options": "i"}},
                {"qualification": {"$regex": keyword, "$options": "i"}}
            ]
        }

        return list(
            collection.find(
                query,
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GENERATE FACULTY ID
    # ------------------------------------------

    @staticmethod
    def generate_faculty_id():

        collection = FacultyService.get_collection()

        last_faculty = collection.find_one(
            {},
            sort=[("faculty_id", -1)]
        )

        if not last_faculty:
            return "FAC0001"

        last_id = last_faculty["faculty_id"]

        number = int(
            last_id.replace("FAC", "")
        )

        number += 1

        return f"FAC{number:04d}"

    # ------------------------------------------
    # GENERATE EMPLOYEE ID
    # ------------------------------------------

    @staticmethod
    def generate_employee_id():

        collection = FacultyService.get_collection()

        last_faculty = collection.find_one(
            {},
            sort=[("employee_id", -1)]
        )

        if not last_faculty:
            return "EMP0001"

        last_id = last_faculty["employee_id"]

        number = int(
            last_id.replace("EMP", "")
        )

        number += 1

        return f"EMP{number:04d}"