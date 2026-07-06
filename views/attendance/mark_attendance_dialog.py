import customtkinter as ctk
from tkinter import messagebox
from datetime import date

from models.attendance import Attendance
from controllers.student_controller import StudentController
from controllers.attendance_controller import AttendanceController


class MarkAttendanceDialog(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.title("Mark Attendance")
        self.geometry("700x760")
        self.resizable(False, False)

        self.grab_set()

        self.students = StudentController.get_all_students()

        self.student_map = {}

        self.build()

    # --------------------------------------------------

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Mark Attendance",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # --------------------------------------------------
        # Scrollable Form
        # --------------------------------------------------

        form = ctk.CTkScrollableFrame(self)

        form.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # --------------------------------------------------
        # Attendance ID
        # --------------------------------------------------

        ctk.CTkLabel(
            form,
            text="Attendance ID"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.attendance_id = AttendanceController.generate_attendance_id()

        attendance_entry = ctk.CTkEntry(form)

        attendance_entry.pack(
            fill="x",
            padx=20
        )

        attendance_entry.insert(
            0,
            self.attendance_id
        )

        attendance_entry.configure(
            state="disabled"
        )

        # --------------------------------------------------
        # Student
        # --------------------------------------------------

        ctk.CTkLabel(
            form,
            text="Student"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        student_values = []

        for student in self.students:

            display = (
                f'{student["student_id"]} - '
                f'{student["first_name"]} '
                f'{student["last_name"]}'
            )

            student_values.append(display)

            self.student_map[display] = student

        self.student_combo = ctk.CTkComboBox(
            form,
            values=student_values,
            command=self.student_selected
        )

        self.student_combo.pack(
            fill="x",
            padx=20
        )

        # --------------------------------------------------
        # Student Name
        # --------------------------------------------------

        ctk.CTkLabel(
            form,
            text="Student Name"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.name_entry = ctk.CTkEntry(form)

        self.name_entry.pack(
            fill="x",
            padx=20
        )

        self.name_entry.configure(
            state="disabled"
        )

        # --------------------------------------------------
        # Course
        # --------------------------------------------------

        ctk.CTkLabel(
            form,
            text="Course"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.course_entry = ctk.CTkEntry(form)

        self.course_entry.pack(
            fill="x",
            padx=20
        )

        self.course_entry.configure(
            state="disabled"
        )

        # --------------------------------------------------
        # Department
        # --------------------------------------------------

        ctk.CTkLabel(
            form,
            text="Department"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.department_entry = ctk.CTkEntry(form)

        self.department_entry.pack(
            fill="x",
            padx=20
        )

        self.department_entry.configure(
            state="disabled"
        )

        # --------------------------------------------------
        # Date
        # --------------------------------------------------

        ctk.CTkLabel(
            form,
            text="Attendance Date"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.date_entry = ctk.CTkEntry(form)

        self.date_entry.pack(
            fill="x",
            padx=20
        )

        self.date_entry.insert(
            0,
            str(date.today())
        )

        # --------------------------------------------------
        # Status
        # --------------------------------------------------

        ctk.CTkLabel(
            form,
            text="Status"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.status_combo = ctk.CTkComboBox(
            form,
            values=[
                "Present",
                "Absent",
                "Late"
            ]
        )

        self.status_combo.set("Present")

        self.status_combo.pack(
            fill="x",
            padx=20
        )

        # --------------------------------------------------
        # Save Button
        # --------------------------------------------------

        save_btn = ctk.CTkButton(
            form,
            text="💾 Save Attendance",
            width=250,
            command=self.save_attendance
        )

        save_btn.pack(
            pady=30
        )

    # --------------------------------------------------

    def student_selected(self, value):

        student = self.student_map[value]

        self.name_entry.configure(state="normal")
        self.course_entry.configure(state="normal")
        self.department_entry.configure(state="normal")

        self.name_entry.delete(0, "end")
        self.course_entry.delete(0, "end")
        self.department_entry.delete(0, "end")

        self.name_entry.insert(
            0,
            f'{student["first_name"]} {student["last_name"]}'
        )

        self.course_entry.insert(
            0,
            student["course"]
        )

        self.department_entry.insert(
            0,
            student["department"]
        )

        self.name_entry.configure(state="disabled")
        self.course_entry.configure(state="disabled")
        self.department_entry.configure(state="disabled")

    # --------------------------------------------------

    def save_attendance(self):

        if self.student_combo.get() == "":

            messagebox.showwarning(
                "Validation",
                "Please select a student."
            )

            return

        student = self.student_map[
            self.student_combo.get()
        ]

        attendance = Attendance(

            attendance_id=self.attendance_id,

            student_id=student["student_id"],

            student_name=f'{student["first_name"]} {student["last_name"]}',

            course=student["course"],

            department=student["department"],

            date=self.date_entry.get(),

            status=self.status_combo.get()

        )

        saved = AttendanceController.save_attendance(
            attendance
        )

        if saved:

            messagebox.showinfo(
                "Success",
                "Attendance marked successfully!"
            )

            self.parent.load_attendance()

            self.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Failed to save attendance."
            )