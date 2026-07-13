import customtkinter as ctk

from views.components.sidebar import Sidebar
from views.components.header import Header

from views.pages.dashboard_page import DashboardPage
from views.pages.student_list_page import StudentListPage
from views.pages.faculty_list_page import FacultyListPage
from views.pages.course_list_page import CourseListPage
from views.pages.attendance_page import AttendancePage
from views.pages.fee_page import FeePage
from views.pages.reports_page import ReportsPage


class DashboardWindow:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.current_page = None

        self.build_dashboard()

    # --------------------------------------------------
    # Build Dashboard
    # --------------------------------------------------

    def build_dashboard(self):

        # Clear Login Screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Student Management System")

        #################################################
        # Root Grid
        #################################################

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        #################################################
        # Sidebar
        #################################################

        self.sidebar = Sidebar(
            self.root,
            self.show_page
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        #################################################
        # Main Frame
        #################################################

        self.main = ctk.CTkFrame(
            self.root,
            corner_radius=0
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.main.grid_rowconfigure(1, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        #################################################
        # Header
        #################################################

        self.header = Header(
            self.main,
            self.username
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        #################################################
        # Content Area
        #################################################

        self.content = ctk.CTkFrame(
            self.main
        )

        self.content.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        #################################################
        # Default Page
        #################################################

        self.show_page("Dashboard")

    # --------------------------------------------------
    # Page Navigation
    # --------------------------------------------------

    def show_page(self, page_name):

        if self.current_page is not None:
            self.current_page.destroy()

        if page_name == "Dashboard":

            self.current_page = DashboardPage(
                self.content
            )

        elif page_name == "Students":

            self.current_page = StudentListPage(
                self.content
            )

        elif page_name == "Faculty":

            self.current_page = FacultyListPage(
                self.content
            )

        elif page_name == "Attendance":

            self.current_page = AttendancePage(
                self.content
            )

        elif page_name == "Fees":

            self.current_page = FeePage(
                self.content
            )

        elif page_name == "Courses":

            self.current_page = CourseListPage(
                self.content
            )

        elif page_name == "Reports":

            self.current_page = ReportsPage(
                self.content
            )

        else:

            self.current_page = ctk.CTkFrame(
                self.content
            )

            label = ctk.CTkLabel(
                self.current_page,
                text=f"{page_name}\nComing Soon",
                font=("Arial", 24, "bold")
            )

            label.pack(expand=True)

        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )