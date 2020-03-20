import shutil
import webbrowser
import platform
import shlex
import ctypes
from os import path, makedirs, system
from PyQt5.QtCore import QModelIndex, QDate, Qt
from PyQt5.QtWidgets import QWidget, QDialog, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap
from PyQt5 import QtWidgets

import GeneralUtils
from ui import ImportReportTab, ReportResultWidget
from ManageVendors import Vendor
from FetchData import REPORT_TYPES, CompletionStatus
from Settings import SettingsModel
from UpdateDatabaseProgressDialogController import UpdateDatabaseProgressDialogController

# All yearly reports tsv and json are saved here in original condition as backup
PROTECTED_DIR = "./all_data/.DO_NOT_MODIFY/"


class ProcessResult:
    def __init__(self, vendor: Vendor, report_type: str):
        self.vendor = vendor
        self.report_type = report_type
        self.completion_status = CompletionStatus.SUCCESSFUL
        self.message = ""
        self.file_name = ""
        self.file_dir = ""
        self.file_path = ""


class ImportReportController:
    def __init__(self, vendors: list, settings: SettingsModel, import_report_widget: QWidget,
                 import_report_ui: ImportReportTab.Ui_import_report_tab):

        # region General
        self.import_report_widget = import_report_widget
        self.vendors = vendors
        self.date = QDate.currentDate()
        self.selected_vendor_index = -1
        self.selected_report_type_index = -1
        self.selected_file_path: str = ""
        self.settings = settings
        self.result_dialog = None
        # endregion

        # region Vendors
        self.vendor_list_view = import_report_ui.vendors_list_view_import
        self.vendor_list_model = QStandardItemModel(self.vendor_list_view)
        self.vendor_list_view.setModel(self.vendor_list_model)
        self.vendor_list_view.clicked.connect(self.on_vendor_selected)
        self.update_vendors_ui()
        # endregion

        # region Report Types
        self.report_type_list_view = import_report_ui.report_types_list_view_import
        self.report_type_list_model = QStandardItemModel(self.report_type_list_view)
        self.report_type_list_view.setModel(self.report_type_list_model)
        self.report_type_list_view.clicked.connect(self.on_report_type_selected)
        for report_type in REPORT_TYPES:
            item = QStandardItem(report_type)
            item.setEditable(False)
            self.report_type_list_model.appendRow(item)
        # endregion

        # region Others
        self.year_date_edit = import_report_ui.report_year_date_edit
        self.year_date_edit.setDate(self.date)
        self.year_date_edit.dateChanged.connect(self.on_date_changed)

        self.select_file_btn = import_report_ui.select_file_button
        self.select_file_btn.clicked.connect(self.on_select_file_clicked)

        self.selected_file_edit = import_report_ui.selected_file_edit

        self.import_report_button = import_report_ui.import_report_button
        self.import_report_button.clicked.connect(self.on_import_clicked)
        # endregion

        # set up restore database button
        self.is_restoring_database = False
        self.update_database_dialog = UpdateDatabaseProgressDialogController(self.import_report_widget)

    def on_vendors_changed(self, vendors: list):
        self.selected_vendor_index = -1
        self.update_vendors(vendors)
        self.update_vendors_ui()

    def update_vendors(self, vendors: list):
        self.vendors = vendors

    def update_vendors_ui(self):
        self.vendor_list_model.clear()
        for vendor in self.vendors:
            item = QStandardItem(vendor.name)
            item.setEditable(False)
            self.vendor_list_model.appendRow(item)

    def on_vendor_selected(self, model_index: QModelIndex):
        self.selected_vendor_index = model_index.row()

    def on_report_type_selected(self, model_index: QModelIndex):
        self.selected_report_type_index = model_index.row()

    def on_date_changed(self, date: QDate):
        self.date = date

    def on_select_file_clicked(self):
        file_path = GeneralUtils.choose_file("All TSV files (*.tsv)")
        if file_path:
            self.selected_file_path = file_path
            self.selected_file_edit.setText(file_path)

    def on_import_clicked(self):
        if self.selected_vendor_index == -1:
            GeneralUtils.show_message("Select a vendor")
            return
        elif self.selected_report_type_index == -1:
            GeneralUtils.show_message("Select a report type")
            return
        elif self.selected_file_path == "":
            GeneralUtils.show_message("Select a file")
            return

        vendor = self.vendors[self.selected_vendor_index]
        report_type = REPORT_TYPES[self.selected_report_type_index]

        process_result = self.import_report(vendor, report_type)
        self.show_result(process_result)

    def import_report(self, vendor: Vendor, report_type: str) -> ProcessResult:
        process_result = ProcessResult(vendor, report_type)

        try:
            dest_file_dir = f"{self.settings.yearly_directory}{self.date.toString('yyyy')}/{vendor.name}/"
            dest_file_name = f"{self.date.toString('yyyy')}_{vendor.name}_{report_type}.tsv"
            dest_file_path = f"{dest_file_dir}{dest_file_name}"

            self.verify_path_exists(dest_file_dir)
            self.copy_file(self.selected_file_path, dest_file_path)

            # Add file to database
            self.is_restoring_database = True
            self.update_database_dialog.update_database([{'file': dest_file_path,
                                                          'vendor': vendor.name,
                                                          'year': int(self.date.toString('yyyy'))}],
                                                        False)
            self.is_restoring_database = False

            process_result.file_dir = dest_file_dir
            process_result.file_name = dest_file_name
            process_result.file_path = dest_file_path
            process_result.completion_status = CompletionStatus.SUCCESSFUL

            # Save protected tsv file
            protected_file_dir = f"{PROTECTED_DIR}{self.date.toString('yyyy')}/{vendor.name}/"
            if not path.isdir(protected_file_dir):
                makedirs(protected_file_dir)
                if platform.system() == "Windows":
                    ctypes.windll.kernel32.SetFileAttributesW(PROTECTED_DIR, 2)  # Hide folder

            protected_file_path = f"{protected_file_dir}{dest_file_name}"
            self.copy_file(self.selected_file_path, protected_file_path)

        except Exception as e:
            process_result.message = f"Exception: {e}"
            process_result.completion_status = CompletionStatus.FAILED

        return process_result

    def verify_path_exists(self, path_str: str):
        if not path.isdir(path_str):
            makedirs(path_str)

    def copy_file(self, origin_path: str, dest_path: str):
        shutil.copy2(origin_path, dest_path)

    def show_result(self, process_result: ProcessResult):
        self.result_dialog = QDialog(self.import_report_widget, flags=Qt.WindowCloseButtonHint)
        self.result_dialog.setWindowTitle("Import Result")
        vertical_layout = QtWidgets.QVBoxLayout(self.result_dialog)
        vertical_layout.setContentsMargins(5, 5, 5, 5)

        report_result_widget = QWidget(self.result_dialog)
        report_result_ui = ReportResultWidget.Ui_ReportResultWidget()
        report_result_ui.setupUi(report_result_widget)

        vendor = process_result.vendor
        report_type = process_result.report_type

        report_result_ui.report_type_label.setText(f"{vendor.name} - {report_type}")
        report_result_ui.success_label.setText(process_result.completion_status.value)

        if process_result.completion_status == CompletionStatus.SUCCESSFUL:
            report_result_ui.message_label.hide()
            report_result_ui.retry_frame.hide()

            report_result_ui.file_label.setText(f"Saved as: {process_result.file_name}")
            report_result_ui.file_label.mousePressEvent = \
                lambda event: GeneralUtils.open_file_or_dir(process_result.file_path)

            folder_pixmap = QPixmap("./ui/resources/folder_icon.png")
            report_result_ui.folder_button.setIcon(QIcon(folder_pixmap))
            report_result_ui.folder_button.clicked.connect(
                lambda: GeneralUtils.open_file_or_dir(process_result.file_dir))

            report_result_ui.success_label.setText("Successful!")
            report_result_ui.retry_frame.hide()

        elif process_result.completion_status == CompletionStatus.FAILED:
            report_result_ui.file_frame.hide()
            report_result_ui.retry_frame.hide()

            report_result_ui.message_label.setText(process_result.message)

        vertical_layout.addWidget(report_result_widget)
        self.result_dialog.show()

