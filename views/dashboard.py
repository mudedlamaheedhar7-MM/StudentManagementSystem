import customtkinter as ctk

from views.components.sidebar import Sidebar
from views.components.header import Header
from views.components.stat_card import StatCard


class DashboardWindow:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.build_dashboard()

    def build_dashboard(self):

        # Remove Login Screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Student Management System")

        ##################################################
        # Root Grid
        ##################################################

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        ##################################################
        # Sidebar
        ##################################################

        self.sidebar = Sidebar(self.root)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        ##################################################
        # Main Frame
        ##################################################

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

        ##################################################
        # Header
        ##################################################

        self.header = Header(
            self.main,
            self.username
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        ##################################################
        # Dashboard Content
        ##################################################

        content = ctk.CTkFrame(
            self.main
        )

        content.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=20
        )

        ##################################################
        # Statistics Cards
        ##################################################

        content.grid_columnconfigure((0,1,2,3), weight=1)

        student_card = StatCard(
            content,
            "Students",
            "0"
        )

        faculty_card = StatCard(
            content,
            "Faculty",
            "0"
        )

        course_card = StatCard(
            content,
            "Courses",
            "0"
        )

        fee_card = StatCard(
            content,
            "Pending Fees",
            "₹0"
        )

        student_card.grid(row=0, column=0, padx=10, pady=10)
        faculty_card.grid(row=0, column=1, padx=10, pady=10)
        course_card.grid(row=0, column=2, padx=10, pady=10)
        fee_card.grid(row=0, column=3, padx=10, pady=10)