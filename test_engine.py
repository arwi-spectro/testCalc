
from calcEngine import BasicEngine
from caclWidget import MainWindow
from pytestqt import qtbot
from pytestqt.qt_compat import qt_api
from PyQt6 import QtCore
import pytest
import sys

engine = BasicEngine()


@pytest.mark.backend
def test_multiple_add():
    result = engine.evaluate("21+42+55+98819128+1221+34")
    assert result == str(float((21 + 42 + 55 + 98819128 + 1221 + 34)))

@pytest.mark.backend
def test_single_add():
    result = engine.evaluate("214255988+19128122134")
    assert result == str(float((214255988 + 19128122134)))


def test_numbers(qtbot):
    window = MainWindow()
    engine = BasicEngine()
    qtbot.addWidget(window)
    window.show()
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
    # sleep(2)
    expression = ""
    for key in numpad.keys():
        expression+=key
        qtbot.mouseClick(numpad[key], QtCore.Qt.MouseButton.LeftButton)
        assert window.ui.lineEdit.text() == expression
    assert window.ui.lineEdit.text() == "5+3/1-9*847260"
    qtbot.mouseClick(window.ui.pushButton_15, QtCore.Qt.MouseButton.LeftButton)
    assert window.ui.lineEdit.text() == engine.evaluate(expression)
    qtbot.mouseClick(window.ui.pushButton_16, QtCore.Qt.MouseButton.LeftButton)
    assert window.ui.lineEdit.text() == ""


def test_basics(qtbot):
    """
    Basic test that works more like a sanity check to ensure we are setting up a QApplication
    properly and are able to display a simple event_recorder.
    """
    assert qt_api.QtWidgets.QApplication.instance() is not None
    widget = qt_api.QtWidgets.QWidget()
    #qt_api.set_qt_api("pyqt6")
    qtbot.addWidget(widget)
    widget.setWindowTitle("W1")
    widget.show()
    #assert qt_api.is_pyside == True
    assert widget.isVisible()
    assert widget.windowTitle() == "W1"
