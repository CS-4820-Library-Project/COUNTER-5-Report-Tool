# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FetchReportsTab.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fetch_reports_tab(object):
    def setupUi(self, fetch_reports_tab):
        fetch_reports_tab.setObjectName("fetch_reports_tab")
        fetch_reports_tab.resize(800, 408)
        fetch_reports_tab.setMinimumSize(QtCore.QSize(800, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(fetch_reports_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(fetch_reports_tab)
        self.frame_4.setMouseTracking(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_35 = QtWidgets.QLabel(self.frame_4)
        self.label_35.setMinimumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_3.addWidget(self.label_35)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_28 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_34 = QtWidgets.QLabel(self.frame_28)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_12.addWidget(self.label_34)
        self.All_reports_edit_fetch = QtWidgets.QDateEdit(self.frame_28)
        self.All_reports_edit_fetch.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.All_reports_edit_fetch.setObjectName("All_reports_edit_fetch")
        self.horizontalLayout_12.addWidget(self.All_reports_edit_fetch)
        self.horizontalLayout_10.addWidget(self.frame_28)
        self.fetch_all_data_button = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_all_data_button.sizePolicy().hasHeightForWidth())
        self.fetch_all_data_button.setSizePolicy(sizePolicy)
        self.fetch_all_data_button.setMaximumSize(QtCore.QSize(300, 16777215))
        self.fetch_all_data_button.setObjectName("fetch_all_data_button")
        self.horizontalLayout_10.addWidget(self.fetch_all_data_button)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.Adv_Fetch_text = QtWidgets.QLabel(self.frame_4)
        self.Adv_Fetch_text.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Adv_Fetch_text.setFont(font)
        self.Adv_Fetch_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Adv_Fetch_text.setObjectName("Adv_Fetch_text")
        self.verticalLayout_3.addWidget(self.Adv_Fetch_text)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalFrame = QtWidgets.QFrame(self.frame_10)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.select_vendors_button_fetch = QtWidgets.QPushButton(self.horizontalFrame)
        self.select_vendors_button_fetch.setObjectName("select_vendors_button_fetch")
        self.horizontalLayout_4.addWidget(self.select_vendors_button_fetch)
        self.deselect_vendors_button_fetch = QtWidgets.QPushButton(self.horizontalFrame)
        self.deselect_vendors_button_fetch.setObjectName("deselect_vendors_button_fetch")
        self.horizontalLayout_4.addWidget(self.deselect_vendors_button_fetch)
        self.verticalLayout_4.addWidget(self.horizontalFrame)
        self.vendors_list_view_fetch = QtWidgets.QListView(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.vendors_list_view_fetch.setFont(font)
        self.vendors_list_view_fetch.setAlternatingRowColors(True)
        self.vendors_list_view_fetch.setObjectName("vendors_list_view_fetch")
        self.verticalLayout_4.addWidget(self.vendors_list_view_fetch)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.frame_11)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.select_report_types_button_fetch = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.select_report_types_button_fetch.setObjectName("select_report_types_button_fetch")
        self.horizontalLayout_6.addWidget(self.select_report_types_button_fetch)
        self.deselect_report_types_button_fetch = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.deselect_report_types_button_fetch.setObjectName("deselect_report_types_button_fetch")
        self.horizontalLayout_6.addWidget(self.deselect_report_types_button_fetch)
        self.report_types_help_button = QtWidgets.QPushButton(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_types_help_button.sizePolicy().hasHeightForWidth())
        self.report_types_help_button.setSizePolicy(sizePolicy)
        self.report_types_help_button.setMaximumSize(QtCore.QSize(25, 25))
        self.report_types_help_button.setObjectName("report_types_help_button")
        self.horizontalLayout_6.addWidget(self.report_types_help_button)
        self.verticalLayout_5.addWidget(self.horizontalFrame_2)
        self.report_types_list_view = QtWidgets.QListView(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.report_types_list_view.setFont(font)
        self.report_types_list_view.setAlternatingRowColors(True)
        self.report_types_list_view.setObjectName("report_types_list_view")
        self.verticalLayout_5.addWidget(self.report_types_list_view)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_14 = QtWidgets.QFrame(self.frame_7)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.frame_6 = QtWidgets.QFrame(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.end_date_edit_fetch_month = QtWidgets.QDateEdit(self.frame_6)
        self.end_date_edit_fetch_month.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date_edit_fetch_month.setObjectName("end_date_edit_fetch_month")
        self.gridLayout.addWidget(self.end_date_edit_fetch_month, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.begin_date_edit_fetch_year = QtWidgets.QDateEdit(self.frame_6)
        self.begin_date_edit_fetch_year.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.begin_date_edit_fetch_year.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.begin_date_edit_fetch_year.setObjectName("begin_date_edit_fetch_year")
        self.gridLayout.addWidget(self.begin_date_edit_fetch_year, 0, 1, 1, 1)
        self.end_date_edit_fetch_year = QtWidgets.QDateEdit(self.frame_6)
        self.end_date_edit_fetch_year.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date_edit_fetch_year.setObjectName("end_date_edit_fetch_year")
        self.gridLayout.addWidget(self.end_date_edit_fetch_year, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.begin_date_edit_fetch_month = QtWidgets.QDateEdit(self.frame_6)
        self.begin_date_edit_fetch_month.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.begin_date_edit_fetch_month.setObjectName("begin_date_edit_fetch_month")
        self.gridLayout.addWidget(self.begin_date_edit_fetch_month, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.custom_dir_frame = QtWidgets.QFrame(self.frame_14)
        self.custom_dir_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custom_dir_frame.setObjectName("custom_dir_frame")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.custom_dir_frame)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_38 = QtWidgets.QLabel(self.custom_dir_frame)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_26.addWidget(self.label_38)
        self.label_41 = QtWidgets.QLabel(self.custom_dir_frame)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_26.addWidget(self.label_41)
        self.frame_39 = QtWidgets.QFrame(self.custom_dir_frame)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.custom_dir_edit = QtWidgets.QLineEdit(self.frame_39)
        self.custom_dir_edit.setObjectName("custom_dir_edit")
        self.horizontalLayout_7.addWidget(self.custom_dir_edit)
        self.custom_dir_button = QtWidgets.QPushButton(self.frame_39)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_dir_button.sizePolicy().hasHeightForWidth())
        self.custom_dir_button.setSizePolicy(sizePolicy)
        self.custom_dir_button.setObjectName("custom_dir_button")
        self.horizontalLayout_7.addWidget(self.custom_dir_button)
        self.verticalLayout_26.addWidget(self.frame_39)
        self.verticalLayout_2.addWidget(self.custom_dir_frame)
        self.verticalLayout_7.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fetch_advanced_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_advanced_button.sizePolicy().hasHeightForWidth())
        self.fetch_advanced_button.setSizePolicy(sizePolicy)
        self.fetch_advanced_button.setObjectName("fetch_advanced_button")
        self.gridLayout_2.addWidget(self.fetch_advanced_button, 1, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_13)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(fetch_reports_tab)
        QtCore.QMetaObject.connectSlotsByName(fetch_reports_tab)

    def retranslateUi(self, fetch_reports_tab):
        _translate = QtCore.QCoreApplication.translate
        fetch_reports_tab.setWindowTitle(_translate("fetch_reports_tab", "Fetch Report"))
        self.label_35.setText(_translate("fetch_reports_tab", "Fetch All Reports"))
        self.label_34.setText(_translate("fetch_reports_tab", "Year"))
        self.All_reports_edit_fetch.setDisplayFormat(_translate("fetch_reports_tab", "yyyy"))
        self.fetch_all_data_button.setText(_translate("fetch_reports_tab", "Fetch All Reports"))
        self.Adv_Fetch_text.setText(_translate("fetch_reports_tab", "Advanced Fetch Reports"))
        self.label_11.setText(_translate("fetch_reports_tab", "Select Vendors"))
        self.select_vendors_button_fetch.setText(_translate("fetch_reports_tab", "Select All"))
        self.deselect_vendors_button_fetch.setText(_translate("fetch_reports_tab", "Deselect All"))
        self.label_12.setText(_translate("fetch_reports_tab", "Select Report Types"))
        self.select_report_types_button_fetch.setText(_translate("fetch_reports_tab", "Select All"))
        self.deselect_report_types_button_fetch.setText(_translate("fetch_reports_tab", "Deselect All"))
        self.report_types_help_button.setText(_translate("fetch_reports_tab", "?"))
        self.label_8.setText(_translate("fetch_reports_tab", "Date Range"))
        self.end_date_edit_fetch_month.setDisplayFormat(_translate("fetch_reports_tab", "MM"))
        self.label_9.setText(_translate("fetch_reports_tab", "Begin Date"))
        self.begin_date_edit_fetch_year.setDisplayFormat(_translate("fetch_reports_tab", "yyyy"))
        self.end_date_edit_fetch_year.setDisplayFormat(_translate("fetch_reports_tab", "yyyy"))
        self.label_10.setText(_translate("fetch_reports_tab", "End Date"))
        self.begin_date_edit_fetch_month.setDisplayFormat(_translate("fetch_reports_tab", "MM"))
        self.label_38.setText(_translate("fetch_reports_tab", "Not a yearly date range"))
        self.label_41.setText(_translate("fetch_reports_tab", "Report(s) will be saved to:"))
        self.custom_dir_button.setText(_translate("fetch_reports_tab", "Change"))
        self.fetch_advanced_button.setText(_translate("fetch_reports_tab", "Fetch Selected Reports"))
