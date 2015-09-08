# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Sep  8 10:05:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 760)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mapViewer = MapViewer(self.centralwidget)
        self.mapViewer.setObjectName("mapViewer")
        self.horizontalLayout.addWidget(self.mapViewer)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 695))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comCheckBox = QtGui.QCheckBox(self.groupBox)
        self.comCheckBox.setEnabled(False)
        self.comCheckBox.setTristate(False)
        self.comCheckBox.setObjectName("comCheckBox")
        self.verticalLayout_4.addWidget(self.comCheckBox)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setEnabled(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.transparencySlider = QtGui.QSlider(self.groupBox)
        self.transparencySlider.setEnabled(True)
        self.transparencySlider.setMaximum(100)
        self.transparencySlider.setProperty("value", 70)
        self.transparencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.transparencySlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.transparencySlider.setObjectName("transparencySlider")
        self.verticalLayout_4.addWidget(self.transparencySlider)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startButton = QtGui.QPushButton(self.groupBox_2)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_2.addWidget(self.startButton)
        self.logPosButton = QtGui.QPushButton(self.groupBox_2)
        self.logPosButton.setCheckable(True)
        self.logPosButton.setObjectName("logPosButton")
        self.verticalLayout_2.addWidget(self.logPosButton)
        self.stopButton = QtGui.QPushButton(self.groupBox_2)
        self.stopButton.setEnabled(False)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_2.addWidget(self.stopButton)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtGui.QToolBox(self.groupBox_3)
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 254, 258))
        self.page.setObjectName("page")
        self.gridLayout = QtGui.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.killedRobotBox = QtGui.QComboBox(self.page)
        self.killedRobotBox.setObjectName("killedRobotBox")
        self.gridLayout.addWidget(self.killedRobotBox, 0, 1, 1, 1)
        self.warnedKilledRobotBox = QtGui.QComboBox(self.page)
        self.warnedKilledRobotBox.setObjectName("warnedKilledRobotBox")
        self.gridLayout.addWidget(self.warnedKilledRobotBox, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.killButton = QtGui.QPushButton(self.page)
        self.killButton.setObjectName("killButton")
        self.gridLayout.addWidget(self.killButton, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 254, 258))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vnetRobotBox = QtGui.QComboBox(self.page_2)
        self.vnetRobotBox.setObjectName("vnetRobotBox")
        self.horizontalLayout_2.addWidget(self.vnetRobotBox)
        self.vnetIsolateButton = QtGui.QPushButton(self.page_2)
        self.vnetIsolateButton.setObjectName("vnetIsolateButton")
        self.horizontalLayout_2.addWidget(self.vnetIsolateButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.vnetBlockButton = QtGui.QPushButton(self.page_2)
        self.vnetBlockButton.setObjectName("vnetBlockButton")
        self.verticalLayout_6.addWidget(self.vnetBlockButton)
        self.vnetResetButton = QtGui.QPushButton(self.page_2)
        self.vnetResetButton.setObjectName("vnetResetButton")
        self.verticalLayout_6.addWidget(self.vnetResetButton)
        self.vnetInfoLabel = QtGui.QLabel(self.page_2)
        self.vnetInfoLabel.setText("")
        self.vnetInfoLabel.setObjectName("vnetInfoLabel")
        self.verticalLayout_6.addWidget(self.vnetInfoLabel)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 254, 258))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtGui.QLabel(self.page_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.targetRobotBox = QtGui.QComboBox(self.page_3)
        self.targetRobotBox.setObjectName("targetRobotBox")
        self.horizontalLayout_5.addWidget(self.targetRobotBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtGui.QLabel(self.page_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.targetXField = QtGui.QLineEdit(self.page_3)
        self.targetXField.setMaximumSize(QtCore.QSize(40, 16777215))
        self.targetXField.setObjectName("targetXField")
        self.horizontalLayout_6.addWidget(self.targetXField)
        self.targetYField = QtGui.QLineEdit(self.page_3)
        self.targetYField.setMaximumSize(QtCore.QSize(40, 16777215))
        self.targetYField.setObjectName("targetYField")
        self.horizontalLayout_6.addWidget(self.targetYField)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.targetSendButton = QtGui.QPushButton(self.page_3)
        self.targetSendButton.setObjectName("targetSendButton")
        self.verticalLayout_7.addWidget(self.targetSendButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 254, 258))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(self.page_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.debugRobotBox = QtGui.QComboBox(self.page_4)
        self.debugRobotBox.setObjectName("debugRobotBox")
        self.horizontalLayout_3.addWidget(self.debugRobotBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.debugStateBox = QtGui.QComboBox(self.page_4)
        self.debugStateBox.setObjectName("debugStateBox")
        self.horizontalLayout_7.addWidget(self.debugStateBox)
        self.debugStateSend = QtGui.QPushButton(self.page_4)
        self.debugStateSend.setObjectName("debugStateSend")
        self.horizontalLayout_7.addWidget(self.debugStateSend)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.debugSendUpdateButton = QtGui.QPushButton(self.page_4)
        self.debugSendUpdateButton.setObjectName("debugSendUpdateButton")
        self.horizontalLayout_4.addWidget(self.debugSendUpdateButton)
        self.debugRepairButton = QtGui.QPushButton(self.page_4)
        self.debugRepairButton.setObjectName("debugRepairButton")
        self.horizontalLayout_4.addWidget(self.debugRepairButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.toolBox.addItem(self.page_4, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ISMAC", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Affichage", None, QtGui.QApplication.UnicodeUTF8))
        self.comCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Communications", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Transparence", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Opérateur Mission", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "Start mission", None, QtGui.QApplication.UnicodeUTF8))
        self.logPosButton.setText(QtGui.QApplication.translate("MainWindow", "Log Pose OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop mission", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Opérateur simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Killed robot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Informed robot", None, QtGui.QApplication.UnicodeUTF8))
        self.killButton.setText(QtGui.QApplication.translate("MainWindow", "Kill", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Robot Mort", None, QtGui.QApplication.UnicodeUTF8))
        self.vnetIsolateButton.setText(QtGui.QApplication.translate("MainWindow", "Isoler", None, QtGui.QApplication.UnicodeUTF8))
        self.vnetBlockButton.setText(QtGui.QApplication.translate("MainWindow", "Tout bloquer", None, QtGui.QApplication.UnicodeUTF8))
        self.vnetResetButton.setText(QtGui.QApplication.translate("MainWindow", "Remise à zéro", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "vNet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Robot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Position (x,y)", None, QtGui.QApplication.UnicodeUTF8))
        self.targetXField.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "236", None, QtGui.QApplication.UnicodeUTF8))
        self.targetYField.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "-9", None, QtGui.QApplication.UnicodeUTF8))
        self.targetSendButton.setText(QtGui.QApplication.translate("MainWindow", "Envoyer", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("MainWindow", "Détection de cible", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Robot", None, QtGui.QApplication.UnicodeUTF8))
        self.debugStateSend.setText(QtGui.QApplication.translate("MainWindow", "Envoyer", None, QtGui.QApplication.UnicodeUTF8))
        self.debugSendUpdateButton.setText(QtGui.QApplication.translate("MainWindow", "Envoyer \n"
"MàJ STN", None, QtGui.QApplication.UnicodeUTF8))
        self.debugRepairButton.setText(QtGui.QApplication.translate("MainWindow", "Réparation", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))

from map_viewer import MapViewer
