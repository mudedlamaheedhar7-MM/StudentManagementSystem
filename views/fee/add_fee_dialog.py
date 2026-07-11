import customtkinter as ctk
from tkinter import messagebox

from models.fee import Fee
from controllers.fee_controller import FeeController
from controllers.student_controller import StudentController


class AddFeeDialog(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.title("Add New Fee")
        self.geometry("720x820")
        self.resizable(False, False)

        self.grab_set()

        # Load students
        self.students = StudentController.get_all_students()
        self.student_map = {}

        self.build()

    # --------------------------------------------------
    # Build UI
    # --------------------------------------------------

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Add New Fee",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        #################################################
        # Scrollable Form
        #################################################

        form = ctk.CTkScrollableFrame(
            self,
            width=650,
            height=620
        )

        form.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        #################################################
        # Fee ID
        #################################################

        ctk.CTkLabel(
            form,
            text="Fee ID"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.fee_id = FeeController.generate_fee_id()

        self.fee_id_entry = ctk.CTkEntry(form)

        self.fee_id_entry.pack(
            fill="x",
            padx=20
        )

        self.fee_id_entry.insert(
            0,
            self.fee_id
        )

        self.fee_id_entry.configure(
            state="disabled"
        )

        #################################################
        # Student
        #################################################

        ctk.CTkLabel(
            form,
            text="Student"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        student_values = []

        for student in self.students:

            display = (
                f'{student["student_id"]} - '
                f'{student["first_name"]} '
                f'{student["last_name"]}'
            )

            student_values.append(display)

            self.student_map[display] = student

        self.student_combo = ctk.CTkComboBox(
            form,
            values=student_values,
            command=self.student_selected
        )

        self.student_combo.pack(
            fill="x",
            padx=20
        )

        #################################################
        # Student Name
        #################################################

        ctk.CTkLabel(
            form,
            text="Student Name"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.student_name_entry = ctk.CTkEntry(form)

        self.student_name_entry.pack(
            fill="x",
            padx=20
        )

        self.student_name_entry.configure(
            state="disabled"
        )

        #################################################
        # Course
        #################################################

        ctk.CTkLabel(
            form,
            text="Course"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.course_entry = ctk.CTkEntry(form)

        self.course_entry.pack(
            fill="x",
            padx=20
        )

        self.course_entry.configure(
            state="disabled"
        )

        #################################################
        # Department
        #################################################

        ctk.CTkLabel(
            form,
            text="Department"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.department_entry = ctk.CTkEntry(form)

        self.department_entry.pack(
            fill="x",
            padx=20
        )

        self.department_entry.configure(
            state="disabled"
        )

        #################################################
        # Total Fee
        #################################################

        ctk.CTkLabel(
            form,
            text="Total Fee"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.total_fee_entry = ctk.CTkEntry(form)

        self.total_fee_entry.pack(
            fill="x",
            padx=20
        )

        self.total_fee_entry.bind(
            "<KeyRelease>",
            self.calculate_balance
        )
                #################################################
        # Amount Paid
        #################################################

        ctk.CTkLabel(
            form,
            text="Amount Paid"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.amount_paid_entry = ctk.CTkEntry(form)

        self.amount_paid_entry.pack(
            fill="x",
            padx=20
        )

        self.amount_paid_entry.insert(0, "0")

        self.amount_paid_entry.bind(
            "<KeyRelease>",
            self.calculate_balance
        )

        #################################################
        # Balance
        #################################################

        ctk.CTkLabel(
            form,
            text="Balance"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.balance_entry = ctk.CTkEntry(form)

        self.balance_entry.pack(
            fill="x",
            padx=20
        )

        self.balance_entry.insert(
            0,
            "0"
        )

        self.balance_entry.configure(
            state="disabled"
        )

        #################################################
        # Due Date
        #################################################

        ctk.CTkLabel(
            form,
            text="Due Date (YYYY-MM-DD)"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.due_date_entry = ctk.CTkEntry(form)

        self.due_date_entry.pack(
            fill="x",
            padx=20
        )

        #################################################
        # Status
        #################################################

        ctk.CTkLabel(
            form,
            text="Status"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.status_combo = ctk.CTkComboBox(
            form,
            values=[
                "Pending",
                "Partial",
                "Paid"
            ]
        )

        self.status_combo.set("Pending")

        self.status_combo.pack(
            fill="x",
            padx=20
        )

        #################################################
        # Remarks
        #################################################

        ctk.CTkLabel(
            form,
            text="Remarks"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.remarks_entry = ctk.CTkEntry(form)

        self.remarks_entry.pack(
            fill="x",
            padx=20
        )

        #################################################
        # Save Button
        #################################################

        save_btn = ctk.CTkButton(
            self,
            text="💾 Save Fee",
            width=250,
            height=40,
            command=self.save_fee
        )

        save_btn.pack(
            pady=20
        )

    # --------------------------------------------------
    # Student Selected
    # --------------------------------------------------

    def student_selected(self, value):

        student = self.student_map.get(value)

        if not student:
            return

        self.student_name_entry.configure(state="normal")
        self.course_entry.configure(state="normal")
        self.department_entry.configure(state="normal")

        self.student_name_entry.delete(0, "end")
        self.course_entry.delete(0, "end")
        self.department_entry.delete(0, "end")

        self.student_name_entry.insert(
            0,
            f'{student["first_name"]} {student["last_name"]}'
        )

        self.course_entry.insert(
            0,
            student["course"]
        )

        self.department_entry.insert(
            0,
            student["department"]
        )

        self.student_name_entry.configure(state="disabled")
        self.course_entry.configure(state="disabled")
        self.department_entry.configure(state="disabled")

            # --------------------------------------------------
    # Auto Calculate Balance
    # --------------------------------------------------

    def calculate_balance(self, event=None):

        try:

            total = float(
                self.total_fee_entry.get() or 0
            )

            paid = float(
                self.amount_paid_entry.get() or 0
            )

            balance = total - paid

            if balance < 0:
                balance = 0

            self.balance_entry.configure(state="normal")

            self.balance_entry.delete(
                0,
                "end"
            )

            self.balance_entry.insert(
                0,
                str(balance)
            )

            self.balance_entry.configure(state="disabled")

            if paid <= 0:

                self.status_combo.set(
                    "Pending"
                )

            elif balance == 0:

                self.status_combo.set(
                    "Paid"
                )

            else:

                self.status_combo.set(
                    "Partial"
                )

        except ValueError:

            pass

    # --------------------------------------------------
    # Save Fee
    # --------------------------------------------------

    def save_fee(self):

        if self.student_combo.get() == "":

            messagebox.showwarning(
                "Validation",
                "Please select a student."
            )

            return

        if self.total_fee_entry.get().strip() == "":

            messagebox.showwarning(
                "Validation",
                "Please enter Total Fee."
            )

            return

        if self.due_date_entry.get().strip() == "":

            messagebox.showwarning(
                "Validation",
                "Please enter Due Date."
            )

            return

        student = self.student_map.get(
            self.student_combo.get()
        )

        if not student:

            messagebox.showerror(
                "Error",
                "Invalid student selected."
            )

            return

        try:

            fee = Fee(

                fee_id=self.fee_id,

                student_id=student["student_id"],

                student_name=f'{student["first_name"]} {student["last_name"]}',

                course=student["course"],

                department=student["department"],

                total_fee=float(
                    self.total_fee_entry.get()
                ),

                amount_paid=float(
                    self.amount_paid_entry.get() or 0
                ),

                balance=float(
                    self.balance_entry.get()
                ),

                due_date=self.due_date_entry.get(),

                status=self.status_combo.get(),

                remarks=self.remarks_entry.get()

            )

            saved = FeeController.save_fee(
                fee
            )

            if saved:

                messagebox.showinfo(
                    "Success",
                    "Fee record added successfully!"
                )

                self.parent.load_fees()

                self.destroy()

            else:

                messagebox.showerror(
                    "Duplicate",
                    "Fee ID already exists."
                )

        except Exception as error:

            import traceback

            traceback.print_exc()

            messagebox.showerror(
                "Error",
                str(error)
            )