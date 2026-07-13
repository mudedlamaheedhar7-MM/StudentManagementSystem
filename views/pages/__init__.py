import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

from controllers.report_controller import ReportController
from views.components.stat_card import StatCard
from views.reports.export_excel import ExcelExporter
from views.reports.export_pdf import PDFExporter
from views.reports.charts import ChartGenerator


class ReportsPage(ctk.CTkScrollableFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.build()

        self.load_dashboard()