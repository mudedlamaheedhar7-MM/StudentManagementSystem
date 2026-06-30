import customtkinter as ctk


class StudentListPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Student List",
            font=("Arial", 24, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        message = ctk.CTkLabel(
            self,
            text="No students loaded yet.",
            font=("Arial", 16)
        )

        message.pack(pady=30)