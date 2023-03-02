
from calcEngine import BasicEngine
from caclWidget import MainWindow
from pytestqt.qt_compat import qt_api
from PyQt6.QtTest import QSignalSpy
from PyQt6 import QtCore
import pytest



#instantiate the backend engine, for engine testing
engine = BasicEngine()

##################################backend tests########################
@pytest.mark.backend
def test_multiple_add():
    result = engine.evaluate("21+42+55+98819128+1221+34")
    assert result == str(float((21 + 42 + 55 + 98819128 + 1221 + 34)))

@pytest.mark.backend
def test_single_add():
    result = engine.evaluate("214255988+19128122134")
    assert result == str(float((214255988 + 19128122134)))

#################################front end tests########################
def test_numbers(qtbot):
    """Test that all the numbers and keys work and the backend evaluation is
    displayed correctly.
    """
    #create a window and pass its reference to qbot fixture.
    window = MainWindow()
    engine = BasicEngine()
    qtbot.addWidget(window)
    window.show()
    # map an expression to widget names
    numpad = {
        "5": window.ui.pushButton_5,
        "+": window.ui.pushButton_11,
        "3": window.ui.pushButton_7,
        "/": window.ui.pushButton_14,
        "1": window.ui.pushButton,
        "-": window.ui.pushButton_12,
        "9": window.ui.pushButton_9,
        "*": window.ui.pushButton_13,
        "8": window.ui.pushButton_6,
        "4": window.ui.pushButton_2,
        "7": window.ui.pushButton_3,
        "2": window.ui.pushButton_4,
        "6": window.ui.pushButton_8,
        "0": window.ui.pushButton_10,
        
    }

    expression = ""
    for key in numpad.keys():
        expression+=key
        qtbot.mouseClick(numpad[key], QtCore.Qt.MouseButton.LeftButton)
        assert window.ui.lineEdit.text() == expression
    assert window.ui.lineEdit.text() == "5+3/1-9*847260" #check correct exp is type on screen
    qtbot.mouseClick(window.ui.pushButton_15, QtCore.Qt.MouseButton.LeftButton) #click on = button
    assert window.ui.lineEdit.text() == engine.evaluate(expression)  #check if value displayed matches value from backend
    qtbot.mouseClick(window.ui.pushButton_16, QtCore.Qt.MouseButton.LeftButton) #click clear button
    assert window.ui.lineEdit.text() == "" #check if the screen is cleared

def test_signal_fire(qtbot):
    """ check if a signal is fired
    """
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    spy = QSignalSpy(window.ui.pushButton_5.clicked) # a spy can be added to a signal of any object
    qtbot.mouseClick(window.ui.pushButton_5, QtCore.Qt.MouseButton.LeftButton)
    assert len(spy) == 1 #spy keeps count of the number of times the signal was fired

def test_basics(qtbot):
    """
    Basic test that works more like a sanity check to ensure we are setting up a QApplication
    properly and are able to display a simple event_recorder.
    """
    #this example uses the inbuilt widgets of qtbot just for testing purposes
    assert qt_api.QtWidgets.QApplication.instance() is not None
    widget = qt_api.QtWidgets.QWidget()
    #qt_api.set_qt_api("pyqt6")
    qtbot.addWidget(widget)
    widget.setWindowTitle("W1")
    widget.show()
    #assert qt_api.is_pyside == True
    assert widget.isVisible()
    assert widget.windowTitle() == "W1"
