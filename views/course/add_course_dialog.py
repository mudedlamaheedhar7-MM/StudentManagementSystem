import customtkinter as ctk
from tkinter import messagebox

from views.components.form_builder import FormBuilder
from models.course import Course
from controllers.course_controller import CourseController


class AddCourseDialog(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.title("Add Course")
        self.geometry("650x650")
        self.resizable(False, False)

        self.grab_set()

        self.build()

    # --------------------------------------------------

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Add New Course",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        fields = [
            ("Course ID", "entry"),
            ("Course Name", "entry"),
            ("Department", "combo",
                ["BBA", "BCA", "MBA"]),
            ("Semester", "combo",
                ["1", "2", "3", "4", "5", "6"]),
            ("Credits", "combo",
                ["1", "2", "3", "4", "5", "6"]),
            ("Duration", "entry"),
            ("Description", "entry")
        ]

        self.fields = FormBuilder.create_form(
            self,
            fields
        )

        # Auto Generate Course ID

        self.course_id = CourseController.generate_course_id()

        self.fields["Course ID"].insert(
            0,
            self.course_id
        )

        self.fields["Course ID"].configure(
            state="disabled"
        )

        save_btn = ctk.CTkButton(
            self,
            text="💾 Save Course",
            width=250,
            command=self.save_course
        )

        save_btn.pack(pady=20)

    # --------------------------------------------------

    def save_course(self):

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

                description=self.fields["Description"].get()
            )

            saved = CourseController.save_course(
                course
            )

            if saved:

                messagebox.showinfo(
                    "Success",
                    "Course added successfully!"
                )

                self.parent.load_courses()

                self.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Course already exists."
                )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )