import sys
import numpy as np

# python.exe -m pip install pyside6
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class ConversaoWindow(QWidget, QObject):
    """Builds the main window"""

    def __init__(self):
        super().__init__()

        self.setWindowModality(Qt.ApplicationModal)

        self.setWindowTitle("Unit Conversions")

        self.init_gui()

        self.isLeftValueChanging = False
        self.isRightValueChanging = False

    def init_gui(self):
        self.leftValueBox = QLineEdit()
        self.rightValueBox = QLineEdit()
        self.leftComboBox = QComboBox()
        self.rightComboBox = QComboBox()

        self.leftValueBox.setFixedSize(150, 20)
        self.rightValueBox.setFixedSize(150, 20)

        items = ['mW', "W", 'dBm', 'dBW']
        self.leftComboBox.addItems(items)
        self.rightComboBox.addItems(items)

        # only accept double values
        self.leftValueBox.setValidator(QDoubleValidator())
        self.rightValueBox.setValidator(QDoubleValidator())

        leftVBox = QVBoxLayout()
        rightVBox = QVBoxLayout()

        leftVBox.addWidget(self.leftValueBox)
        leftVBox.addWidget(self.leftComboBox)
        rightVBox.addWidget(self.rightValueBox)
        rightVBox.addWidget(self.rightComboBox)

        leftVBox.setSpacing(0)
        rightVBox.setSpacing(0)

        layout = QHBoxLayout()

        layout.addLayout(leftVBox)
        layout.addWidget(QLabel('='))
        layout.addLayout(rightVBox)

        self.setLayout(layout)
        self.setFixedSize(345, 70)

        # connects
        self.leftValueBox.textChanged.connect(self.leftValueChanged)
        self.rightValueBox.textChanged.connect(self.rightValueChanged)
        self.leftComboBox.currentIndexChanged.connect(self.comboBoxChanged)
        self.rightComboBox.currentIndexChanged.connect(self.comboBoxChanged)

    def leftValueChanged(self, value):
        """when the value in the left box is changed"""
        if self.isRightValueChanging:
            return
        if not value:
            self.rightValueBox.clear()
            return
        self.isLeftValueChanging = True
        value = (float)(value)
        fromUnit = self.leftComboBox.currentText()
        toUnit = self.rightComboBox.currentText()
        self.rightValueBox.setText(self.converter(value, fromUnit, toUnit))
        self.isLeftValueChanging = False

    def rightValueChanged(self, value):
        """when the value in the left right is changed"""
        if self.isLeftValueChanging:
            return
        if not value:
            self.leftValueBox.clear()
            return
        self.isRightValueChanging = True
        value = (float)(value)
        fromUnit = self.rightComboBox.currentText()
        toUnit = self.leftComboBox.currentText()
        self.leftValueBox.setText(self.converter(value, fromUnit, toUnit))
        self.isRightValueChanging = False

    def comboBoxChanged(self):
        """when the unit in any combobox is changed"""
        self.leftValueChanged(self.leftValueBox.text())

    def converter(self, value, fromUnit, toUnit):
        """where the conversion happens, return the converted value"""
        try:
            if fromUnit == 'mW':
                if toUnit == 'mW':
                    converted = value
                elif toUnit == 'W':
                    converted = value / 1000.0
                elif toUnit == 'dBm':
                    converted = 10 * np.log10(value)
                elif toUnit == 'dBW':
                    converted = 10 * np.log10(value / 1000.0)
            elif fromUnit == 'W':
                if toUnit == 'mW':
                    converted = value * 1000.0
                elif toUnit == 'W':
                    converted = value
                elif toUnit == 'dBm':
                    converted = 10 * np.log10(value) + 30.0
                elif toUnit == 'dBW':
                    converted = 10 * np.log10(value)
            elif fromUnit == 'dBm':
                if toUnit == 'mW':
                    converted = 10 ** (value / 10.0)
                elif toUnit == 'W':
                    converted = (10 ** (value / 10.0)) / 1000.0
                elif toUnit == 'dBm':
                    converted = value
                elif toUnit == 'dBW':
                    converted = value - 30.0
            elif fromUnit == 'dBW':
                if toUnit == 'mW':
                    converted = (10 ** (value / 10.0)) * 1000
                elif toUnit == 'W':
                    converted = 10 ** (value / 10.0)
                elif toUnit == 'dBm':
                    converted = value + 30.0
                elif toUnit == 'dBW':
                    converted = value
        except:
            converted = ''

        return (str)(converted)
