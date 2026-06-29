from dataclasses import dataclass, asdict


@dataclass
class Student:

    student_id: str
    admission_no: str

    first_name: str
    last_name: str

    gender: str

    dob: str

    phone: str
    email: str

    address: str

    course: str
    department: str

    semester: int
    batch: str

    attendance: float = 0
    fees_due: float = 0

    status: str = "Active"

    def to_dict(self):
        return asdict(self)