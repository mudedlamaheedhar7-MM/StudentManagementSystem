import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=220,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.build_sidebar()

    def build_sidebar(self):

        # Logo / Title
        title = ctk.CTkLabel(
            self,
            text="🎓\n\nStudent\nManagement\nSystem",
            font=("Arial", 24, "bold"),
            justify="center"
        )

        title.pack(pady=30)

        # Navigation Buttons
        menu_items = [
            "Dashboard",
            "Students",
            "Faculty",
            "Attendance",
            "Fees",
            "Courses",
            "Reports",
            "Settings"
        ]

        self.buttons = {}

        for item in menu_items:

            button = ctk.CTkButton(
                self,
                text=item,
                width=180,
                height=40
            )

            button.pack(pady=6)

            self.buttons[item] = button