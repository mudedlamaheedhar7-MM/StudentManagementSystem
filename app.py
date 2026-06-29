from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["student_management_system"]

print("MongoDB Connected Successfully!")

import customtkinter as ctk

from config import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    THEME,
    COLOR_THEME
)

from database.mongodb import mongodb


def main():

    # Connect to MongoDB
    mongodb.connect()

    # Theme
    ctk.set_appearance_mode(THEME)
    ctk.set_default_color_theme(COLOR_THEME)

    # Main Window
    app = ctk.CTk()

    app.title(APP_NAME)
    app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    label = ctk.CTkLabel(
        app,
        text="Student Management System",
        font=("Arial", 28, "bold")
    )

    label.pack(pady=80)

    app.mainloop()


if __name__ == "__main__":
    main()