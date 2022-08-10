from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QComboBox, QPlainTextEdit, QPushButton, QVBoxLayout, QLineEdit
from PyQt5 import uic
import sys
from basic_converter import converter

class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        # Load file
        uic.loadUi('CC_QT.ui', self)

        self.setWindowTitle('Currency Converter')

        # Define Widgets
        self.input_box = self.findChild(QLineEdit, 'lineEdit')
        self.input_dropdown = self.findChild(QComboBox, 'comboBox')
        self.output_dropdown = self.findChild(QComboBox, 'comboBox_2')
        self.convert_button = self.findChild(QPushButton, 'pushButton')
        self.output_amount = self.findChild(QLabel, 'label_3')
        self.output_currency = self.findChild(QLabel, 'label_4')
        self.reset_button = self.findChild(QPushButton, 'pushButton_2')

        # Activate Conversion
        self.convert_button.clicked.connect(self.convert)
        self.reset_button.clicked.connect(self.reset)

        self.show()

    def convert(self):
        io_currency = self.input_dropdown.currentText()[-3:]
        out_currency = self.output_dropdown.currentText()[-3:]
        in_value = float(self.input_box.text())


        self.output_amount.setText(str(round(converter(io_currency, out_currency, in_value), 2)))
        self.output_currency.setText(self.output_dropdown.currentText()[:-5])
        
    def reset(self):
        self.output_amount.setText('')
        self.output_currency.setText('')
        self.input_box.clear()
        self.input_dropdown.setCurrentIndex(0)
        self.output_dropdown.setCurrentIndex(0)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()