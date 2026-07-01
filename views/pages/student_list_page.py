import customtkinter as ctk
from tkinter import ttk

from controllers.student_controller import StudentController
from views.students.add_student_dialog import AddStudentDialog


class StudentListPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.build()
        self.load_students()

    def build(self):

        # ---------------- Title ----------------

        title = ctk.CTkLabel(
            self,
            text="Student List",
            font=("Arial", 24, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))

        # ---------------- Top Bar ----------------

        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=20, pady=10)

        self.search_entry = ctk.CTkEntry(
            top_frame,
            width=300,
            placeholder_text="Search Student..."
        )
        self.search_entry.pack(side="left", padx=10)

        refresh_btn = ctk.CTkButton(
            top_frame,
            text="Refresh",
            command=self.load_students
        )
        refresh_btn.pack(side="right", padx=10)

        add_btn = ctk.CTkButton(
            top_frame,
            text="➕ Add Student",
            command=self.open_add_dialog
        )
        add_btn.pack(side="right", padx=10)

        # ---------------- Table ----------------

        columns = (
            "student_id",
            "admission_no",
            "name",
            "course",
            "department",
            "semester",
            "status",
            "phone"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        headings = {
            "student_id": "Student ID",
            "admission_no": "Admission No",
            "name": "Name",
            "course": "Course",
            "department": "Department",
            "semester": "Semester",
            "status": "Status",
            "phone": "Phone"
        }

        for key, value in headings.items():
            self.table.heading(key, text=value)
            self.table.column(key, width=120, anchor="center")

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def load_students(self):

        for row in self.table.get_children():
            self.table.delete(row)

        students = StudentController.get_all_students()

        for student in students:

            self.table.insert(
                "",
                "end",
                values=(
                    student["student_id"],
                    student["admission_no"],
                    f'{student["first_name"]} {student["last_name"]}',
                    student["course"],
                    student["department"],
                    student["semester"],
                    student["status"],
                    student["phone"]
                )
            )

    def open_add_dialog(self):
        AddStudentDialog(self)