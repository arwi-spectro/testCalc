import sys
from caclWidget import MainWindow
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
