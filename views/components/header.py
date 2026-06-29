import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, parent, username):

        super().__init__(
            parent,
            height=70,
            corner_radius=0
        )

        self.username = username

        self.pack_propagate(False)

        self.build_header()

    def build_header(self):

        # Left Side
        left_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        left_frame.pack(
            side="left",
            padx=20,
            pady=10
        )

        title = ctk.CTkLabel(
            left_frame,
            text="Student Management System",
            font=("Arial", 22, "bold")
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            left_frame,
            text="Dashboard",
            font=("Arial", 14)
        )

        subtitle.pack(anchor="w")

        # Right Side
        right_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        right_frame.pack(
            side="right",
            padx=20,
            pady=10
        )

        welcome = ctk.CTkLabel(
            right_frame,
            text=f"Welcome, {self.username}",
            font=("Arial", 16)
        )

        welcome.pack(side="left", padx=10)

        logout_button = ctk.CTkButton(
            right_frame,
            text="Logout",
            width=100
        )

        logout_button.pack(side="left")