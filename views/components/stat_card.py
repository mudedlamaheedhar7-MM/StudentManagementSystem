import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        title,
        value,
        icon="📊",
        accent="#3B82F6",
        width=220,
        height=140
    ):

        super().__init__(
            parent,
            width=width,
            height=height,
            corner_radius=18,
            border_width=1,
            border_color="#D1D5DB"
        )

        self.title = title
        self.value = str(value)
        self.icon = icon
        self.accent = accent

        self.pack_propagate(False)

        self.build_card()

    # --------------------------------------------------

    def build_card(self):

        #################################################
        # Accent Bar
        #################################################

        accent_bar = ctk.CTkFrame(
            self,
            height=6,
            fg_color=self.accent,
            corner_radius=20
        )

        accent_bar.pack(
            fill="x",
            padx=10,
            pady=(10, 5)
        )

        #################################################
        # Icon
        #################################################

        self.icon_label = ctk.CTkLabel(
            self,
            text=self.icon,
            font=("Arial", 28)
        )

        self.icon_label.pack(
            pady=(5, 5)
        )

        #################################################
        # Value
        #################################################

        self.value_label = ctk.CTkLabel(
            self,
            text=self.value,
            font=("Arial", 32, "bold")
        )

        self.value_label.pack()

        #################################################
        # Title
        #################################################

        self.title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=("Arial", 15)
        )

        self.title_label.pack(
            pady=(5, 15)
        )

    # --------------------------------------------------

    def update_value(self, value):

        self.value = str(value)

        self.value_label.configure(
            text=self.value
        )

    # --------------------------------------------------

    def update_title(self, title):

        self.title = title

        self.title_label.configure(
            text=self.title
        )

    # --------------------------------------------------

    def update_icon(self, icon):

        self.icon = icon

        self.icon_label.configure(
            text=self.icon
        )