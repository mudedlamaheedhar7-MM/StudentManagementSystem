import customtkinter as ctk


class DashboardWindow:

    def __init__(self, root, username):

        self.root = root
        self.username = username

        self.create_dashboard()

    def create_dashboard(self):

        # Clear Login Screen
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Student Management System - Dashboard")

        ###################################################
        # Configure Grid
        ###################################################

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        ###################################################
        # Sidebar
        ###################################################

        sidebar = ctk.CTkFrame(
            self.root,
            width=220,
            corner_radius=0
        )

        sidebar.grid(row=0, column=0, sticky="ns")

        title = ctk.CTkLabel(
            sidebar,
            text="🎓\nStudent\nManagement",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=30)

        menu = [
            "Dashboard",
            "Students",
            "Faculty",
            "Attendance",
            "Fees",
            "Courses",
            "Reports",
            "Settings"
        ]

        for item in menu:

            button = ctk.CTkButton(
                sidebar,
                text=item,
                width=180
            )

            button.pack(pady=8)

        ###################################################
        # Main Area
        ###################################################

        main = ctk.CTkFrame(
            self.root,
            corner_radius=0
        )

        main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        ###################################################
        # Header
        ###################################################

        header = ctk.CTkFrame(
            main,
            height=70
        )

        header.pack(fill="x")

        welcome = ctk.CTkLabel(
            header,
            text=f"Welcome, {self.username}",
            font=("Arial", 22, "bold")
        )

        welcome.pack(
            side="left",
            padx=20,
            pady=20
        )

        logout = ctk.CTkButton(
            header,
            text="Logout",
            width=100
        )

        logout.pack(
            side="right",
            padx=20
        )

        ###################################################
        # Statistics
        ###################################################

        cards = ctk.CTkFrame(main)

        cards.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        titles = [
            "Students",
            "Faculty",
            "Courses",
            "Pending Fees"
        ]

        for index, title in enumerate(titles):

            card = ctk.CTkFrame(
                cards,
                width=220,
                height=150
            )

            card.grid(
                row=0,
                column=index,
                padx=10,
                pady=10
            )

            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Arial",18,"bold")
            ).pack(pady=20)

            ctk.CTkLabel(
                card,
                text="0",
                font=("Arial",32)
            ).pack()