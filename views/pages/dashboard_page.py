import customtkinter as ctk

from views.components.stat_card import StatCard


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Dashboard Overview",
            font=("Arial", 24, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        cards = ctk.CTkFrame(self)
        cards.pack(fill="x", padx=20, pady=20)

        student = StatCard(cards, "Students", "0")
        faculty = StatCard(cards, "Faculty", "0")
        course = StatCard(cards, "Courses", "0")
        fees = StatCard(cards, "Pending Fees", "₹0")

        student.grid(row=0, column=0, padx=10)
        faculty.grid(row=0, column=1, padx=10)
        course.grid(row=0, column=2, padx=10)
        fees.grid(row=0, column=3, padx=10)