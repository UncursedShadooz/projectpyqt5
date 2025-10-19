# from PyQt5.QWidgets import QApplication, QLabel 
# import sys

# app = QApplication(sys.argv)
# label = QLabel("test")
# label.show()
# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QGroupBox, QPushButton, QCheckBox, QComboBox, QRadioButton, 
    QProgressBar, QSlider, QDial, QLineEdit, QTextEdit, QLabel,
    QTabWidget, QGridLayout, QMenuBar, QAction, QFrame
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        label = QLabel("Hi, I'm doing something here")
        btn_changeText = QPushButton("Click me to change text", self)
        btn = QPushButton("Click me", self)

        btn_changeText.clicked.connect(lambda: label.setText("This text got changed"))
        btn.clicked.connect(self.on_click)

        layout.addWidget(label)
        layout.addWidget(btn_changeText)
        layout.addWidget(btn)
        
    def on_click(self):
        print("This button is clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
