from models.fee import Fee
from controllers.fee_controller import FeeController


fee = Fee(

    fee_id=FeeController.generate_fee_id(),

    student_id="SMS0001",

    student_name="Maheedhar Mudedla",

    course="BBA",

    department="HR",

    total_fee=120000,

    amount_paid=50000,

    balance=70000,

    due_date="2026-09-01",

    status="Partial",

    remarks="First Installment"

)

saved = FeeController.save_fee(fee)

print("Fee Saved:", saved)