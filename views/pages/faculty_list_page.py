import customtkinter as ctk
from tkinter import ttk, messagebox

from controllers.faculty_controller import FacultyController
from views.faculty.add_faculty_dialog import AddFacultyDialog
from views.faculty.edit_faculty_dialog import EditFacultyDialog


class FacultyListPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.build()
        self.load_faculty()

    # --------------------------------------------------
    # Build UI
    # --------------------------------------------------

    def build(self):

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

        # Live Search

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_faculty
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

        # Double Click

        self.table.bind(
            "<Double-1>",
            self.on_double_click
        )

    # --------------------------------------------------
    # Populate Table
    # --------------------------------------------------

    def populate_table(self, faculty_members):

        for row in self.table.get_children():
            self.table.delete(row)

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
    # Load Faculty
    # --------------------------------------------------

    def load_faculty(self):

        faculty_members = FacultyController.get_all_faculty()

        self.populate_table(
            faculty_members
        )

    # --------------------------------------------------
    # Search Faculty
    # --------------------------------------------------

    def search_faculty(self, event):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_faculty()
            return

        faculty_members = FacultyController.search_faculty(
            keyword
        )

        self.populate_table(
            faculty_members
        )

    # --------------------------------------------------
    # Add Faculty
    # --------------------------------------------------

    def open_add_dialog(self):

        AddFacultyDialog(self)

    # --------------------------------------------------
    # Delete Faculty
    # --------------------------------------------------

    def delete_faculty(self):

        selected = self.table.focus()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a faculty member to delete."
            )

            return

        values = self.table.item(selected)["values"]

        faculty_id = values[0]
        faculty_name = values[2]

        confirm = messagebox.askyesno(
            "Delete Faculty",
            f"Are you sure you want to delete\n\n{faculty_name} ({faculty_id})?"
        )

        if not confirm:
            return

        deleted = FacultyController.delete_faculty(
            faculty_id
        )

        if deleted:

            messagebox.showinfo(
                "Success",
                "Faculty deleted successfully!"
            )

            self.load_faculty()

        else:

            messagebox.showerror(
                "Error",
                "Failed to delete faculty."
            )

    # --------------------------------------------------
    # Double Click -> Edit Faculty
    # --------------------------------------------------

    def on_double_click(self, event):

        selected = self.table.focus()

        if not selected:
            return

        values = self.table.item(selected)["values"]

        faculty_id = values[0]

        EditFacultyDialog(
            self,
            faculty_id
        )