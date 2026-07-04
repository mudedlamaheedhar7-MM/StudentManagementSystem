import customtkinter as ctk
from tkinter import messagebox

from views.components.form_builder import FormBuilder
from models.student import Student
from controllers.student_controller import StudentController


class EditStudentDialog(ctk.CTkToplevel):

    def __init__(self, parent, student_id):

        super().__init__(parent)

        self.parent = parent
        self.student_id = student_id

        self.student = StudentController.get_student_by_id(student_id)

        if not self.student:
            messagebox.showerror(
                "Error",
                "Student not found."
            )
            self.destroy()
            return

        self.title("Edit Student")
        self.geometry("650x700")
        self.resizable(False, False)

        self.grab_set()

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Edit Student",
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

        self.load_student()

        update_btn = ctk.CTkButton(
            self,
            text="💾 Update Student",
            width=250,
            command=self.update_student
        )

        update_btn.pack(pady=20)

    def load_student(self):

        self.fields["Admission No"].insert(
            0,
            self.student.get("admission_no", "")
        )

        self.fields["First Name"].insert(
            0,
            self.student.get("first_name", "")
        )

        self.fields["Last Name"].insert(
            0,
            self.student.get("last_name", "")
        )

        self.fields["Gender"].set(
            self.student.get("gender", "Male")
        )

        self.fields["Phone"].insert(
            0,
            self.student.get("phone", "")
        )

        self.fields["Email"].insert(
            0,
            self.student.get("email", "")
        )

        self.fields["Course"].set(
            self.student.get("course", "BBA")
        )

        self.fields["Department"].set(
            self.student.get("department", "HR")
        )

        self.fields["Semester"].set(
            str(self.student.get("semester", 1))
        )

        self.fields["Batch"].insert(
            0,
            self.student.get("batch", "")
        )

    def update_student(self):

        try:

            updated_student = Student(

                student_id=self.student_id,

                admission_no=self.fields["Admission No"].get(),

                first_name=self.fields["First Name"].get(),

                last_name=self.fields["Last Name"].get(),

                gender=self.fields["Gender"].get(),

                dob=self.student.get("dob", ""),

                phone=self.fields["Phone"].get(),

                email=self.fields["Email"].get(),

                address=self.student.get("address", ""),

                course=self.fields["Course"].get(),

                department=self.fields["Department"].get(),

                semester=int(self.fields["Semester"].get()),

                batch=self.fields["Batch"].get(),

                attendance=self.student.get("attendance", 0),

                fees_due=self.student.get("fees_due", 0),

                status=self.student.get("status", "Active")
            )

            updated = StudentController.update_student(updated_student)

            if updated:

                messagebox.showinfo(
                    "Success",
                    "Student updated successfully!"
                )

                self.parent.load_students()

                self.destroy()

            else:

                messagebox.showinfo(
                    "Information",
                    "No changes were made."
                )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error))