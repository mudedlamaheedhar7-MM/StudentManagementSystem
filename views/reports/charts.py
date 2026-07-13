import os
import matplotlib.pyplot as plt


class ChartGenerator:

    # ==================================================
    # Common Chart Style
    # ==================================================

    @staticmethod
    def setup():

        plt.style.use("ggplot")

    # ==================================================
    # Save Chart
    # ==================================================

    @staticmethod
    def save_chart(filename):

        folder = os.path.join(
            "exports",
            "charts"
        )

        os.makedirs(
            folder,
            exist_ok=True
        )

        path = os.path.join(
            folder,
            filename
        )

        plt.tight_layout()

        plt.savefig(
            path,
            dpi=150,
            bbox_inches="tight"
        )

        plt.close()

        return path

    # ==================================================
    # Attendance Pie Chart
    # ==================================================

    @staticmethod
    def attendance_chart(summary):

        ChartGenerator.setup()

        labels = [
            "Present",
            "Absent",
            "Late"
        ]

        values = [
            summary.get("present", 0),
            summary.get("absent", 0),
            summary.get("late", 0)
        ]

        # Prevent matplotlib crash if all values are zero
        if sum(values) == 0:
            values = [1, 1, 1]

        plt.figure(figsize=(6, 6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.axis("equal")

        plt.title(
            "Attendance Distribution",
            fontsize=14,
            fontweight="bold"
        )

        return ChartGenerator.save_chart(
            "attendance_pie.png"
        )

    # ==================================================
    # Fee Pie Chart
    # ==================================================

    @staticmethod
    def fee_chart(summary):

        ChartGenerator.setup()

        labels = [
            "Paid",
            "Partial",
            "Pending"
        ]

        values = [
            summary.get("paid", 0),
            summary.get("partial", 0),
            summary.get("pending", 0)
        ]

        # Prevent matplotlib crash if all values are zero
        if sum(values) == 0:
            values = [1, 1, 1]

        plt.figure(figsize=(6, 6))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.axis("equal")

        plt.title(
            "Fee Status Distribution",
            fontsize=14,
            fontweight="bold"
        )

        return ChartGenerator.save_chart(
            "fee_pie.png"
        )

    # ==================================================
    # Students by Department
    # ==================================================

    @staticmethod
    def department_chart(data):

        ChartGenerator.setup()

        if not data:

            data = {
                "No Data": 0
            }

        departments = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(7, 5))

        plt.bar(
            departments,
            values
        )

        plt.title(
            "Students by Department",
            fontsize=14,
            fontweight="bold"
        )

        plt.xlabel("Department")
        plt.ylabel("Students")

        plt.xticks(rotation=30)

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        return ChartGenerator.save_chart(
            "department_chart.png"
        )

    # ==================================================
    # Courses by Department
    # ==================================================

    @staticmethod
    def course_chart(data):

        ChartGenerator.setup()

        if not data:

            data = {
                "No Data": 0
            }

        departments = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(7, 5))

        plt.bar(
            departments,
            values
        )

        plt.title(
            "Courses by Department",
            fontsize=14,
            fontweight="bold"
        )

        plt.xlabel("Department")
        plt.ylabel("Courses")

        plt.xticks(rotation=30)

        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        return ChartGenerator.save_chart(
            "course_chart.png"
        )