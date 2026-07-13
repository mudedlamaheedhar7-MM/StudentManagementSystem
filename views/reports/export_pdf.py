import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)


class PDFExporter:

    # ==================================================
    # Export Folder
    # ==================================================

    @staticmethod
    def get_export_folder():
        folder = os.path.join(
            "exports",
            "pdf"
        )
        os.makedirs(
            folder,
            exist_ok=True
        )
        return folder

    # ==================================================
    # Styles
    # ==================================================

    @staticmethod
    def styles():
        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        title_style.alignment = TA_CENTER

        subtitle_style = styles["Heading2"]
        subtitle_style.alignment = TA_CENTER

        normal_style = styles["Normal"]

        return (
            title_style,
            subtitle_style,
            normal_style
        )

    # ==================================================
    # Generic PDF Generator
    # ==================================================

    @classmethod
    def generate_report(
        cls,
        report_title,
        headers,
        records,
        extractor,
        filename
    ):
        filepath = os.path.join(
            cls.get_export_folder(),
            filename
        )

        doc = SimpleDocTemplate(
            filepath,
            rightMargin=0.5 * inch,
            leftMargin=0.5 * inch,
            topMargin=0.5 * inch,
            bottomMargin=0.5 * inch
        )

        title_style, subtitle_style, normal_style = cls.styles()
        elements = []

        #################################################
        # Header
        #################################################

        elements.append(
            Paragraph(
                "STUDENT MANAGEMENT SYSTEM",
                title_style
            )
        )

        elements.append(
            Paragraph(
                report_title,
                subtitle_style
            )
        )

        elements.append(
            Paragraph(
                f"<b>Export Date:</b> "
                f"{datetime.now().strftime('%d-%m-%Y %H:%M')}",
                normal_style
            )
        )

        elements.append(Spacer(1, 20))

        #################################################
        # Table Data
        #################################################

        table_data = [headers]

        for record in records:
            table_data.append(
                extractor(record)
            )

        table = Table(
            table_data,
            repeatRows=1
        )

        table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#2563EB")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.black
                ),
                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.beige
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    8
                )
            ])
        )

        elements.append(table)
        doc.build(elements)

        return filepath

    # ==================================================
    # Export Students
    # ==================================================

    @classmethod
    def export_students(cls):
        from controllers.student_controller import StudentController

        headers = [
            "Student ID",
            "Admission No",
            "First Name",
            "Last Name",
            "Gender",
            "Course",
            "Department",
            "Semester",
            "Status"
        ]

        students = StudentController.get_all_students()

        def extractor(student):
            return [
                student.get("student_id", ""),
                student.get("admission_no", ""),
                student.get("first_name", ""),
                student.get("last_name", ""),
                student.get("gender", ""),
                student.get("course", ""),
                student.get("department", ""),
                str(student.get("semester", "")),
                student.get("status", "")
            ]

        return cls.generate_report(
            report_title="Student Report",
            headers=headers,
            records=students,
            extractor=extractor,
            filename="Students.pdf"
        )

    # ==================================================
    # Export Faculty
    # ==================================================

    @classmethod
    def export_faculty(cls):
        from controllers.faculty_controller import FacultyController

        headers = [
            "Faculty ID",
            "First Name",
            "Last Name",
            "Gender",
            "Department",
            "Qualification",
            "Email",
            "Status"
        ]

        faculty = FacultyController.get_all_faculty()

        def extractor(member):
            return [
                member.get("faculty_id", ""),
                member.get("first_name", ""),
                member.get("last_name", ""),
                member.get("gender", ""),
                member.get("department", ""),
                member.get("qualification", ""),
                member.get("email", ""),
                member.get("status", "")
            ]

        return cls.generate_report(
            report_title="Faculty Report",
            headers=headers,
            records=faculty,
            extractor=extractor,
            filename="Faculty.pdf"
        )

    # ==================================================
    # Export Courses
    # ==================================================

    @classmethod
    def export_courses(cls):
        from controllers.course_controller import CourseController

        headers = [
            "Course ID",
            "Course Name",
            "Department",
            "Semester",
            "Credits",
            "Duration",
            "Status"
        ]

        courses = CourseController.get_all_courses()

        def extractor(course):
            return [
                course.get("course_id", ""),
                course.get("course_name", ""),
                course.get("department", ""),
                str(course.get("semester", "")),
                str(course.get("credits", "")),
                course.get("duration", ""),
                course.get("status", "")
            ]

        return cls.generate_report(
            report_title="Course Report",
            headers=headers,
            records=courses,
            extractor=extractor,
            filename="Courses.pdf"
        )

    # ==================================================
    # Export Attendance
    # ==================================================

    @classmethod
    def export_attendance(cls):
        from controllers.attendance_controller import AttendanceController

        headers = [
            "Attendance ID",
            "Student ID",
            "Student Name",
            "Course",
            "Department",
            "Date",
            "Status"
        ]

        attendance = AttendanceController.get_all_attendance()

        def extractor(record):
            return [
                record.get("attendance_id", ""),
                record.get("student_id", ""),
                record.get("student_name", ""),
                record.get("course", ""),
                record.get("department", ""),
                record.get("date", ""),
                record.get("status", "")
            ]

        return cls.generate_report(
            report_title="Attendance Report",
            headers=headers,
            records=attendance,
            extractor=extractor,
            filename="Attendance.pdf"
        )

    # ==================================================
    # Export Fees
    # ==================================================

    @classmethod
    def export_fees(cls):
        from controllers.fee_controller import FeeController

        headers = [
            "Fee ID",
            "Student ID",
            "Student Name",
            "Course",
            "Department",
            "Total Fee",
            "Amount Paid",
            "Balance",
            "Due Date",
            "Status"
        ]

        fees = FeeController.get_all_fees()

        def extractor(fee):
            return [
                fee.get("fee_id", ""),
                fee.get("student_id", ""),
                fee.get("student_name", ""),
                fee.get("course", ""),
                fee.get("department", ""),
                str(fee.get("total_fee", "")),
                str(fee.get("amount_paid", "")),
                str(fee.get("balance", "")),
                fee.get("due_date", ""),
                fee.get("status", "")
            ]

        return cls.generate_report(
            report_title="Fee Report",
            headers=headers,
            records=fees,
            extractor=extractor,
            filename="Fees.pdf"
        )