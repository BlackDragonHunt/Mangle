# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev/ui/options.ui'
#
# Created: Sun Mar 20 00:06:33 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogOptions(object):
    def setupUi(self, DialogOptions):
        DialogOptions.setObjectName("DialogOptions")
        DialogOptions.resize(333, 446)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogOptions.sizePolicy().hasHeightForWidth())
        DialogOptions.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QtGui.QVBoxLayout(DialogOptions)
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(DialogOptions)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditTitle = QtGui.QLineEdit(self.groupBox)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditTitle)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DialogOptions)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBoxDevice = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxDevice.setObjectName("comboBoxDevice")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.comboBoxDevice.addItem("")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxDevice)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.checkboxOverwrite = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxOverwrite.setEnabled(True)
        self.checkboxOverwrite.setObjectName("checkboxOverwrite")
        self.verticalLayout_2.addWidget(self.checkboxOverwrite)
        self.checkboxCBZ = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxCBZ.setObjectName("checkboxCBZ")
        self.verticalLayout_2.addWidget(self.checkboxCBZ)
        self.checkboxOrient = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxOrient.setAutoExclusive(False)
        self.checkboxOrient.setObjectName("checkboxOrient")
        self.verticalLayout_2.addWidget(self.checkboxOrient)
        self.checkboxSplit = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxSplit.setAutoExclusive(False)
        self.checkboxSplit.setObjectName("checkboxSplit")
        self.verticalLayout_2.addWidget(self.checkboxSplit)
        self.checkboxShrink = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxShrink.setObjectName("checkboxShrink")
        self.verticalLayout_2.addWidget(self.checkboxShrink)
        self.checkboxEnlarge = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxEnlarge.setObjectName("checkboxEnlarge")
        self.verticalLayout_2.addWidget(self.checkboxEnlarge)
        self.checkboxQuantize = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxQuantize.setObjectName("checkboxQuantize")
        self.verticalLayout_2.addWidget(self.checkboxQuantize)
        self.checkboxFrame = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxFrame.setObjectName("checkboxFrame")
        self.verticalLayout_2.addWidget(self.checkboxFrame)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.restoreDefaults = QtGui.QPushButton(DialogOptions)
        self.restoreDefaults.setObjectName("restoreDefaults")
        self.verticalLayout.addWidget(self.restoreDefaults)
        self.saveDefaults = QtGui.QPushButton(DialogOptions)
        self.saveDefaults.setObjectName("saveDefaults")
        self.verticalLayout.addWidget(self.saveDefaults)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.buttonBox = QtGui.QDialogButtonBox(DialogOptions)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DialogOptions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogOptions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogOptions.reject)
        QtCore.QObject.connect(self.restoreDefaults, QtCore.SIGNAL("clicked()"), DialogOptions.restore_defaults)
        QtCore.QObject.connect(self.saveDefaults, QtCore.SIGNAL("clicked()"), DialogOptions.save_defaults)
        QtCore.QObject.connect(self.checkboxOrient, QtCore.SIGNAL("stateChanged(int)"), DialogOptions.orient_changed)
        QtCore.QObject.connect(self.checkboxSplit, QtCore.SIGNAL("stateChanged(int)"), DialogOptions.split_changed)
        QtCore.QObject.connect(self.checkboxCBZ, QtCore.SIGNAL("stateChanged(int)"), DialogOptions.cbz_changed)
        QtCore.QMetaObject.connectSlotsByName(DialogOptions)
        DialogOptions.setTabOrder(self.lineEditTitle, self.comboBoxDevice)
        DialogOptions.setTabOrder(self.comboBoxDevice, self.checkboxOverwrite)
        DialogOptions.setTabOrder(self.checkboxOverwrite, self.checkboxCBZ)
        DialogOptions.setTabOrder(self.checkboxCBZ, self.checkboxOrient)
        DialogOptions.setTabOrder(self.checkboxOrient, self.checkboxSplit)
        DialogOptions.setTabOrder(self.checkboxSplit, self.checkboxShrink)
        DialogOptions.setTabOrder(self.checkboxShrink, self.checkboxEnlarge)
        DialogOptions.setTabOrder(self.checkboxEnlarge, self.checkboxQuantize)
        DialogOptions.setTabOrder(self.checkboxQuantize, self.checkboxFrame)
        DialogOptions.setTabOrder(self.checkboxFrame, self.restoreDefaults)
        DialogOptions.setTabOrder(self.restoreDefaults, self.saveDefaults)
        DialogOptions.setTabOrder(self.saveDefaults, self.buttonBox)

    def retranslateUi(self, DialogOptions):
        DialogOptions.setWindowTitle(QtGui.QApplication.translate("DialogOptions", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogOptions", "Book", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogOptions", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogOptions", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogOptions", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(0, QtGui.QApplication.translate("DialogOptions", "Kindle 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(1, QtGui.QApplication.translate("DialogOptions", "Kindle 2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(2, QtGui.QApplication.translate("DialogOptions", "Kindle 3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(3, QtGui.QApplication.translate("DialogOptions", "Kindle DX", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(4, QtGui.QApplication.translate("DialogOptions", "Kindle DXG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(5, QtGui.QApplication.translate("DialogOptions", "nook", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(6, QtGui.QApplication.translate("DialogOptions", "nook color", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxOverwrite.setText(QtGui.QApplication.translate("DialogOptions", "Overwrite existing files", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxCBZ.setToolTip(QtGui.QApplication.translate("DialogOptions", "Don\'t output the converted images to a directory, but instead store them in a single .cbz archive.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxCBZ.setText(QtGui.QApplication.translate("DialogOptions", "Output to .cbz", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxOrient.setToolTip(QtGui.QApplication.translate("DialogOptions", "If an image has an aspect ratio too wide for the device\'s screen, rotate it 90 degrees to fit the device\'s aspect ratio.\n"
"\n"
"Note: This cannot be enabled simultaneously with \"Split images to match aspect ratio.\"", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxOrient.setText(QtGui.QApplication.translate("DialogOptions", "Orient images to match aspect ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxSplit.setToolTip(QtGui.QApplication.translate("DialogOptions", "If an image has an aspect ratio too wide for the device\'s screen, split it evenly into 2 (or 3, or 4, etc.) images that fit the device\'s aspect ratio.\n"
"\n"
"Note: This cannot be enabled simultaneously with \"Orient images to match aspect ratio.\"", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxSplit.setText(QtGui.QApplication.translate("DialogOptions", "Split images to match aspect ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxShrink.setText(QtGui.QApplication.translate("DialogOptions", "Shrink oversized images to fit on screen", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxEnlarge.setText(QtGui.QApplication.translate("DialogOptions", "Enlarge undersized images to fit on screen", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxQuantize.setText(QtGui.QApplication.translate("DialogOptions", "Dither images to match device palette", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxFrame.setText(QtGui.QApplication.translate("DialogOptions", "Draw frame around images", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreDefaults.setText(QtGui.QApplication.translate("DialogOptions", "Restore &Defaults", None, QtGui.QApplication.UnicodeUTF8))
        self.saveDefaults.setText(QtGui.QApplication.translate("DialogOptions", "&Save Defaults", None, QtGui.QApplication.UnicodeUTF8))

