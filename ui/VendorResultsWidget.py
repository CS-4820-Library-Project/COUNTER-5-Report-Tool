# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VendorResultsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VendorResultsWidget(object):
    def setupUi(self, VendorResultsWidget):
        VendorResultsWidget.setObjectName("VendorResultsWidget")
        VendorResultsWidget.resize(600, 59)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VendorResultsWidget.sizePolicy().hasHeightForWidth())
        VendorResultsWidget.setSizePolicy(sizePolicy)
        VendorResultsWidget.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        VendorResultsWidget.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(VendorResultsWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(VendorResultsWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vendor_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vendor_label.sizePolicy().hasHeightForWidth())
        self.vendor_label.setSizePolicy(sizePolicy)
        self.vendor_label.setObjectName("vendor_label")
        self.gridLayout_2.addWidget(self.vendor_label, 0, 1, 1, 1)
        self.results_frame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_frame.sizePolicy().hasHeightForWidth())
        self.results_frame.setSizePolicy(sizePolicy)
        self.results_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.results_frame.setObjectName("results_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.results_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2.addWidget(self.results_frame, 1, 1, 1, 6)
        self.collapse_button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collapse_button.sizePolicy().hasHeightForWidth())
        self.collapse_button.setSizePolicy(sizePolicy)
        self.collapse_button.setMinimumSize(QtCore.QSize(70, 0))
        self.collapse_button.setMaximumSize(QtCore.QSize(70, 16777215))
        self.collapse_button.setObjectName("collapse_button")
        self.gridLayout_2.addWidget(self.collapse_button, 0, 6, 1, 1)
        self.status_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setMinimumSize(QtCore.QSize(100, 0))
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.gridLayout_2.addWidget(self.status_label, 0, 4, 1, 1)
        self.expand_button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expand_button.sizePolicy().hasHeightForWidth())
        self.expand_button.setSizePolicy(sizePolicy)
        self.expand_button.setMinimumSize(QtCore.QSize(70, 0))
        self.expand_button.setMaximumSize(QtCore.QSize(70, 16777215))
        self.expand_button.setObjectName("expand_button")
        self.gridLayout_2.addWidget(self.expand_button, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(VendorResultsWidget)
        QtCore.QMetaObject.connectSlotsByName(VendorResultsWidget)

    def retranslateUi(self, VendorResultsWidget):
        _translate = QtCore.QCoreApplication.translate
        VendorResultsWidget.setWindowTitle(_translate("VendorResultsWidget", "Form"))
        self.vendor_label.setText(_translate("VendorResultsWidget", "Bioone"))
        self.collapse_button.setText(_translate("VendorResultsWidget", "Collapse"))
        self.status_label.setText(_translate("VendorResultsWidget", "Success"))
        self.expand_button.setText(_translate("VendorResultsWidget", "Expand"))
