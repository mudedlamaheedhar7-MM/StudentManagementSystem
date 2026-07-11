import customtkinter as ctk
from tkinter import ttk, messagebox

from controllers.fee_controller import FeeController
from views.fee.add_fee_dialog import AddFeeDialog
from views.fee.edit_fee_dialog import EditFeeDialog
from views.components.stat_card import StatCard


class FeePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.build()
        self.load_fees()

    # --------------------------------------------------
    # Build UI
    # --------------------------------------------------

    def build(self):

        #################################################
        # Title
        #################################################

        title = ctk.CTkLabel(
            self,
            text="Fee Management",
            font=("Arial", 24, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        #################################################
        # Summary Cards
        #################################################

        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.total_card = StatCard(
            cards_frame,
            title="Total",
            value="0",
            icon="💰",
            accent="#2563EB"
        )

        self.total_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        self.paid_card = StatCard(
            cards_frame,
            title="Paid",
            value="0",
            icon="🟢",
            accent="#16A34A"
        )

        self.paid_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        self.partial_card = StatCard(
            cards_frame,
            title="Partial",
            value="0",
            icon="🟡",
            accent="#F59E0B"
        )

        self.partial_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        self.pending_card = StatCard(
            cards_frame,
            title="Pending",
            value="0",
            icon="🔴",
            accent="#DC2626"
        )

        self.pending_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8
        )

        #################################################
        # Toolbar
        #################################################

        top_frame = ctk.CTkFrame(self)

        top_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.search_entry = ctk.CTkEntry(
            top_frame,
            width=280,
            placeholder_text="Search Fees..."
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.live_search
        )

        refresh_btn = ctk.CTkButton(
            top_frame,
            text="Refresh",
            command=self.load_fees
        )

        refresh_btn.pack(
            side="right",
            padx=5
        )

        add_btn = ctk.CTkButton(
            top_frame,
            text="➕ Add Fee",
            command=self.open_add_dialog
        )

        add_btn.pack(
            side="right",
            padx=5
        )

        delete_btn = ctk.CTkButton(
            top_frame,
            text="🗑 Delete",
            fg_color="red",
            hover_color="darkred",
            command=self.delete_fee
        )

        delete_btn.pack(
            side="right",
            padx=5
        )

        #################################################
        # Table Style
        #################################################

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 11, "bold")
        )

        #################################################
        # Table
        #################################################

        columns = (
            "fee_id",
            "student_id",
            "student_name",
            "course",
            "department",
            "total_fee",
            "amount_paid",
            "balance",
            "due_date",
            "status"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=18
        )

        headings = {
            "fee_id": "Fee ID",
            "student_id": "Student ID",
            "student_name": "Student Name",
            "course": "Course",
            "department": "Department",
            "total_fee": "Total Fee",
            "amount_paid": "Amount Paid",
            "balance": "Balance",
            "due_date": "Due Date",
            "status": "Status"
        }

        for key, value in headings.items():

            self.table.heading(
                key,
                text=value
            )

            self.table.column(
                key,
                width=130,
                anchor="center"
            )

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.table.bind(
            "<Double-1>",
            self.on_double_click
        )

    # --------------------------------------------------
    # Populate Table
    # --------------------------------------------------

    def populate_table(self, fees):

        for row in self.table.get_children():
            self.table.delete(row)

        for fee in fees:

            self.table.insert(
                "",
                "end",
                values=(
                    fee["fee_id"],
                    fee["student_id"],
                    fee["student_name"],
                    fee["course"],
                    fee["department"],
                    fee["total_fee"],
                    fee["amount_paid"],
                    fee["balance"],
                    fee["due_date"],
                    fee["status"]
                )
            )

    # --------------------------------------------------
    # Update Summary Cards
    # --------------------------------------------------

    def update_summary(self, fees):

        total = len(fees)

        paid = 0
        partial = 0
        pending = 0

        for fee in fees:

            status = fee["status"]

            if status == "Paid":
                paid += 1

            elif status == "Partial":
                partial += 1

            elif status == "Pending":
                pending += 1

        self.total_card.update_value(str(total))
        self.paid_card.update_value(str(paid))
        self.partial_card.update_value(str(partial))
        self.pending_card.update_value(str(pending))

    # --------------------------------------------------
    # Load Fees
    # --------------------------------------------------

    def load_fees(self):

        fees = FeeController.get_all_fees()

        self.populate_table(fees)
        self.update_summary(fees)

    # --------------------------------------------------
    # Live Search
    # --------------------------------------------------

    def live_search(self, event=None):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_fees()
            return

        fees = FeeController.search_fees(keyword)

        self.populate_table(fees)
        self.update_summary(fees)

    # --------------------------------------------------
    # Add Fee
    # --------------------------------------------------

    def open_add_dialog(self):

        AddFeeDialog(self)

    # --------------------------------------------------
    # Delete Fee
    # --------------------------------------------------

    def delete_fee(self):

        selected = self.table.focus()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a fee record."
            )

            return

        values = self.table.item(selected)["values"]

        fee_id = values[0]

        confirm = messagebox.askyesno(
            "Delete Fee",
            f"Are you sure you want to delete\n\n{fee_id}?"
        )

        if not confirm:
            return

        deleted = FeeController.delete_fee(fee_id)

        if deleted:

            messagebox.showinfo(
                "Success",
                "Fee record deleted successfully!"
            )

            self.load_fees()

        else:

            messagebox.showerror(
                "Error",
                "Failed to delete fee record."
            )

    # --------------------------------------------------
    # Edit Fee
    # --------------------------------------------------

    def on_double_click(self, event):

        selected = self.table.focus()

        if not selected:
            return

        values = self.table.item(selected)["values"]

        fee_id = values[0]

        EditFeeDialog(
            self,
            fee_id
    )