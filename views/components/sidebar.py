import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):

        super().__init__(
            parent,
            width=220,
            corner_radius=0
        )

        self.callback = callback

        self.pack_propagate(False)

        self.build_sidebar()

    def build_sidebar(self):

        title = ctk.CTkLabel(
            self,
            text="🎓\n\nStudent\nManagement\nSystem",
            font=("Arial", 24, "bold"),
            justify="center"
        )

        title.pack(pady=30)

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

        for item in menu_items:

            button = ctk.CTkButton(
                self,
                text=item,
                width=180,
                command=lambda page=item: self.callback(page)
            )

            button.pack(pady=6)