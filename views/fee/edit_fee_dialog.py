import customtkinter as ctk
from tkinter import messagebox

from models.fee import Fee
from controllers.fee_controller import FeeController


class EditFeeDialog(ctk.CTkToplevel):

    def __init__(self, parent, fee_id):
        super().__init__(parent)

        self.parent = parent
        self.fee_id = fee_id

        self.title("Edit Fee")
        self.geometry("700x750")
        self.resizable(False, False)

        self.grab_set()

        self.fee = FeeController.get_fee_by_id(fee_id)

        if not self.fee:
            messagebox.showerror(
                "Error",
                "Fee record not found."
            )
            self.destroy()
            return

        self.build()

    # --------------------------------------------------

    def build(self):
        title = ctk.CTkLabel(
            self,
            text="Edit Fee",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        form = ctk.CTkFrame(self)
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

        self.fee_id_entry = ctk.CTkEntry(form)
        self.fee_id_entry.pack(fill="x", padx=20)
        self.fee_id_entry.insert(0, self.fee["fee_id"])
        self.fee_id_entry.configure(state="disabled")

        #################################################
        # Student ID
        #################################################
        ctk.CTkLabel(
            form,
            text="Student ID"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.student_id_entry = ctk.CTkEntry(form)
        self.student_id_entry.pack(fill="x", padx=20)
        self.student_id_entry.insert(0, self.fee["student_id"])
        self.student_id_entry.configure(state="disabled")

        #################################################
        # Student Name
        #################################################
        ctk.CTkLabel(
            form,
            text="Student Name"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.student_name_entry = ctk.CTkEntry(form)
        self.student_name_entry.pack(fill="x", padx=20)
        self.student_name_entry.insert(0, self.fee["student_name"])
        self.student_name_entry.configure(state="disabled")

        #################################################
        # Course
        #################################################
        ctk.CTkLabel(
            form,
            text="Course"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.course_entry = ctk.CTkEntry(form)
        self.course_entry.pack(fill="x", padx=20)
        self.course_entry.insert(0, self.fee["course"])
        self.course_entry.configure(state="disabled")

        #################################################
        # Department
        #################################################
        ctk.CTkLabel(
            form,
            text="Department"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.department_entry = ctk.CTkEntry(form)
        self.department_entry.pack(fill="x", padx=20)
        self.department_entry.insert(0, self.fee["department"])
        self.department_entry.configure(state="disabled")

        #################################################
        # Total Fee
        #################################################
        ctk.CTkLabel(
            form,
            text="Total Fee"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.total_fee_entry = ctk.CTkEntry(form)
        self.total_fee_entry.pack(fill="x", padx=20)
        self.total_fee_entry.insert(0, str(self.fee["total_fee"]))
        self.total_fee_entry.configure(state="disabled")

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
        self.amount_paid_entry.insert(0, str(self.fee["amount_paid"]))
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
        self.balance_entry.insert(0, str(self.fee["balance"]))

        #################################################
        # Due Date
        #################################################
        ctk.CTkLabel(
            form,
            text="Due Date"
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.due_date_entry = ctk.CTkEntry(form)
        self.due_date_entry.pack(
            fill="x",
            padx=20
        )
        self.due_date_entry.insert(0, self.fee["due_date"])

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
        self.status_combo.pack(
            fill="x",
            padx=20
        )
        self.status_combo.set(self.fee["status"])

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
        self.remarks_entry.insert(0, self.fee["remarks"])

        #################################################
        # Update Button
        #################################################
        update_btn = ctk.CTkButton(
            self,
            text="💾 Update Fee",
            command=self.update_fee
        )
        update_btn.pack(pady=20)

    # --------------------------------------------------
    # Auto Calculate Balance
    # --------------------------------------------------

    def calculate_balance(self, event=None):
        try:
            total = float(self.total_fee_entry.get())
            paid = float(self.amount_paid_entry.get())

            balance = total - paid

            self.balance_entry.delete(0, "end")
            self.balance_entry.insert(0, str(balance))

            if paid <= 0:
                self.status_combo.set("Pending")
            elif paid >= total:
                self.status_combo.set("Paid")
            else:
                self.status_combo.set("Partial")

        except ValueError:
            pass

    # --------------------------------------------------
    # Update Fee
    # --------------------------------------------------

    def update_fee(self):
        try:
            fee = Fee(
                fee_id=self.fee["fee_id"],
                student_id=self.fee["student_id"],
                student_name=self.fee["student_name"],
                course=self.fee["course"],
                department=self.fee["department"],
                total_fee=float(self.total_fee_entry.get()),
                amount_paid=float(self.amount_paid_entry.get()),
                balance=float(self.balance_entry.get()),
                due_date=self.due_date_entry.get(),
                status=self.status_combo.get(),
                remarks=self.remarks_entry.get()
            )

            updated = FeeController.update_fee(fee)

            if updated:
                messagebox.showinfo(
                    "Success",
                    "Fee updated successfully!"
                )
                self.parent.load_fees()
                self.destroy()
            else:
                messagebox.showwarning(
                    "No Changes",
                    "No changes were made."
                )

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )