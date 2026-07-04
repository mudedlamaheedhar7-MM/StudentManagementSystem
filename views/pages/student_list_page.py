import customtkinter as ctk
from tkinter import ttk, messagebox

from controllers.student_controller import StudentController
from views.students.add_student_dialog import AddStudentDialog
from views.students.edit_student_dialog import EditStudentDialog


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

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        # ---------------- Top Bar ----------------

        top_frame = ctk.CTkFrame(self)

        top_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.search_entry = ctk.CTkEntry(
            top_frame,
            width=300,
            placeholder_text="Search Student..."
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        # ✅ Live Search
        self.search_entry.bind(
            "<KeyRelease>",
            self.search_students
        )

        refresh_btn = ctk.CTkButton(
            top_frame,
            text="Refresh",
            command=self.load_students
        )

        refresh_btn.pack(
            side="right",
            padx=10
        )

        add_btn = ctk.CTkButton(
            top_frame,
            text="➕ Add Student",
            command=self.open_add_dialog
        )

        add_btn.pack(
            side="right",
            padx=10
        )

        delete_btn = ctk.CTkButton(
            top_frame,
            text="🗑 Delete Student",
            fg_color="red",
            hover_color="darkred",
            command=self.delete_student
        )

        delete_btn.pack(
            side="right",
            padx=10
        )

        # ---------------- Student Table ----------------

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

            self.table.column(
                key,
                width=120,
                anchor="center"
            )

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ---------------- Double Click ----------------

        self.table.bind(
            "<Double-1>",
            self.on_double_click
        )

    # ---------------------------------------------------

    def populate_table(self, students):

        for row in self.table.get_children():
            self.table.delete(row)

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

    # ---------------------------------------------------

    def load_students(self):

        students = StudentController.get_all_students()

        self.populate_table(students)

    # ---------------------------------------------------

    def search_students(self, event):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_students()
            return

        students = StudentController.search_students(keyword)

        self.populate_table(students)

    # ---------------------------------------------------

    def open_add_dialog(self):

        AddStudentDialog(self)

    # ---------------------------------------------------

    def on_double_click(self, event):

        selected = self.table.focus()

        if not selected:
            return

        values = self.table.item(selected)["values"]

        student_id = values[0]

        EditStudentDialog(
            self,
            student_id
        )

    # ---------------------------------------------------

    def delete_student(self):

        selected = self.table.focus()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a student to delete."
            )

            return

        values = self.table.item(selected)["values"]

        student_id = values[0]

        confirm = messagebox.askyesno(
            "Delete Student",
            f"Are you sure you want to delete\n\n{student_id}?"
        )

        if not confirm:
            return

        deleted = StudentController.delete_student(student_id)

        if deleted:

            messagebox.showinfo(
                "Success",
                "Student deleted successfully!"
            )

            self.load_students()

        else:

            messagebox.showerror(
                "Error",
                "Failed to delete student."
            )