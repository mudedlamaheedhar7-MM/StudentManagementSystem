from database.mongodb import mongodb


class CourseService:

    @staticmethod
    def get_collection():
        db = mongodb.get_database()
        return db.courses

    # ------------------------------------------
    # CREATE COURSE
    # ------------------------------------------

    @staticmethod
    def create_course(course):

        collection = CourseService.get_collection()

        existing = collection.find_one(
            {"course_id": course.course_id}
        )

        if existing:
            return False

        collection.insert_one(
            course.to_dict()
        )

        return True

    # ------------------------------------------
    # GET ALL COURSES
    # ------------------------------------------

    @staticmethod
    def get_all_courses():

        collection = CourseService.get_collection()

        return list(
            collection.find(
                {},
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GET COURSE BY ID
    # ------------------------------------------

    @staticmethod
    def get_course_by_id(course_id):

        collection = CourseService.get_collection()

        return collection.find_one(
            {"course_id": course_id},
            {"_id": 0}
        )

    # ------------------------------------------
    # UPDATE COURSE
    # ------------------------------------------

    @staticmethod
    def update_course(course):

        collection = CourseService.get_collection()

        result = collection.update_one(
            {"course_id": course.course_id},
            {"$set": course.to_dict()}
        )

        return result.modified_count > 0

    # ------------------------------------------
    # DELETE COURSE
    # ------------------------------------------

    @staticmethod
    def delete_course(course_id):

        collection = CourseService.get_collection()

        result = collection.delete_one(
            {"course_id": course_id}
        )

        return result.deleted_count > 0

    # ------------------------------------------
    # SEARCH COURSES
    # ------------------------------------------

    @staticmethod
    def search_courses(keyword):

        collection = CourseService.get_collection()

        query = {
            "$or": [
                {"course_id": {"$regex": keyword, "$options": "i"}},
                {"course_name": {"$regex": keyword, "$options": "i"}},
                {"department": {"$regex": keyword, "$options": "i"}},
                {"duration": {"$regex": keyword, "$options": "i"}},
                {"status": {"$regex": keyword, "$options": "i"}}
            ]
        }

        return list(
            collection.find(
                query,
                {"_id": 0}
            )
        )

    # ------------------------------------------
    # GENERATE COURSE ID
    # ------------------------------------------

    @staticmethod
    def generate_course_id():

        collection = CourseService.get_collection()

        last = collection.find_one(
            {},
            sort=[("course_id", -1)]
        )

        if not last:
            return "CRS0001"

        number = int(
            last["course_id"].replace("CRS", "")
        )

        number += 1

        return f"CRS{number:04d}"