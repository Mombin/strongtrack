# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '08.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1675, 1081)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(750, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SideBar = QtWidgets.QVBoxLayout()
        self.SideBar.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.SideBar.setSpacing(6)
        self.SideBar.setObjectName("SideBar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(120, 140, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.button_landmarks = QtWidgets.QPushButton(self.centralwidget)
        self.button_landmarks.setEnabled(False)
        self.button_landmarks.setObjectName("button_landmarks")
        self.verticalLayout_3.addWidget(self.button_landmarks)
        self.button_train = QtWidgets.QPushButton(self.centralwidget)
        self.button_train.setEnabled(False)
        self.button_train.setObjectName("button_train")
        self.verticalLayout_3.addWidget(self.button_train)
        self.button_weld = QtWidgets.QPushButton(self.centralwidget)
        self.button_weld.setEnabled(False)
        self.button_weld.setObjectName("button_weld")
        self.verticalLayout_3.addWidget(self.button_weld)
        self.button_neutral = QtWidgets.QPushButton(self.centralwidget)
        self.button_neutral.setEnabled(False)
        self.button_neutral.setObjectName("button_neutral")
        self.verticalLayout_3.addWidget(self.button_neutral)
        self.button_guess = QtWidgets.QPushButton(self.centralwidget)
        self.button_guess.setEnabled(False)
        self.button_guess.setObjectName("button_guess")
        self.verticalLayout_3.addWidget(self.button_guess)
        self.button_mouth = QtWidgets.QPushButton(self.centralwidget)
        self.button_mouth.setEnabled(False)
        self.button_mouth.setObjectName("button_mouth")
        self.verticalLayout_3.addWidget(self.button_mouth)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox)
        self.button_setKeypose = QtWidgets.QPushButton(self.centralwidget)
        self.button_setKeypose.setEnabled(False)
        self.button_setKeypose.setObjectName("button_setKeypose")
        self.verticalLayout_5.addWidget(self.button_setKeypose)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.label_currentmodeltitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_currentmodeltitle.setFont(font)
        self.label_currentmodeltitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currentmodeltitle.setWordWrap(False)
        self.label_currentmodeltitle.setObjectName("label_currentmodeltitle")
        self.verticalLayout_5.addWidget(self.label_currentmodeltitle)
        self.label_currentmodel = QtWidgets.QLabel(self.centralwidget)
        self.label_currentmodel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currentmodel.setObjectName("label_currentmodel")
        self.verticalLayout_5.addWidget(self.label_currentmodel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.label_exportready = QtWidgets.QLabel(self.centralwidget)
        self.label_exportready.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_exportready.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_exportready.setFont(font)
        self.label_exportready.setAlignment(QtCore.Qt.AlignCenter)
        self.label_exportready.setWordWrap(True)
        self.label_exportready.setObjectName("label_exportready")
        self.verticalLayout_5.addWidget(self.label_exportready)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.label_videotitle = QtWidgets.QLabel(self.centralwidget)
        self.label_videotitle.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_videotitle.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_videotitle.setFont(font)
        self.label_videotitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_videotitle.setWordWrap(True)
        self.label_videotitle.setObjectName("label_videotitle")
        self.verticalLayout_5.addWidget(self.label_videotitle)
        self.label_videoflavour = QtWidgets.QLabel(self.centralwidget)
        self.label_videoflavour.setAlignment(QtCore.Qt.AlignCenter)
        self.label_videoflavour.setWordWrap(True)
        self.label_videoflavour.setObjectName("label_videoflavour")
        self.verticalLayout_5.addWidget(self.label_videoflavour)
        self.label_landmarks = QtWidgets.QLabel(self.centralwidget)
        self.label_landmarks.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_landmarks.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_landmarks.setFont(font)
        self.label_landmarks.setAlignment(QtCore.Qt.AlignCenter)
        self.label_landmarks.setWordWrap(True)
        self.label_landmarks.setObjectName("label_landmarks")
        self.verticalLayout_5.addWidget(self.label_landmarks)
        self.label_landmarksflavour = QtWidgets.QLabel(self.centralwidget)
        self.label_landmarksflavour.setAlignment(QtCore.Qt.AlignCenter)
        self.label_landmarksflavour.setWordWrap(True)
        self.label_landmarksflavour.setObjectName("label_landmarksflavour")
        self.verticalLayout_5.addWidget(self.label_landmarksflavour)
        self.label_keyposes = QtWidgets.QLabel(self.centralwidget)
        self.label_keyposes.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_keyposes.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_keyposes.setFont(font)
        self.label_keyposes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_keyposes.setWordWrap(True)
        self.label_keyposes.setObjectName("label_keyposes")
        self.verticalLayout_5.addWidget(self.label_keyposes)
        self.label_keyposesflavour = QtWidgets.QLabel(self.centralwidget)
        self.label_keyposesflavour.setAlignment(QtCore.Qt.AlignCenter)
        self.label_keyposesflavour.setWordWrap(True)
        self.label_keyposesflavour.setObjectName("label_keyposesflavour")
        self.verticalLayout_5.addWidget(self.label_keyposesflavour)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.SideBar.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.SideBar)
        self.RightBar = QtWidgets.QVBoxLayout()
        self.RightBar.setObjectName("RightBar")
        self.vidholder = QtWidgets.QHBoxLayout()
        self.vidholder.setObjectName("vidholder")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMouseTracking(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vidholder.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.RightBar.addLayout(self.vidholder)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.RightBar.addWidget(self.horizontalSlider)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_prevFrame = QtWidgets.QPushButton(self.centralwidget)
        self.button_prevFrame.setEnabled(False)
        self.button_prevFrame.setObjectName("button_prevFrame")
        self.horizontalLayout_3.addWidget(self.button_prevFrame)
        self.button_playPause = QtWidgets.QPushButton(self.centralwidget)
        self.button_playPause.setEnabled(False)
        self.button_playPause.setObjectName("button_playPause")
        self.horizontalLayout_3.addWidget(self.button_playPause)
        self.button_nextFrame = QtWidgets.QPushButton(self.centralwidget)
        self.button_nextFrame.setEnabled(False)
        self.button_nextFrame.setObjectName("button_nextFrame")
        self.horizontalLayout_3.addWidget(self.button_nextFrame)
        self.button_record = QtWidgets.QPushButton(self.centralwidget)
        self.button_record.setEnabled(False)
        self.button_record.setObjectName("button_record")
        self.horizontalLayout_3.addWidget(self.button_record)
        self.button_lockWebcamBox = QtWidgets.QPushButton(self.centralwidget)
        self.button_lockWebcamBox.setEnabled(False)
        self.button_lockWebcamBox.setObjectName("button_lockWebcamBox")
        self.horizontalLayout_3.addWidget(self.button_lockWebcamBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.RightBar.addLayout(self.verticalLayout)
        self.RightBar.setStretch(0, 50)
        self.RightBar.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.RightBar)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1675, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Video = QtWidgets.QAction(MainWindow)
        self.actionOpen_Video.setObjectName("actionOpen_Video")
        self.actionNew_Model = QtWidgets.QAction(MainWindow)
        self.actionNew_Model.setEnabled(False)
        self.actionNew_Model.setObjectName("actionNew_Model")
        self.actionLoad_Model = QtWidgets.QAction(MainWindow)
        self.actionLoad_Model.setEnabled(False)
        self.actionLoad_Model.setObjectName("actionLoad_Model")
        self.actionPrevious_Model = QtWidgets.QAction(MainWindow)
        self.actionPrevious_Model.setEnabled(False)
        self.actionPrevious_Model.setObjectName("actionPrevious_Model")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setEnabled(False)
        self.actionExport.setObjectName("actionExport")
        self.actionStream_OSC = QtWidgets.QAction(MainWindow)
        self.actionStream_OSC.setEnabled(False)
        self.actionStream_OSC.setObjectName("actionStream_OSC")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionQuick_Video = QtWidgets.QAction(MainWindow)
        self.actionQuick_Video.setObjectName("actionQuick_Video")
        self.actionOpen_Webcam = QtWidgets.QAction(MainWindow)
        self.actionOpen_Webcam.setWhatsThis("")
        self.actionOpen_Webcam.setObjectName("actionOpen_Webcam")
        self.actionRecord_Webcam = QtWidgets.QAction(MainWindow)
        self.actionRecord_Webcam.setEnabled(False)
        self.actionRecord_Webcam.setObjectName("actionRecord_Webcam")
        self.actionOpen_Webcam_Video_recorded = QtWidgets.QAction(MainWindow)
        self.actionOpen_Webcam_Video_recorded.setObjectName("actionOpen_Webcam_Video_recorded")
        self.menuFile.addAction(self.actionOpen_Video)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Webcam)
        self.menuFile.addAction(self.actionOpen_Webcam_Video_recorded)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_Model)
        self.menuFile.addAction(self.actionLoad_Model)
        self.menuFile.addAction(self.actionPrevious_Model)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuData.addAction(self.actionExport)
        self.menuData.addAction(self.actionStream_OSC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StrongTrack 0.8"))
        self.label_2.setText(_translate("MainWindow", "Training Landmarks:"))
        self.button_landmarks.setText(_translate("MainWindow", "Log Landmarks (F)"))
        self.button_train.setText(_translate("MainWindow", "Train Model (T)"))
        self.button_weld.setText(_translate("MainWindow", "Weld Lips (W)"))
        self.button_neutral.setText(_translate("MainWindow", "Neutral Lips (N)"))
        self.button_guess.setText(_translate("MainWindow", "Guess all points (G)"))
        self.button_mouth.setText(_translate("MainWindow", "Guess mouth points (M)"))
        self.label_3.setText(_translate("MainWindow", "Extraction poses:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Neutral"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Jaw Open"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Closed Smile"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Smile Left"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Smile Right"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Mouth Frown"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Lip Funnel"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Lip Pucker"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Brows Up"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Brows Down"))
        self.button_setKeypose.setText(_translate("MainWindow", "Set Keypose"))
        self.label_currentmodeltitle.setText(_translate("MainWindow", "Current Model:"))
        self.label_currentmodel.setText(_translate("MainWindow", "None"))
        self.label_exportready.setText(_translate("MainWindow", "Not ready for export or stream"))
        self.label_videotitle.setText(_translate("MainWindow", "Video: Not opened"))
        self.label_videoflavour.setText(_translate("MainWindow", "Head to \'File\' and open a video or webcam feed"))
        self.label_landmarks.setText(_translate("MainWindow", "Landmarks: Not placed"))
        self.label_landmarksflavour.setText(_translate("MainWindow", "Open the file menu and either create a new model or load a previously created one."))
        self.label_keyposes.setText(_translate("MainWindow", "Keyposes: Not set"))
        self.label_keyposesflavour.setText(_translate("MainWindow", "Look at the \'extraction poses\' drop down menu above and have the subject in the video pull these poses. Pause the video and set the keypose to the matching expression. "))
        self.label.setText(_translate("MainWindow", "Select \'Open Video\' or \'Open Webcam\' from the File menu to get started"))
        self.button_prevFrame.setText(_translate("MainWindow", "Prev. Frame (A)"))
        self.button_playPause.setText(_translate("MainWindow", "Pause/Play (Space)"))
        self.button_nextFrame.setText(_translate("MainWindow", "Next Frame (D)"))
        self.button_record.setText(_translate("MainWindow", "Record webcam video and animation"))
        self.button_lockWebcamBox.setText(_translate("MainWindow", "Lock Box position"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuData.setTitle(_translate("MainWindow", "Stream/Export"))
        self.actionOpen_Video.setText(_translate("MainWindow", "Open Video..."))
        self.actionNew_Model.setText(_translate("MainWindow", "New Model..."))
        self.actionLoad_Model.setText(_translate("MainWindow", "Load Model..."))
        self.actionPrevious_Model.setText(_translate("MainWindow", "Previous Model"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExport.setText(_translate("MainWindow", "Export..."))
        self.actionStream_OSC.setText(_translate("MainWindow", "Stream OSC..."))
        self.actionDocumentation.setText(_translate("MainWindow", "Docs (web link)"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionQuick_Video.setText(_translate("MainWindow", "Quick Video"))
        self.actionOpen_Webcam.setText(_translate("MainWindow", "Open Webcam Feed (experimental)"))
        self.actionRecord_Webcam.setText(_translate("MainWindow", "Record Webcam"))
        self.actionOpen_Webcam_Video_recorded.setText(_translate("MainWindow", "Open Webcam Video (previously recorded)..."))
        self.actionOpen_Webcam_Video_recorded.setIconText(_translate("MainWindow", "Open Webcam Video (previously recorded)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())