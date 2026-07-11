import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):

        super().__init__(
            parent,
            width=260,
            corner_radius=0
        )

        self.callback = callback

        # Keep sidebar at a fixed width
        self.grid_propagate(False)

        self.build_sidebar()

    # --------------------------------------------------
    # Build Sidebar
    # --------------------------------------------------

    def build_sidebar(self):

        title = ctk.CTkLabel(
            self,
            text="🎓\n\nStudent\nManagement\nSystem",
            font=("Arial", 24, "bold"),
            justify="center"
        )

        title.pack(
            pady=(30, 40)
        )

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
                width=220,
                height=40,
                command=lambda page=item: self.callback(page)
            )

            button.pack(
                padx=20,
                pady=6,
                fill="x"
            )