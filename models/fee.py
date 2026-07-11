class Fee:

    def __init__(
        self,
        fee_id,
        student_id,
        student_name,
        course,
        department,
        total_fee,
        amount_paid,
        balance,
        due_date,
        status,
        remarks=""
    ):

        self.fee_id = fee_id
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.department = department
        self.total_fee = float(total_fee)
        self.amount_paid = float(amount_paid)
        self.balance = float(balance)
        self.due_date = due_date
        self.status = status
        self.remarks = remarks

    # --------------------------------------------------
    # Convert Object to Dictionary
    # --------------------------------------------------

    def to_dict(self):

        return {

            "fee_id": self.fee_id,

            "student_id": self.student_id,

            "student_name": self.student_name,

            "course": self.course,

            "department": self.department,

            "total_fee": self.total_fee,

            "amount_paid": self.amount_paid,

            "balance": self.balance,

            "due_date": self.due_date,

            "status": self.status,

            "remarks": self.remarks
        }