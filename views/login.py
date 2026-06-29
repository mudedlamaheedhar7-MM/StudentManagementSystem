import customtkinter as ctk


class LoginWindow:

    def __init__(self, root):
        self.root = root
        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self.root,
            text="Student Management System",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(40, 20))

        self.username = ctk.CTkEntry(
            self.root,
            width=300,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            self.root,
            width=300,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        login_button = ctk.CTkButton(
            self.root,
            text="Login",
            command=self.login
        )
        login_button.pack(pady=20)

    def login(self):
        print("Login button clicked")