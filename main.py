import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from Ui_tuto import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("tuto.ui", self)
        
# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self, *args, obj=None, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()