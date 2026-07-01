import customtkinter as ctk
from tkinter import messagebox

from views.components.form_builder import FormBuilder


class AddStudentDialog(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.title("Add Student")
        self.geometry("650x650")
        self.resizable(False, False)

        self.grab_set()

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Add New Student",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        fields = [
            ("Admission No", "entry"),
            ("First Name", "entry"),
            ("Last Name", "entry"),
            ("Gender", "combo", ["Male", "Female", "Other"]),
            ("Phone", "entry"),
            ("Email", "entry"),
            ("Course", "combo", ["BBA", "BCA", "MBA"]),
            ("Department", "combo", ["HR", "Finance", "Marketing"]),
            ("Semester", "combo", ["1", "2", "3", "4", "5", "6"]),
            ("Batch", "entry")
        ]

        self.fields = FormBuilder.create_form(
            self,
            fields
        )

        save_btn = ctk.CTkButton(
            self,
            text="💾 Save Student",
            command=self.save_student
        )

        save_btn.pack(pady=20)

    def save_student(self):

        data = {}

        for label, widget in self.fields.items():
            data[label] = widget.get()

        print("Student Data")

        for key, value in data.items():
            print(f"{key}: {value}")

        messagebox.showinfo(
            "Success",
            "Form captured successfully!\n\nDatabase connection comes next."
        )