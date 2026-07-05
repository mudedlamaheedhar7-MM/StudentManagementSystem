from services.course_service import CourseService


class CourseController:

    @staticmethod
    def save_course(course):
        return CourseService.create_course(course)

    @staticmethod
    def get_all_courses():
        return CourseService.get_all_courses()

    @staticmethod
    def get_course_by_id(course_id):
        return CourseService.get_course_by_id(course_id)

    @staticmethod
    def update_course(course):
        return CourseService.update_course(course)

    @staticmethod
    def delete_course(course_id):
        return CourseService.delete_course(course_id)

    @staticmethod
    def search_courses(keyword):
        return CourseService.search_courses(keyword)

    @staticmethod
    def generate_course_id():
        return CourseService.generate_course_id()