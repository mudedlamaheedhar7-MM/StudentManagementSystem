import customtkinter as ctk
from tkinter import messagebox

from views.components.form_builder import FormBuilder
from models.course import Course
from controllers.course_controller import CourseController


class EditCourseDialog(ctk.CTkToplevel):

    def __init__(self, parent, course_id):

        super().__init__(parent)

        self.parent = parent
        self.course_id = course_id

        self.course = CourseController.get_course_by_id(course_id)

        self.title("Edit Course")
        self.geometry("650x650")
        self.resizable(False, False)

        self.grab_set()

        self.build()

    # --------------------------------------------------

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Edit Course",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        fields = [
            ("Course ID", "entry"),
            ("Course Name", "entry"),
            ("Department", "combo", ["BBA", "BCA", "MBA"]),
            ("Semester", "combo", ["1", "2", "3", "4", "5", "6"]),
            ("Credits", "combo", ["1", "2", "3", "4", "5", "6"]),
            ("Duration", "entry"),
            ("Description", "entry")
        ]

        self.fields = FormBuilder.create_form(
            self,
            fields
        )

        self.load_course()

        update_btn = ctk.CTkButton(
            self,
            text="💾 Update Course",
            command=self.update_course
        )

        update_btn.pack(pady=20)

    # --------------------------------------------------

    def load_course(self):

        self.fields["Course ID"].insert(
            0,
            self.course["course_id"]
        )

        self.fields["Course ID"].configure(
            state="disabled"
        )

        self.fields["Course Name"].insert(
            0,
            self.course["course_name"]
        )

        self.fields["Department"].set(
            self.course["department"]
        )

        self.fields["Semester"].set(
            str(self.course["semester"])
        )

        self.fields["Credits"].set(
            str(self.course["credits"])
        )

        self.fields["Duration"].insert(
            0,
            self.course["duration"]
        )

        self.fields["Description"].insert(
            0,
            self.course["description"]
        )

    # --------------------------------------------------

    def update_course(self):

        try:

            course = Course(

                course_id=self.course_id,

                course_name=self.fields["Course Name"].get(),

                department=self.fields["Department"].get(),

                semester=int(
                    self.fields["Semester"].get()
                ),

                credits=int(
                    self.fields["Credits"].get()
                ),

                duration=self.fields["Duration"].get(),

                description=self.fields["Description"].get(),

                status=self.course.get(
                    "status",
                    "Active"
                )
            )

            updated = CourseController.update_course(
                course
            )

            if updated:

                messagebox.showinfo(
                    "Success",
                    "Course updated successfully!"
                )

                self.parent.load_courses()

                self.destroy()

            else:

                messagebox.showwarning(
                    "No Changes",
                    "No changes were made."
                )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )