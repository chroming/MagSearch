# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mag_search.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(1087, 529)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		MainWindow.setMinimumSize(QtCore.QSize(1087, 529))
		MainWindow.setMaximumSize(QtCore.QSize(1087, 529))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.input_lineedit = QtGui.QLineEdit(self.centralwidget)
		self.input_lineedit.setGeometry(QtCore.QRect(12, 15, 715, 20))
		self.input_lineedit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.input_lineedit.setObjectName(_fromUtf8("input_lineedit"))
		self.search_pushbutton = QtGui.QPushButton(self.centralwidget)
		self.search_pushbutton.setGeometry(QtCore.QRect(738, 15, 75, 22))
		self.search_pushbutton.setObjectName(_fromUtf8("search_pushbutton"))
		self.result_treewidget = QtGui.QTreeWidget(self.centralwidget)
		self.result_treewidget.setGeometry(QtCore.QRect(12, 54, 802, 415))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.result_treewidget.sizePolicy().hasHeightForWidth())
		self.result_treewidget.setSizePolicy(sizePolicy)
		self.result_treewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.result_treewidget.setObjectName(_fromUtf8("result_treewidget"))
		self.result_treewidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
		self.result_treewidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
		self.result_treewidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
		self.result_treewidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
		self.result_treewidget.header().setVisible(True)
		self.result_treewidget.header().setCascadingSectionResizes(False)
		self.result_treewidget.header().setDefaultSectionSize(200)
		self.result_treewidget.header().setHighlightSections(True)
		self.result_treewidget.header().setSortIndicatorShown(True)
		self.result_treewidget.header().setStretchLastSection(False)
		self.filter_lineedit = QtGui.QLineEdit(self.centralwidget)
		self.filter_lineedit.setGeometry(QtCore.QRect(831, 54, 157, 20))
		self.filter_lineedit.setObjectName(_fromUtf8("filter_lineedit"))
		self.use_filter_checkbox = QtGui.QCheckBox(self.centralwidget)
		self.use_filter_checkbox.setGeometry(QtCore.QRect(1002, 54, 70, 19))
		self.use_filter_checkbox.setObjectName(_fromUtf8("use_filter_checkbox"))
		self.less_than_lineedit = QtGui.QLineEdit(self.centralwidget)
		self.less_than_lineedit.setGeometry(QtCore.QRect(948, 87, 28, 20))
		self.less_than_lineedit.setObjectName(_fromUtf8("less_than_lineedit"))
		self.more_than_lineedit = QtGui.QLineEdit(self.centralwidget)
		self.more_than_lineedit.setGeometry(QtCore.QRect(864, 87, 28, 19))
		self.more_than_lineedit.setObjectName(_fromUtf8("more_than_lineedit"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(831, 87, 34, 19))
		self.label.setObjectName(_fromUtf8("label"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(915, 87, 34, 19))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.size_limit_checkbox = QtGui.QCheckBox(self.centralwidget)
		self.size_limit_checkbox.setGeometry(QtCore.QRect(1002, 87, 67, 22))
		self.size_limit_checkbox.setObjectName(_fromUtf8("size_limit_checkbox"))
		self.source_treewidget = QtGui.QTreeWidget(self.centralwidget)
		self.source_treewidget.setEnabled(False)
		self.source_treewidget.setGeometry(QtCore.QRect(828, 153, 240, 313))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.source_treewidget.sizePolicy().hasHeightForWidth())
		self.source_treewidget.setSizePolicy(sizePolicy)
		self.source_treewidget.setObjectName(_fromUtf8("source_treewidget"))
		self.source_treewidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
		self.source_treewidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
		self.source_treewidget.header().setDefaultSectionSize(50)
		self.label_3 = QtGui.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(828, 132, 130, 16))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.label_4 = QtGui.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(897, 87, 16, 19))
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.label_5 = QtGui.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(981, 87, 16, 19))
		self.label_5.setObjectName(_fromUtf8("label_5"))
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.menuBar = QtGui.QMenuBar(MainWindow)
		self.menuBar.setEnabled(False)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 1087, 23))
		self.menuBar.setObjectName(_fromUtf8("menuBar"))
		MainWindow.setMenuBar(self.menuBar)
		self.action = QtGui.QAction(MainWindow)
		self.action.setObjectName(_fromUtf8("action"))
		self.action_2 = QtGui.QAction(MainWindow)
		self.action_2.setObjectName(_fromUtf8("action_2"))

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MagSearch", None))
		self.search_pushbutton.setText(_translate("MainWindow", "搜索", None))
		self.result_treewidget.headerItem().setText(0, _translate("MainWindow", "名称", None))
		self.result_treewidget.headerItem().setText(1, _translate("MainWindow", "大小", None))
		self.result_treewidget.headerItem().setText(2, _translate("MainWindow", "链接", None))
		self.result_treewidget.headerItem().setText(3, _translate("MainWindow", "来源", None))
		self.use_filter_checkbox.setText(_translate("MainWindow", "名称包含", None))
		self.label.setText(_translate("MainWindow", "大于:", None))
		self.label_2.setText(_translate("MainWindow", "小于:", None))
		self.size_limit_checkbox.setText(_translate("MainWindow", "大小限制", None))
		self.source_treewidget.headerItem().setText(0, _translate("MainWindow", "启用", None))
		self.source_treewidget.headerItem().setText(1, _translate("MainWindow", "名称", None))
		self.label_3.setText(_translate("MainWindow", "来源选项:(待添加功能)", None))
		self.label_4.setText(_translate("MainWindow", "MB", None))
		self.label_5.setText(_translate("MainWindow", "MB", None))
		self.action.setText(_translate("MainWindow", "配置源", None))
		self.action_2.setText(_translate("MainWindow", "导入配置", None))

import source_rc
