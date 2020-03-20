# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportResultWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportResultWidget(object):
    def setupUi(self, ReportResultWidget):
        ReportResultWidget.setObjectName("ReportResultWidget")
        ReportResultWidget.resize(600, 60)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(ReportResultWidget.sizePolicy().hasHeightForWidth())
        ReportResultWidget.setSizePolicy(sizePolicy)
        ReportResultWidget.setMinimumSize(QtCore.QSize(600, 60))
        ReportResultWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ReportResultWidget.setSizeIncrement(QtCore.QSize(0, 1000))
        font = QtGui.QFont()
        font.setPointSize(9)
        ReportResultWidget.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ReportResultWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(ReportResultWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(600, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(80, 50))
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.report_type_label = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_type_label.sizePolicy().hasHeightForWidth())
        self.report_type_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.report_type_label.setFont(font)
        self.report_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.report_type_label.setObjectName("report_type_label")
        self.verticalLayout_5.addWidget(self.report_type_label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_frame = QtWidgets.QFrame(self.frame_2)
        self.file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_frame.setObjectName("file_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.file_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.file_label = QtWidgets.QLabel(self.file_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_label.sizePolicy().hasHeightForWidth())
        self.file_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.file_label.setFont(font)
        self.file_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_label.setStyleSheet("color: #0000EE")
        self.file_label.setWordWrap(True)
        self.file_label.setObjectName("file_label")
        self.horizontalLayout_4.addWidget(self.file_label)
        self.folder_button = QtWidgets.QPushButton(self.file_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_button.sizePolicy().hasHeightForWidth())
        self.folder_button.setSizePolicy(sizePolicy)
        self.folder_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/folder_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.folder_button.setIcon(icon)
        self.folder_button.setObjectName("folder_button")
        self.horizontalLayout_4.addWidget(self.folder_button)
        self.verticalLayout.addWidget(self.file_frame)
        self.message_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        self.message_label.setWordWrap(True)
        self.message_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.message_label.setObjectName("message_label")
        self.verticalLayout.addWidget(self.message_label)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(120, 50))
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.success_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.success_label.sizePolicy().hasHeightForWidth())
        self.success_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.success_label.setFont(font)
        self.success_label.setAlignment(QtCore.Qt.AlignCenter)
        self.success_label.setObjectName("success_label")
        self.horizontalLayout_3.addWidget(self.success_label)
        self.retry_frame = QtWidgets.QFrame(self.frame_4)
        self.retry_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.retry_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.retry_frame.setObjectName("retry_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.retry_frame)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.retry_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.retry_check_box = QtWidgets.QCheckBox(self.retry_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.retry_check_box.sizePolicy().hasHeightForWidth())
        self.retry_check_box.setSizePolicy(sizePolicy)
        self.retry_check_box.setText("")
        self.retry_check_box.setObjectName("retry_check_box")
        self.verticalLayout_7.addWidget(self.retry_check_box, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.retry_frame)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(ReportResultWidget)
        QtCore.QMetaObject.connectSlotsByName(ReportResultWidget)

    def retranslateUi(self, ReportResultWidget):
        _translate = QtCore.QCoreApplication.translate
        ReportResultWidget.setWindowTitle(_translate("ReportResultWidget", "Report Result"))
        self.report_type_label.setText(_translate("ReportResultWidget", "TR_J1"))
        self.file_label.setText(_translate("ReportResultWidget", "Saved as: Bleh.tsv"))
        self.message_label.setText(_translate("ReportResultWidget", "No exception messages"))
        self.success_label.setText(_translate("ReportResultWidget", "Failed!"))
        self.label_6.setText(_translate("ReportResultWidget", "Retry"))