# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\j.delannoy\Documents\Artem\Dev\test\qtpy\tuto.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1100, 700))
        self.tabWidget.setMinimumSize(QtCore.QSize(1100, 700))
        self.tabWidget.setMaximumSize(QtCore.QSize(1100, 700))
        self.tabWidget.setObjectName("tabWidget")
        self.linear_tab = QtWidgets.QWidget()
        self.linear_tab.setObjectName("linear_tab")
        self.tabWidget.addTab(self.linear_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linear_tab), _translate("MainWindow", "Hello there"))
