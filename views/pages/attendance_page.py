import customtkinter as ctk
from tkinter import ttk, messagebox

from controllers.attendance_controller import AttendanceController
from views.attendance.mark_attendance_dialog import MarkAttendanceDialog
from views.attendance.edit_attendance_dialog import EditAttendanceDialog
from views.components.stat_card import StatCard


class AttendancePage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.build()
        self.load_attendance()

    # --------------------------------------------------
    # Build UI
    # --------------------------------------------------

    def build(self):

        #################################################
        # Title
        #################################################

        title = ctk.CTkLabel(
            self,
            text="Attendance Management",
            font=("Arial", 24, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        #################################################
        # Summary Cards
        #################################################

        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        # Total

        self.total_card = StatCard(
            cards_frame,
            title="Total",
            value="0",
            icon="📋",
            accent="#2563EB"
        )

        self.total_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        # Present

        self.present_card = StatCard(
            cards_frame,
            title="Present",
            value="0",
            icon="✅",
            accent="#16A34A"
        )

        self.present_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        # Absent

        self.absent_card = StatCard(
            cards_frame,
            title="Absent",
            value="0",
            icon="❌",
            accent="#DC2626"
        )

        self.absent_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        # Late

        self.late_card = StatCard(
            cards_frame,
            title="Late",
            value="0",
            icon="⏰",
            accent="#F59E0B"
        )

        self.late_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        #################################################
        # Top Bar
        #################################################

        top_frame = ctk.CTkFrame(self)

        top_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Search

        self.search_entry = ctk.CTkEntry(
            top_frame,
            width=260,
            placeholder_text="Search Attendance..."
        )

        self.search_entry.pack(
            side="left",
            padx=(10, 5)
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.live_search
        )

        # Date Filter

        self.date_entry = ctk.CTkEntry(
            top_frame,
            width=140,
            placeholder_text="YYYY-MM-DD"
        )

        self.date_entry.pack(
            side="left",
            padx=5
        )

        filter_btn = ctk.CTkButton(
            top_frame,
            text="Filter",
            width=90,
            command=self.filter_by_date
        )

        filter_btn.pack(
            side="left",
            padx=5
        )

        clear_btn = ctk.CTkButton(
            top_frame,
            text="Clear",
            width=80,
            command=self.load_attendance
        )

        clear_btn.pack(
            side="left",
            padx=5
        )

        # Right Side Buttons

        refresh_btn = ctk.CTkButton(
            top_frame,
            text="Refresh",
            width=100,
            command=self.load_attendance
        )

        refresh_btn.pack(
            side="right",
            padx=(5, 10)
        )

        add_btn = ctk.CTkButton(
            top_frame,
            text="✅ Mark Attendance",
            command=self.open_mark_dialog
        )

        add_btn.pack(
            side="right",
            padx=5
        )

        delete_btn = ctk.CTkButton(
            top_frame,
            text="🗑 Delete",
            fg_color="red",
            hover_color="darkred",
            command=self.delete_attendance
        )

        delete_btn.pack(
            side="right",
            padx=5
        )

        #################################################
        # Attendance Table
        #################################################

        columns = (
            "attendance_id",
            "student_id",
            "student_name",
            "course",
            "department",
            "date",
            "status"
        )

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Treeview.Heading",
            font=("Arial", 11, "bold")
        )

        style.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=18
        )

        headings = {
            "attendance_id": "Attendance ID",
            "student_id": "Student ID",
            "student_name": "Student Name",
            "course": "Course",
            "department": "Department",
            "date": "Date",
            "status": "Status"
        }

        for key, value in headings.items():

            self.table.heading(
                key,
                text=value
            )

            self.table.column(
                key,
                width=150,
                anchor="center"
            )

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.table.bind(
            "<Double-1>",
            self.on_double_click
        )
        # --------------------------------------------------
    # Populate Table
    # --------------------------------------------------

    def populate_table(self, attendance):

        for row in self.table.get_children():
            self.table.delete(row)

        for record in attendance:

            self.table.insert(
                "",
                "end",
                values=(
                    record["attendance_id"],
                    record["student_id"],
                    record["student_name"],
                    record["course"],
                    record["department"],
                    record["date"],
                    record["status"]
                )
            )

    # --------------------------------------------------
    # Update Summary Cards
    # --------------------------------------------------

    def update_summary(self, records):

        total = len(records)

        present = 0
        absent = 0
        late = 0

        for record in records:

            status = record["status"]

            if status == "Present":
                present += 1

            elif status == "Absent":
                absent += 1

            elif status == "Late":
                late += 1

        self.total_card.update_value(total)
        self.present_card.update_value(present)
        self.absent_card.update_value(absent)
        self.late_card.update_value(late)

    # --------------------------------------------------
    # Load Attendance
    # --------------------------------------------------

    def load_attendance(self):

        records = AttendanceController.get_all_attendance()

        self.populate_table(records)
        self.update_summary(records)

        self.search_entry.delete(0, "end")
        self.date_entry.delete(0, "end")

    # --------------------------------------------------
    # Live Search
    # --------------------------------------------------

    def live_search(self, event=None):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            records = AttendanceController.get_all_attendance()

        else:

            records = AttendanceController.search_attendance(
                keyword
            )

        self.populate_table(records)
        self.update_summary(records)

    # --------------------------------------------------
    # Filter By Date
    # --------------------------------------------------

    def filter_by_date(self):

        selected_date = self.date_entry.get().strip()

        if selected_date == "":

            self.load_attendance()
            return

        records = AttendanceController.get_attendance_by_date(
            selected_date
        )

        self.populate_table(records)
        self.update_summary(records)

    # --------------------------------------------------
    # Mark Attendance
    # --------------------------------------------------

    def open_mark_dialog(self):

        MarkAttendanceDialog(self)

    # --------------------------------------------------
    # Delete Attendance
    # --------------------------------------------------

    def delete_attendance(self):

        selected = self.table.focus()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select an attendance record."
            )

            return

        values = self.table.item(selected)["values"]

        attendance_id = values[0]

        confirm = messagebox.askyesno(
            "Delete Attendance",
            f"Are you sure you want to delete\n\n{attendance_id}?"
        )

        if not confirm:
            return

        deleted = AttendanceController.delete_attendance(
            attendance_id
        )

        if deleted:

            messagebox.showinfo(
                "Success",
                "Attendance deleted successfully!"
            )

            self.load_attendance()

        else:

            messagebox.showerror(
                "Error",
                "Failed to delete attendance."
            )

    # --------------------------------------------------
    # Edit Attendance
    # --------------------------------------------------

    def on_double_click(self, event):

        selected = self.table.focus()

        if not selected:
            return

        values = self.table.item(selected)["values"]

        attendance_id = values[0]

        EditAttendanceDialog(
            self,
            attendance_id
        )