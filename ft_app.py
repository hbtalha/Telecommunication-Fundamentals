import sys
# python.exe -m pip install pyside6
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from Mod1.units_conversion import ConversaoWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)

        self.conversionWindow = ConversaoWindow()

        self.init_gui()
        self.connect_buttons()

        self.setFixedSize(696, 120)
        self.setWindowTitle('FT App')

    def init_gui(self):
        self.buttonGroup = QGroupBox()

        self.label = QLabel('Telecommunication Fundamentals\n')

        self.conversion_window_button = QPushButton('Unit Conversions')
        self.power_multiple_sections_window_button = QPushButton('Powers in multiple sections')
        self.SystemsSpectrumWindowButton = QPushButton('Systems Spectrum and ...')
        self.probabilityNoiseWindowButton = QPushButton('Noise and Probability')
        self.scanningWindowButton = QPushButton('Scanning')
        self.MultiplexingWindowButton = QPushButton('Multiplexing')
        self.sourceEncodingWindowButton = QPushButton('Source Encoding')
        self.channelEncodingWindowButton = QPushButton('Channel Encoding')

        BUTTON_WIDTH = 160
        self.conversion_window_button.setFixedWidth(BUTTON_WIDTH)
        self.power_multiple_sections_window_button.setFixedWidth(BUTTON_WIDTH)
        self.SystemsSpectrumWindowButton.setFixedWidth(BUTTON_WIDTH)
        self.probabilityNoiseWindowButton.setFixedWidth(BUTTON_WIDTH)
        self.scanningWindowButton.setFixedWidth(BUTTON_WIDTH)
        self.MultiplexingWindowButton.setFixedWidth(BUTTON_WIDTH)
        self.sourceEncodingWindowButton.setFixedWidth(BUTTON_WIDTH)
        self.channelEncodingWindowButton.setFixedWidth(BUTTON_WIDTH)

        labelLayout = QHBoxLayout()
        hBoxLayout = QHBoxLayout()
        hBoxLayout1 = QHBoxLayout()
        vBoxLayout1 = QVBoxLayout()

        labelLayout.addStretch()
        labelLayout.addWidget(self.label)
        labelLayout.addStretch()

        hBoxLayout.addWidget(self.conversion_window_button)
        hBoxLayout.addWidget(self.power_multiple_sections_window_button)
        hBoxLayout.addWidget(self.SystemsSpectrumWindowButton)
        hBoxLayout.addWidget(self.probabilityNoiseWindowButton)

        hBoxLayout1.addWidget(self.scanningWindowButton)
        hBoxLayout1.addWidget(self.MultiplexingWindowButton)
        hBoxLayout1.addWidget(self.sourceEncodingWindowButton)
        hBoxLayout1.addWidget(self.channelEncodingWindowButton)

        vBoxLayout1.addLayout(labelLayout)
        vBoxLayout1.addLayout(hBoxLayout)
        vBoxLayout1.addLayout(hBoxLayout1)

        self.buttonGroup.setLayout(vBoxLayout1)

        layout = QHBoxLayout()
        layout.addWidget(self.buttonGroup)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

    def connect_buttons(self):
        self.conversion_window_button.clicked.connect(self.abrir_conversao)

    def abrir_conversao(self):
        if not self.conversionWindow.isVisible():
            self.conversionWindow.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
