from dataclasses import dataclass, asdict


@dataclass
class Course:

    course_id: str

    course_name: str

    department: str

    semester: int

    credits: int

    duration: str

    description: str = ""

    status: str = "Active"

    def to_dict(self):
        return asdict(self)