from dataclasses import dataclass, asdict


@dataclass
class Attendance:

    attendance_id: str

    student_id: str

    student_name: str

    course: str

    department: str

    date: str

    status: str

    def to_dict(self):
        return asdict(self)