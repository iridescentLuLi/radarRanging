# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 556)
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1021, 561))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 20, 631, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.BScanImage = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.BScanImage.setContentsMargins(0, 0, 0, 0)
        self.BScanImage.setObjectName("BScanImage")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 230, 341, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.RangeNetPlot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.RangeNetPlot.setContentsMargins(0, 0, 0, 0)
        self.RangeNetPlot.setObjectName("RangeNetPlot")
        self.btnStart = QtWidgets.QPushButton(self.tab_2)
        self.btnStart.setGeometry(QtCore.QRect(30, 30, 131, 51))
        self.btnStart.setObjectName("btnStart")
        self.btnSave = QtWidgets.QPushButton(self.tab_2)
        self.btnSave.setGeometry(QtCore.QRect(180, 30, 141, 51))
        self.btnSave.setObjectName("btnSave")
        self.btnClear = QtWidgets.QPushButton(self.tab_2)
        self.btnClear.setGeometry(QtCore.QRect(30, 100, 131, 51))
        self.btnClear.setObjectName("btnClear")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.editDistanceStart = QtWidgets.QLineEdit(self.tab)
        self.editDistanceStart.setGeometry(QtCore.QRect(310, 250, 113, 41))
        self.editDistanceStart.setObjectName("editDistanceStart")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 230, 251, 81))
        self.label.setObjectName("label")
        self.editDistanceEnd = QtWidgets.QLineEdit(self.tab)
        self.editDistanceEnd.setGeometry(QtCore.QRect(480, 250, 113, 41))
        self.editDistanceEnd.setObjectName("editDistanceEnd")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(430, 230, 51, 81))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(600, 230, 51, 81))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 251, 81))
        self.label_5.setObjectName("label_5")
        self.editNodeIDInputA = QtWidgets.QLineEdit(self.tab)
        self.editNodeIDInputA.setGeometry(QtCore.QRect(160, 40, 113, 41))
        self.editNodeIDInputA.setObjectName("editNodeIDInputA")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(300, 20, 251, 81))
        self.label_6.setObjectName("label_6")
        self.editNodeIDInputB = QtWidgets.QLineEdit(self.tab)
        self.editNodeIDInputB.setGeometry(QtCore.QRect(420, 40, 113, 41))
        self.editNodeIDInputB.setObjectName("editNodeIDInputB")
        self.btnNodeIdSet = QtWidgets.QPushButton(self.tab)
        self.btnNodeIdSet.setGeometry(QtCore.QRect(580, 30, 151, 51))
        self.btnNodeIdSet.setObjectName("btnNodeIdSet")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 181, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(250, 160, 31, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(340, 160, 31, 51))
        self.label_9.setObjectName("label_9")
        self.labelNodeA = QtWidgets.QLabel(self.tab)
        self.labelNodeA.setGeometry(QtCore.QRect(280, 160, 61, 51))
        self.labelNodeA.setObjectName("labelNodeA")
        self.labelNodeB = QtWidgets.QLabel(self.tab)
        self.labelNodeB.setGeometry(QtCore.QRect(370, 160, 71, 51))
        self.labelNodeB.setObjectName("labelNodeB")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 290, 251, 81))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 350, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.editTransmitGain = QtWidgets.QLineEdit(self.tab)
        self.editTransmitGain.setGeometry(QtCore.QRect(310, 310, 113, 41))
        self.editTransmitGain.setObjectName("editTransmitGain")
        self.editIntegratinoIdex = QtWidgets.QLineEdit(self.tab)
        self.editIntegratinoIdex.setGeometry(QtCore.QRect(310, 370, 113, 41))
        self.editIntegratinoIdex.setObjectName("editIntegratinoIdex")
        self.btnRadarConfigSet = QtWidgets.QPushButton(self.tab)
        self.btnRadarConfigSet.setGeometry(QtCore.QRect(310, 440, 181, 51))
        self.btnRadarConfigSet.setObjectName("btnRadarConfigSet")
        self.btnRadarConfigRead = QtWidgets.QPushButton(self.tab)
        self.btnRadarConfigRead.setGeometry(QtCore.QRect(20, 440, 171, 51))
        self.btnRadarConfigRead.setObjectName("btnRadarConfigRead")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(30, 90, 251, 81))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(520, 160, 131, 51))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(760, 160, 131, 51))
        self.label_14.setObjectName("label_14")
        self.editDistance = QtWidgets.QLineEdit(self.tab)
        self.editDistance.setGeometry(QtCore.QRect(160, 110, 113, 41))
        self.editDistance.setObjectName("editDistance")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(280, 110, 131, 51))
        self.label_15.setObjectName("label_15")
        self.labelDistance = QtWidgets.QLabel(self.tab)
        self.labelDistance.setGeometry(QtCore.QRect(650, 160, 101, 51))
        self.labelDistance.setObjectName("labelDistance")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "image"))
        self.label.setText(_translate("MainWindow", "Detection distance"))
        self.label_2.setText(_translate("MainWindow", "m -"))
        self.label_3.setText(_translate("MainWindow", "m"))
        self.label_5.setText(_translate("MainWindow", "NodeID A"))
        self.label_6.setText(_translate("MainWindow", "NodeID B"))
        self.btnNodeIdSet.setText(_translate("MainWindow", "Confirm"))
        self.label_7.setText(_translate("MainWindow", "Current Node: "))
        self.label_8.setText(_translate("MainWindow", "A:"))
        self.label_9.setText(_translate("MainWindow", "B:"))
        self.labelNodeA.setText(_translate("MainWindow", "0"))
        self.labelNodeB.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Transmit Gain "))
        self.label_11.setText(_translate("MainWindow", "Base Integration Index"))
        self.btnRadarConfigSet.setText(_translate("MainWindow", "Write Config"))
        self.btnRadarConfigRead.setText(_translate("MainWindow", "Read Config"))
        self.label_12.setText(_translate("MainWindow", "Distance:"))
        self.label_13.setText(_translate("MainWindow", "Distance:"))
        self.label_14.setText(_translate("MainWindow", "m"))
        self.label_15.setText(_translate("MainWindow", "m"))
        self.labelDistance.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "config"))
