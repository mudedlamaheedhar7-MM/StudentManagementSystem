import customtkinter as ctk
from tkinter import ttk, messagebox

from controllers.faculty_controller import FacultyController
from views.faculty.add_faculty_dialog import AddFacultyDialog


class FacultyListPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.build()
        self.load_faculty()

    # --------------------------------------------------

    def build(self):

        # ---------------- Title ----------------

        title = ctk.CTkLabel(
            self,
            text="Faculty Management",
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
            placeholder_text="Search Faculty..."
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        refresh_btn = ctk.CTkButton(
            top_frame,
            text="Refresh",
            command=self.load_faculty
        )

        refresh_btn.pack(
            side="right",
            padx=10
        )

        add_btn = ctk.CTkButton(
            top_frame,
            text="➕ Add Faculty",
            command=self.open_add_dialog
        )

        add_btn.pack(
            side="right",
            padx=10
        )

        delete_btn = ctk.CTkButton(
            top_frame,
            text="🗑 Delete Faculty",
            fg_color="red",
            hover_color="darkred",
            command=self.delete_faculty
        )

        delete_btn.pack(
            side="right",
            padx=10
        )

        # ---------------- Faculty Table ----------------

        columns = (
            "faculty_id",
            "employee_id",
            "name",
            "department",
            "designation",
            "status"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        headings = {
            "faculty_id": "Faculty ID",
            "employee_id": "Employee ID",
            "name": "Name",
            "department": "Department",
            "designation": "Designation",
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
            pady=20
        )

        self.table.bind(
            "<Double-1>",
            self.on_double_click
        )

    # --------------------------------------------------

    def load_faculty(self):

        for row in self.table.get_children():
            self.table.delete(row)

        faculty_members = FacultyController.get_all_faculty()

        for faculty in faculty_members:

            self.table.insert(
                "",
                "end",
                values=(
                    faculty["faculty_id"],
                    faculty["employee_id"],
                    f'{faculty["first_name"]} {faculty["last_name"]}',
                    faculty["department"],
                    faculty["designation"],
                    faculty["status"]
                )
            )

    # --------------------------------------------------

    def open_add_dialog(self):

        AddFacultyDialog(self)

    # --------------------------------------------------

    def delete_faculty(self):

        messagebox.showinfo(
            "Coming Soon",
            "Delete Faculty will be implemented in Sprint 5.2."
        )

    # --------------------------------------------------

    def on_double_click(self, event):

        messagebox.showinfo(
            "Coming Soon",
            "Edit Faculty will be implemented in Sprint 5.2."
        )