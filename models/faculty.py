from dataclasses import dataclass, asdict


@dataclass
class Faculty:

    faculty_id: str
    employee_id: str

    first_name: str
    last_name: str

    gender: str

    phone: str
    email: str

    department: str

    designation: str

    qualification: str

    experience: int

    salary: float

    status: str = "Active"

    def to_dict(self):
        return asdict(self)