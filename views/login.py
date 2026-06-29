from views.dashboard import DashboardWindow
import customtkinter as ctk
from tkinter import messagebox

from controllers.login_controller import LoginController


class LoginWindow:

    def __init__(self, root):
        self.root = root
        self.create_layout()

    def create_layout(self):

        # Configure window grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # ---------------- LEFT PANEL ----------------

        left = ctk.CTkFrame(self.root, corner_radius=0)
        left.grid(row=0, column=0, sticky="nsew")

        title = ctk.CTkLabel(
            left,
            text="🎓\n\nStudent Management\nSystem",
            font=("Arial", 30, "bold"),
            justify="center"
        )
        title.place(relx=0.5, rely=0.40, anchor="center")

        subtitle = ctk.CTkLabel(
            left,
            text="Institution Management Solution",
            font=("Arial", 16)
        )
        subtitle.place(relx=0.5, rely=0.60, anchor="center")

        # ---------------- RIGHT PANEL ----------------

        right = ctk.CTkFrame(self.root, corner_radius=0)
        right.grid(row=0, column=1, sticky="nsew")

        heading = ctk.CTkLabel(
            right,
            text="Welcome Back",
            font=("Arial", 28, "bold")
        )
        heading.pack(pady=(70, 40))

        self.username = ctk.CTkEntry(
            right,
            width=320,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            right,
            width=320,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        self.role = ctk.CTkComboBox(
            right,
            width=320,
            values=[
                "Admin",
                "Faculty",
                "Accountant",
                "Student"
            ]
        )

        self.role.set("Admin")
        self.role.pack(pady=10)

        login_button = ctk.CTkButton(
            right,
            width=320,
            text="LOGIN",
            command=self.login
        )

        login_button.pack(pady=30)

    def login(self):

        username = self.username.get().strip()
        password = self.password.get()
        role = self.role.get()

        authenticated = LoginController.authenticate(
            username,
            password,
            role
        )

        if authenticated:

            DashboardWindow(
            self.root,
            username
    )
            
            
        else:
            messagebox.showerror(
                "Login",
                "Invalid Username or Password"
            )