import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(self, parent, title, value):

        super().__init__(
            parent,
            width=220,
            height=140,
            corner_radius=15
        )

        self.title = title
        self.value = value

        self.grid_propagate(False)

        self.build_card()

    def build_card(self):

        title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=("Arial", 18, "bold")
        )

        title_label.pack(pady=(20, 10))

        self.value_label = ctk.CTkLabel(
            self,
            text=self.value,
            font=("Arial", 32)
        )

        self.value_label.pack()

    def update_value(self, new_value):

        self.value = new_value
        self.value_label.configure(text=new_value)