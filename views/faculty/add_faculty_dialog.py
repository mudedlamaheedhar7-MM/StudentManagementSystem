import customtkinter as ctk
from tkinter import messagebox

from views.components.form_builder import FormBuilder
from models.faculty import Faculty
from controllers.faculty_controller import FacultyController


class AddFacultyDialog(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.title("Add Faculty")
        self.geometry("650x780")
        self.resizable(False, False)

        self.grab_set()

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Add New Faculty",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        fields = [
            ("Faculty ID", "entry"),
            ("Employee ID", "entry"),
            ("First Name", "entry"),
            ("Last Name", "entry"),
            ("Gender", "combo", ["Male", "Female", "Other"]),
            ("Phone", "entry"),
            ("Email", "entry"),
            ("Department", "entry"),
            ("Designation", "entry"),
            ("Qualification", "entry"),
            ("Experience", "entry"),
            ("Salary", "entry")
        ]

        self.fields = FormBuilder.create_form(
            self,
            fields
        )

        # ------------------------------------------
        # Auto Generate IDs
        # ------------------------------------------

        faculty_id = FacultyController.generate_faculty_id()
        employee_id = FacultyController.generate_employee_id()

        self.fields["Faculty ID"].insert(
            0,
            faculty_id
        )

        self.fields["Employee ID"].insert(
            0,
            employee_id
        )

        self.fields["Faculty ID"].configure(
            state="disabled"
        )

        self.fields["Employee ID"].configure(
            state="disabled"
        )

        save_btn = ctk.CTkButton(
            self,
            text="💾 Save Faculty",
            width=250,
            command=self.save_faculty
        )

        save_btn.pack(pady=20)

    def save_faculty(self):

        try:

            faculty = Faculty(

                faculty_id=self.fields["Faculty ID"].get(),

                employee_id=self.fields["Employee ID"].get(),

                first_name=self.fields["First Name"].get(),

                last_name=self.fields["Last Name"].get(),

                gender=self.fields["Gender"].get(),

                phone=self.fields["Phone"].get(),

                email=self.fields["Email"].get(),

                department=self.fields["Department"].get(),

                designation=self.fields["Designation"].get(),

                qualification=self.fields["Qualification"].get(),

                experience=int(
                    self.fields["Experience"].get()
                ),

                salary=float(
                    self.fields["Salary"].get()
                )
            )

            saved = FacultyController.save_faculty(
                faculty
            )

            if saved:

                messagebox.showinfo(
                    "Success",
                    "Faculty added successfully!"
                )

                self.parent.load_faculty()

                self.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Faculty already exists."
                )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )