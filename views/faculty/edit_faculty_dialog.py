import customtkinter as ctk
from tkinter import messagebox

from views.components.form_builder import FormBuilder
from models.faculty import Faculty
from controllers.faculty_controller import FacultyController


class EditFacultyDialog(ctk.CTkToplevel):

    def __init__(self, parent, faculty_id):

        super().__init__(parent)

        self.parent = parent
        self.faculty_id = faculty_id

        self.faculty = FacultyController.get_faculty_by_id(
            faculty_id
        )

        self.title("Edit Faculty")
        self.geometry("650x780")
        self.resizable(False, False)

        self.grab_set()

        self.build()

    # ----------------------------------------

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Edit Faculty",
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

        self.load_faculty()

        update_btn = ctk.CTkButton(
            self,
            text="💾 Update Faculty",
            command=self.update_faculty
        )

        update_btn.pack(pady=20)

    # ----------------------------------------

    def load_faculty(self):

        self.fields["Faculty ID"].insert(
            0,
            self.faculty["faculty_id"]
        )

        self.fields["Employee ID"].insert(
            0,
            self.faculty["employee_id"]
        )

        self.fields["Faculty ID"].configure(
            state="disabled"
        )

        self.fields["Employee ID"].configure(
            state="disabled"
        )

        self.fields["First Name"].insert(
            0,
            self.faculty["first_name"]
        )

        self.fields["Last Name"].insert(
            0,
            self.faculty["last_name"]
        )

        self.fields["Gender"].set(
            self.faculty["gender"]
        )

        self.fields["Phone"].insert(
            0,
            self.faculty["phone"]
        )

        self.fields["Email"].insert(
            0,
            self.faculty["email"]
        )

        self.fields["Department"].insert(
            0,
            self.faculty["department"]
        )

        self.fields["Designation"].insert(
            0,
            self.faculty["designation"]
        )

        self.fields["Qualification"].insert(
            0,
            self.faculty["qualification"]
        )

        self.fields["Experience"].insert(
            0,
            str(self.faculty["experience"])
        )

        self.fields["Salary"].insert(
            0,
            str(self.faculty["salary"])
        )

    # ----------------------------------------

    def update_faculty(self):

        try:

            faculty = Faculty(

                faculty_id=self.faculty["faculty_id"],

                employee_id=self.faculty["employee_id"],

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
                ),

                status=self.faculty.get(
                    "status",
                    "Active"
                )
            )

            updated = FacultyController.update_faculty(
                faculty
            )

            if updated:

                messagebox.showinfo(
                    "Success",
                    "Faculty updated successfully!"
                )

                self.parent.load_faculty()

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