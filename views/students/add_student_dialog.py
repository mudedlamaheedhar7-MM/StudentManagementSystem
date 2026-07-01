import customtkinter as ctk
from tkinter import messagebox

from views.components.form_builder import FormBuilder
from models.student import Student
from controllers.student_controller import StudentController


class AddStudentDialog(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.title("Add Student")
        self.geometry("650x700")
        self.resizable(False, False)

        # Make dialog modal
        self.grab_set()

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Add New Student",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        fields = [
            ("Admission No", "entry"),
            ("First Name", "entry"),
            ("Last Name", "entry"),
            ("Gender", "combo", ["Male", "Female", "Other"]),
            ("Phone", "entry"),
            ("Email", "entry"),
            ("Course", "combo", ["BBA", "BCA", "MBA"]),
            ("Department", "combo", ["HR", "Finance", "Marketing"]),
            ("Semester", "combo", ["1", "2", "3", "4", "5", "6"]),
            ("Batch", "entry")
        ]

        self.fields = FormBuilder.create_form(
            self,
            fields
        )

        save_button = ctk.CTkButton(
            self,
            text="💾 Save Student",
            width=250,
            command=self.save_student
        )

        save_button.pack(pady=20)

    def save_student(self):

        try:

            student = Student(

                student_id=StudentController.generate_student_id(),

                admission_no=self.fields["Admission No"].get(),

                first_name=self.fields["First Name"].get(),

                last_name=self.fields["Last Name"].get(),

                gender=self.fields["Gender"].get(),

                dob="",

                phone=self.fields["Phone"].get(),

                email=self.fields["Email"].get(),

                address="",

                course=self.fields["Course"].get(),

                department=self.fields["Department"].get(),

                semester=int(self.fields["Semester"].get()),

                batch=self.fields["Batch"].get()
            )

            saved = StudentController.save_student(student)

            if saved:

                messagebox.showinfo(
                    "Success",
                    "Student added successfully!"
                )

                # Refresh Student List
                self.parent.load_students()

                # Close dialog
                self.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Student already exists."
                )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )