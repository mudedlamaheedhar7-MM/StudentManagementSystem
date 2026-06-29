import customtkinter as ctk

from config import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    THEME,
    COLOR_THEME
)

from database.mongodb import mongodb
from views.login import LoginWindow


def main():

    # Connect to MongoDB
    mongodb.connect()

    # Set application theme
    ctk.set_appearance_mode(THEME)
    ctk.set_default_color_theme(COLOR_THEME)

    # Create main window
    app = ctk.CTk()

    app.title(APP_NAME)
    app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # Open Login Screen
    LoginWindow(app)

    app.mainloop()


if __name__ == "__main__":
    main()