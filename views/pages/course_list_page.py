import customtkinter as ctk
from tkinter import ttk, messagebox

from controllers.course_controller import CourseController
from views.course.add_course_dialog import AddCourseDialog
from views.course.edit_course_dialog import EditCourseDialog


class CourseListPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.build()
        self.load_courses()

    # --------------------------------------------------
    # Build UI
    # --------------------------------------------------

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Course Management",
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
            placeholder_text="Search Course..."
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        # -------- Live Search --------

        self.search_entry.bind(
            "<KeyRelease>",
            self.live_search
        )

        refresh_btn = ctk.CTkButton(
            top_frame,
            text="Refresh",
            command=self.load_courses
        )

        refresh_btn.pack(
            side="right",
            padx=10
        )

        add_btn = ctk.CTkButton(
            top_frame,
            text="➕ Add Course",
            command=self.open_add_dialog
        )

        add_btn.pack(
            side="right",
            padx=10
        )

        delete_btn = ctk.CTkButton(
            top_frame,
            text="🗑 Delete Course",
            fg_color="red",
            hover_color="darkred",
            command=self.delete_course
        )

        delete_btn.pack(
            side="right",
            padx=10
        )

        # ---------------- Course Table ----------------

        columns = (
            "course_id",
            "course_name",
            "department",
            "semester",
            "credits",
            "duration",
            "status"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        headings = {
            "course_id": "Course ID",
            "course_name": "Course Name",
            "department": "Department",
            "semester": "Semester",
            "credits": "Credits",
            "duration": "Duration",
            "status": "Status"
        }

        for key, value in headings.items():

            self.table.heading(
                key,
                text=value
            )

            self.table.column(
                key,
                width=140,
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

    # --------------------------------------------------
    # Populate Table
    # --------------------------------------------------

    def populate_table(self, courses):

        for row in self.table.get_children():
            self.table.delete(row)

        for course in courses:

            self.table.insert(
                "",
                "end",
                values=(
                    course["course_id"],
                    course["course_name"],
                    course["department"],
                    course["semester"],
                    course["credits"],
                    course["duration"],
                    course["status"]
                )
            )

    # --------------------------------------------------
    # Load Courses
    # --------------------------------------------------

    def load_courses(self):

        courses = CourseController.get_all_courses()

        self.populate_table(
            courses
        )

    # --------------------------------------------------
    # Live Search
    # --------------------------------------------------

    def live_search(self, event=None):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_courses()
            return

        courses = CourseController.search_courses(
            keyword
        )

        self.populate_table(
            courses
        )

    # --------------------------------------------------
    # Add Course
    # --------------------------------------------------

    def open_add_dialog(self):

        AddCourseDialog(self)

    # --------------------------------------------------
    # Delete Course
    # --------------------------------------------------

    def delete_course(self):

        selected = self.table.focus()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a course to delete."
            )

            return

        values = self.table.item(selected)["values"]

        course_id = values[0]

        confirm = messagebox.askyesno(
            "Delete Course",
            f"Are you sure you want to delete\n\n{course_id}?"
        )

        if not confirm:
            return

        deleted = CourseController.delete_course(
            course_id
        )

        if deleted:

            messagebox.showinfo(
                "Success",
                "Course deleted successfully!"
            )

            self.load_courses()

        else:

            messagebox.showerror(
                "Error",
                "Failed to delete course."
            )

    # --------------------------------------------------
    # Edit Course
    # --------------------------------------------------

    def on_double_click(self, event):

        selected = self.table.focus()

        if not selected:
            return

        values = self.table.item(selected)["values"]

        course_id = values[0]

        EditCourseDialog(
            self,
            course_id
        )