import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

from controllers.report_controller import ReportController
from views.components.stat_card import StatCard
from views.reports.export_excel import ExcelExporter
from views.reports.export_pdf import PDFExporter
from views.reports.charts import ChartGenerator
import os


class ReportsPage(ctk.CTkScrollableFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.build()

        self.load_dashboard()

    # --------------------------------------------------
    # Build UI
    # --------------------------------------------------

    def build(self):

        #################################################
        # Title
        #################################################

        title = ctk.CTkLabel(
            self,
            text="Reports & Analytics",
            font=("Arial", 28, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        #################################################
        # Summary Cards
        #################################################

        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.student_card = StatCard(
            cards,
            title="Students",
            value="0",
            icon="🎓",
            accent="#2563EB"
        )

        self.student_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        self.faculty_card = StatCard(
            cards,
            title="Faculty",
            value="0",
            icon="👨‍🏫",
            accent="#16A34A"
        )

        self.faculty_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        self.course_card = StatCard(
            cards,
            title="Courses",
            value="0",
            icon="📚",
            accent="#9333EA"
        )

        self.course_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        self.fee_card = StatCard(
            cards,
            title="Fees",
            value="0",
            icon="💰",
            accent="#F59E0B"
        )

        self.fee_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        self.attendance_card = StatCard(
            cards,
            title="Attendance",
            value="0",
            icon="✅",
            accent="#DC2626"
        )

        self.attendance_card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        #################################################
        # Attendance Summary
        #################################################

        attendance_frame = ctk.CTkFrame(self)

        attendance_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            attendance_frame,
            text="Attendance Summary",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        self.present_label = ctk.CTkLabel(
            attendance_frame,
            text="🟢 Present : 0",
            font=("Arial", 18)
        )

        self.present_label.pack(
            anchor="w",
            padx=30,
            pady=3
        )

        self.absent_label = ctk.CTkLabel(
            attendance_frame,
            text="🔴 Absent : 0",
            font=("Arial", 18)
        )

        self.absent_label.pack(
            anchor="w",
            padx=30,
            pady=3
        )

        self.late_label = ctk.CTkLabel(
            attendance_frame,
            text="🟡 Late : 0",
            font=("Arial", 18)
        )

        self.late_label.pack(
            anchor="w",
            padx=30,
            pady=(3, 15)
        )

        #################################################
        # Fee Summary
        #################################################

        fee_frame = ctk.CTkFrame(self)

        fee_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        ctk.CTkLabel(
            fee_frame,
            text="Fee Summary",
            font=("Arial", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        self.paid_label = ctk.CTkLabel(
            fee_frame,
            text="🟢 Paid : 0",
            font=("Arial", 18)
        )

        self.paid_label.pack(
            anchor="w",
            padx=30,
            pady=3
        )

        self.partial_label = ctk.CTkLabel(
            fee_frame,
            text="🟡 Partial : 0",
            font=("Arial", 18)
        )

        self.partial_label.pack(
            anchor="w",
            padx=30,
            pady=3
        )

        self.pending_label = ctk.CTkLabel(
            fee_frame,
            text="🔴 Pending : 0",
            font=("Arial", 18)
        )

        self.pending_label.pack(
            anchor="w",
            padx=30,
            pady=(3, 15)
        )

        #################################################
        # Analytics Dashboard
        #################################################

        self.analytics_frame = ctk.CTkFrame(self)

        self.analytics_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.analytics_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.analytics_frame.grid_columnconfigure(
            1,
            weight=1
        )

        self.analytics_frame.grid_rowconfigure(
            1,
            weight=1
        )

        self.analytics_frame.grid_rowconfigure(
            2,
            weight=1
        )

        analytics_title = ctk.CTkLabel(
            self.analytics_frame,
            text="Analytics Dashboard",
            font=("Arial", 22, "bold")
        )

        analytics_title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15, 20)
        )

        self.chart1 = ctk.CTkLabel(
            self.analytics_frame,
            text="",
            width=450,
            height=340
        )
        

        self.chart1.grid(
            row=1,
            column=0,
            padx=30,
            pady=30,
            sticky="n"
        )

        self.chart2 = ctk.CTkLabel(
            self.analytics_frame,
            text="",
            width=450,
            height=340

        )

        self.chart2.grid(
            row=1,
            column=1,
            padx=30,
            pady=30,
            sticky="n"
        )

        self.chart3 = ctk.CTkLabel(
            self.analytics_frame,
            text="",
            width=450,
            height=340
        )

        self.chart3.grid(
            row=2,
            column=0,
            padx=30,
            pady=30,
            sticky="n"
        )

        self.chart4 = ctk.CTkLabel(
            self.analytics_frame,
            text="",
            width=450,
            height=340
        )
        

        self.chart4.grid(
            row=2,
            column=1,
            padx=30,
            pady=30,
            sticky="n"
        )
    #################################################
# Export Section
#################################################

        self.build_export_section()
        # --------------------------------------------------
    # Export Section
    # --------------------------------------------------

    def build_export_section(self):

        export_frame = ctk.CTkFrame(self)

        export_frame.pack(
            fill="x",
            padx=20,
            pady=(10, 20)
        )

        title = ctk.CTkLabel(
            export_frame,
            text="Export Reports",
            font=("Arial", 20, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        buttons = ctk.CTkFrame(
            export_frame,
            fg_color="transparent"
        )

        buttons.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        excel_btn = ctk.CTkButton(
            buttons,
            text="📊 Export to Excel",
            width=220,
            command=self.export_excel
        )

        excel_btn.pack(
            side="left",
            padx=10
        )

        pdf_btn = ctk.CTkButton(
            buttons,
            text="📄 Export to PDF",
            width=220,
            command=self.export_pdf
        )

        pdf_btn.pack(
            side="left",
            padx=10
        )

        refresh_btn = ctk.CTkButton(
            buttons,
            text="🔄 Refresh",
            width=180,
            command=self.refresh_dashboard
        )

        refresh_btn.pack(
            side="right",
            padx=10
        )

        # --------------------------------------------------
    # Load Dashboard
    # --------------------------------------------------

    def load_dashboard(self):

        #################################################
        # Dashboard Summary
        #################################################

        summary = ReportController.get_dashboard_summary()

        self.student_card.update_value(
            str(summary["students"])
        )

        self.faculty_card.update_value(
            str(summary["faculty"])
        )

        self.course_card.update_value(
            str(summary["courses"])
        )

        self.fee_card.update_value(
            str(summary["fees"])
        )

        self.attendance_card.update_value(
            str(summary["attendance"])
        )

        #################################################
        # Attendance Summary
        #################################################

        attendance = ReportController.get_attendance_summary()

        self.present_label.configure(
            text=f"🟢 Present : {attendance['present']}"
        )

        self.absent_label.configure(
            text=f"🔴 Absent : {attendance['absent']}"
        )

        self.late_label.configure(
            text=f"🟡 Late : {attendance['late']}"
        )

        #################################################
        # Fee Summary
        #################################################

        fees = ReportController.get_fee_summary()

        self.paid_label.configure(
            text=f"🟢 Paid : {fees['paid']}"
        )

        self.partial_label.configure(
            text=f"🟡 Partial : {fees['partial']}"
        )

        self.pending_label.configure(
            text=f"🔴 Pending : {fees['pending']}"
        )

        #################################################
        # Generate Charts
        #################################################

        ChartGenerator.attendance_chart(
            attendance
        )

        ChartGenerator.fee_chart(
            fees
        )

        ChartGenerator.department_chart(
            ReportController.get_students_by_department()
        )

        ChartGenerator.course_chart(
            ReportController.get_courses_by_department()
        )

        #################################################
        # Load Images
        #################################################

        import os

        charts = [

            (
                "exports/charts/attendance_pie.png",
                self.chart1,
                (320, 320)
            ),

            (
                "exports/charts/fee_pie.png",
                self.chart2,
                (320, 320)
            ),

            (
                "exports/charts/department_chart.png",
                self.chart3,
                (420, 280)
            ),

            (
                "exports/charts/course_chart.png",
                self.chart4,
                (420, 280)
            )

        ]

        for path, label, size in charts:

            if os.path.exists(path):

                image = ctk.CTkImage(

                    light_image=Image.open(path),

                    size=size

                )

                label.configure(

                    image=image,

                    text=""

                )

                label.image = image

            else:

                label.configure(

                    text="Chart not available",

                    image=None

                )

    # --------------------------------------------------
    # Refresh
    # --------------------------------------------------

    def refresh_dashboard(self):

        self.load_dashboard()
    # --------------------------------------------------
    # Export Excel
    # --------------------------------------------------

    def export_excel(self):

        try:

            ExcelExporter.export_students()

            ExcelExporter.export_faculty()

            ExcelExporter.export_courses()

            ExcelExporter.export_attendance()

            ExcelExporter.export_fees()

            messagebox.showinfo(

                "Export Successful",

                "All Excel reports have been exported successfully!\n\n"

                "Location:\nexports/excel/"

            )

        except Exception as error:

            messagebox.showerror(

                "Export Failed",

                str(error)

            )

    # --------------------------------------------------
    # Export PDF
    # --------------------------------------------------

    def export_pdf(self):

        try:

            PDFExporter.export_students()

            PDFExporter.export_faculty()

            PDFExporter.export_courses()

            PDFExporter.export_attendance()

            PDFExporter.export_fees()

            messagebox.showinfo(

                "Export Successful",

                "All PDF reports have been exported successfully!\n\n"

                "Location:\nexports/pdf/"

            )

        except Exception as error:

            messagebox.showerror(

                "Export Failed",

                str(error)

            )
