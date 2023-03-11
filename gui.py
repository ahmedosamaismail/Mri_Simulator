# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_phantom = QtWidgets.QFrame(self.frame_main)
        self.frame_phantom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_phantom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_phantom.setObjectName("frame_phantom")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_phantom)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_phantom = QtWidgets.QWidget(self.frame_phantom)
        self.widget_phantom.setObjectName("widget_phantom")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_phantom)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_10 = QtWidgets.QFrame(self.widget_phantom)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_phantom = QtWidgets.QLabel(self.frame_10)
        self.label_phantom.setText("")
        self.label_phantom.setObjectName("label_phantom")
        self.gridLayout_2.addWidget(self.label_phantom, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.widget_phantom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setContentsMargins(20, 0, 5, 0)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.slider_brightness = QtWidgets.QSlider(self.frame_9)
        self.slider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brightness.setObjectName("slider_brightness")
        self.horizontalLayout_4.addWidget(self.slider_brightness)
        self.lable_brightness = QtWidgets.QLabel(self.frame_9)
        self.lable_brightness.setObjectName("lable_brightness")
        self.horizontalLayout_4.addWidget(self.lable_brightness)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.widget_phantom)
        self.frame = QtWidgets.QFrame(self.frame_phantom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_size = QtWidgets.QLabel(self.frame_5)
        self.label_size.setObjectName("label_size")
        self.verticalLayout_3.addWidget(self.label_size)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_size = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_size.setObjectName("comboBox_size")
        self.verticalLayout_4.addWidget(self.comboBox_size)
        self.comboBox_weights = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_weights.setEditable(False)
        self.comboBox_weights.setObjectName("comboBox_weights")
        self.comboBox_weights.addItem("")
        self.comboBox_weights.addItem("")
        self.comboBox_weights.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_weights)
        self.horizontalLayout_2.addWidget(self.frame_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_T1 = QtWidgets.QLabel(self.frame_8)
        self.label_T1.setObjectName("label_T1")
        self.verticalLayout_6.addWidget(self.label_T1)
        self.label_T2 = QtWidgets.QLabel(self.frame_8)
        self.label_T2.setObjectName("label_T2")
        self.verticalLayout_6.addWidget(self.label_T2)
        self.label_PD = QtWidgets.QLabel(self.frame_8)
        self.label_PD.setObjectName("label_PD")
        self.verticalLayout_6.addWidget(self.label_PD)
        self.horizontalLayout_3.addWidget(self.frame_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_phantom)
        self.frame_3 = QtWidgets.QFrame(self.frame_main)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sequance = QtWidgets.QWidget()
        self.tab_sequance.setObjectName("tab_sequance")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_sequance)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.tab_sequance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.plotwidget_sequance = PlotWidget(self.tab_sequance)
        self.plotwidget_sequance.setObjectName("plotwidget_sequance")
        self.verticalLayout_8.addWidget(self.plotwidget_sequance)
        self.label_7 = QtWidgets.QLabel(self.tab_sequance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.plotwidget_kspace = PlotWidget(self.tab_sequance)
        self.plotwidget_kspace.setObjectName("plotwidget_kspace")
        self.verticalLayout_8.addWidget(self.plotwidget_kspace)
        self.btn_start_sequance = QtWidgets.QPushButton(self.tab_sequance)
        self.btn_start_sequance.setText("Start Sequance")
        self.btn_start_sequance.setObjectName("btn_start_sequance")
        self.verticalLayout_8.addWidget(self.btn_start_sequance)
        self.tabWidget.addTab(self.tab_sequance, "")
        self.tab_synth = QtWidgets.QWidget()
        self.tab_synth.setObjectName("tab_synth")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_synth)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.plotwidget_synth = PlotWidget(self.tab_synth)
        self.plotwidget_synth.setObjectName("plotwidget_synth")
        self.verticalLayout_9.addWidget(self.plotwidget_synth)
        self.frame_11 = QtWidgets.QFrame(self.tab_synth)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.txtbox_FA = QtWidgets.QPlainTextEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtbox_FA.sizePolicy().hasHeightForWidth())
        self.txtbox_FA.setSizePolicy(sizePolicy)
        self.txtbox_FA.setMaximumSize(QtCore.QSize(30, 25))
        self.txtbox_FA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txtbox_FA.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.txtbox_FA.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.txtbox_FA.setOverwriteMode(False)
        self.txtbox_FA.setObjectName("txtbox_FA")
        self.horizontalLayout_5.addWidget(self.txtbox_FA)
        self.horizontalLayout_6.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_13)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.txtbox_TR = QtWidgets.QPlainTextEdit(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtbox_TR.sizePolicy().hasHeightForWidth())
        self.txtbox_TR.setSizePolicy(sizePolicy)
        self.txtbox_TR.setMaximumSize(QtCore.QSize(30, 25))
        self.txtbox_TR.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txtbox_TR.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txtbox_TR.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.txtbox_TR.setOverwriteMode(False)
        self.txtbox_TR.setObjectName("txtbox_TR")
        self.horizontalLayout_7.addWidget(self.txtbox_TR)
        self.horizontalLayout_6.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.frame_14)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.txtbox_TE = QtWidgets.QPlainTextEdit(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtbox_TE.sizePolicy().hasHeightForWidth())
        self.txtbox_TE.setSizePolicy(sizePolicy)
        self.txtbox_TE.setMaximumSize(QtCore.QSize(30, 25))
        self.txtbox_TE.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txtbox_TE.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txtbox_TE.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.txtbox_TE.setOverwriteMode(False)
        self.txtbox_TE.setObjectName("txtbox_TE")
        self.horizontalLayout_8.addWidget(self.txtbox_TE)
        self.horizontalLayout_6.addWidget(self.frame_14)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.tabWidget.addTab(self.tab_synth, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mri Simulator"))
        self.label_5.setText(_translate("MainWindow", "Brightness"))
        self.lable_brightness.setText(_translate("MainWindow", "val"))
        self.label_size.setText(_translate("MainWindow", "Phantom Size"))
        self.label_2.setText(_translate("MainWindow", "Show"))
        self.comboBox_weights.setItemText(0, _translate("MainWindow", "T1"))
        self.comboBox_weights.setItemText(1, _translate("MainWindow", "T2"))
        self.comboBox_weights.setItemText(2, _translate("MainWindow", "PD"))
        self.label_4.setText(_translate("MainWindow", "T1:"))
        self.label.setText(_translate("MainWindow", "T2:"))
        self.label_3.setText(_translate("MainWindow", "PD:"))
        self.label_T1.setText(_translate("MainWindow", "T1value"))
        self.label_T2.setText(_translate("MainWindow", "T2value"))
        self.label_PD.setText(_translate("MainWindow", "PDvalue"))
        self.label_6.setText(_translate("MainWindow", "Sequance"))
        self.label_7.setText(_translate("MainWindow", "Kspace"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sequance), _translate("MainWindow", "Tab 1"))
        self.label_8.setText(_translate("MainWindow", "Flipe Angle:"))
        self.txtbox_FA.setPlainText(_translate("MainWindow", "312"))
        self.label_9.setText(_translate("MainWindow", "TR:"))
        self.txtbox_TR.setPlainText(_translate("MainWindow", "312"))
        self.label_10.setText(_translate("MainWindow", "TE:"))
        self.txtbox_TE.setPlainText(_translate("MainWindow", "312"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_synth), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())