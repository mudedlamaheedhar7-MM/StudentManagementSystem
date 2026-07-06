import customtkinter as ctk
from tkinter import messagebox

from models.attendance import Attendance
from controllers.attendance_controller import AttendanceController


class EditAttendanceDialog(ctk.CTkToplevel):

    def __init__(self, parent, attendance_id):

        super().__init__(parent)

        self.parent = parent
        self.attendance_id = attendance_id

        self.record = AttendanceController.get_attendance_by_id(
            attendance_id
        )

        self.title("Edit Attendance")
        self.geometry("650x650")
        self.resizable(False, False)

        self.grab_set()

        self.build()

    # --------------------------------------------------

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Edit Attendance",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        form = ctk.CTkScrollableFrame(self)

        form.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # ------------------------------------------
        # Attendance ID
        # ------------------------------------------

        ctk.CTkLabel(
            form,
            text="Attendance ID"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.attendance_entry = ctk.CTkEntry(form)

        self.attendance_entry.pack(
            fill="x",
            padx=20
        )

        self.attendance_entry.insert(
            0,
            self.record["attendance_id"]
        )

        self.attendance_entry.configure(
            state="disabled"
        )

        # ------------------------------------------
        # Student ID
        # ------------------------------------------

        ctk.CTkLabel(
            form,
            text="Student ID"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.student_id_entry = ctk.CTkEntry(form)

        self.student_id_entry.pack(
            fill="x",
            padx=20
        )

        self.student_id_entry.insert(
            0,
            self.record["student_id"]
        )

        self.student_id_entry.configure(
            state="disabled"
        )

        # ------------------------------------------
        # Student Name
        # ------------------------------------------

        ctk.CTkLabel(
            form,
            text="Student Name"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.name_entry = ctk.CTkEntry(form)

        self.name_entry.pack(
            fill="x",
            padx=20
        )

        self.name_entry.insert(
            0,
            self.record["student_name"]
        )

        self.name_entry.configure(
            state="disabled"
        )

        # ------------------------------------------
        # Course
        # ------------------------------------------

        ctk.CTkLabel(
            form,
            text="Course"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.course_entry = ctk.CTkEntry(form)

        self.course_entry.pack(
            fill="x",
            padx=20
        )

        self.course_entry.insert(
            0,
            self.record["course"]
        )

        self.course_entry.configure(
            state="disabled"
        )

        # ------------------------------------------
        # Department
        # ------------------------------------------

        ctk.CTkLabel(
            form,
            text="Department"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.department_entry = ctk.CTkEntry(form)

        self.department_entry.pack(
            fill="x",
            padx=20
        )

        self.department_entry.insert(
            0,
            self.record["department"]
        )

        self.department_entry.configure(
            state="disabled"
        )

        # ------------------------------------------
        # Date
        # ------------------------------------------

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
            self.record["date"]
        )

        # ------------------------------------------
        # Status
        # ------------------------------------------

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

        self.status_combo.pack(
            fill="x",
            padx=20
        )

        self.status_combo.set(
            self.record["status"]
        )

        # ------------------------------------------
        # Update Button
        # ------------------------------------------

        update_btn = ctk.CTkButton(
            form,
            text="💾 Update Attendance",
            width=250,
            command=self.update_attendance
        )

        update_btn.pack(
            pady=30
        )

    # --------------------------------------------------

    def update_attendance(self):

        attendance = Attendance(

            attendance_id=self.record["attendance_id"],

            student_id=self.record["student_id"],

            student_name=self.record["student_name"],

            course=self.record["course"],

            department=self.record["department"],

            date=self.date_entry.get(),

            status=self.status_combo.get()

        )

        updated = AttendanceController.update_attendance(
            attendance
        )

        if updated:

            messagebox.showinfo(
                "Success",
                "Attendance updated successfully!"
            )

            self.parent.load_attendance()

            self.destroy()

        else:

            messagebox.showwarning(
                "No Changes",
                "No changes were made."
            )