# # from PyQt5.QWidgets import QApplication, QLabel 
# # import sys

# # app = QApplication(sys.argv)
# # label = QLabel("test")
# # label.show()
# # sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
#     QGroupBox, QPushButton, QCheckBox, QComboBox, QRadioButton, 
#     QProgressBar, QSlider, QDial, QLineEdit, QTextEdit, QLabel,
#     QTabWidget, QGridLayout, QMenuBar, QAction, QFrame
# )
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5")
#         self.resize(1200, 700)

#         mainLayout = QHBoxLayout()
#         layout1 = QVBoxLayout()
#         layout2 = QHBoxLayout()
#         layout3 = QHBoxLayout()
#         layout4 = QHBoxLayout()

#         central = QWidget()
#         self.setCentralWidget(central)
#         central.setLayout(mainLayout)
#         mainLayout.addLayout(layout1)
#         mainLayout.addLayout(layout2)
#         mainLayout.addLayout(layout3)
#         mainLayout.addLayout(layout4)

#         button1 = QPushButton("click", self)
#         button2 = QPushButton("click", self)

#         layout1.addWidget(button1)
#         layout1.addWidget(button2)

#         # central = QWidget()
#         # self.setCentralWidget(central)

#         # layout = QVBoxLayout()
#         # central.setLayout(layout)

#         # label = QLabel("Hi, I'm doing something here")
#         # btn_changeText = QPushButton("Click me to change text", self)
#         # btn = QPushButton("Click me", self)

#         # btn_changeText.clicked.connect(lambda: label.setText("This text got changed"))
#         # btn.clicked.connect(self.on_click)

#         # layout.addWidget(label)
#         # layout.addWidget(btn_changeText)
#         # layout.addWidget(btn)
        
#     def on_click(self):
#         print("This button is clicked")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel, QComboBox, QProgressBar
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(facecolor='#19232D')
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        self.ax.set_facecolor('#19232D')
        self.ax.tick_params(colors='white')
        self.ax.spines[:].set_color('white')
        self.plot_data()

    def plot_data(self):
        x = np.arange(1, 11)
        y1 = np.random.randint(2, 10, size=10)
        y2 = np.random.randint(1, 8, size=10)

        self.ax.fill_between(x, y1, color='#2ECC71', alpha=0.6)
        self.ax.fill_between(x, y2, color='#E67E22', alpha=0.8)
        self.ax.plot(x, y1, color='white', lw=1)
        self.ax.plot(x, y2, color='white', lw=1)
        self.draw()


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Dashboard Example")
        self.resize(900, 500)
        self.set_dark_theme()

        main_layout = QHBoxLayout()
        control_panel = self.create_controls()
        chart = MatplotlibWidget(self)

        main_layout.addLayout(control_panel, 1)
        main_layout.addWidget(chart, 3)
        self.setLayout(main_layout)

    def create_controls(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        layout.addWidget(QLabel("Controls"))
        layout.addWidget(QPushButton("Start"))
        layout.addWidget(QPushButton("Stop"))

        combo = QComboBox()
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(combo)

        layout.addWidget(QLabel("Progress"))
        progress = QProgressBar()
        progress.setValue(70)
        layout.addWidget(progress)

        layout.addWidget(QLabel("Adjust Value"))
        slider = QSlider(Qt.Horizontal)
        layout.addWidget(slider)

        return layout

    def set_dark_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#19232D"))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor("#1E1E1E"))
        palette.setColor(QPalette.AlternateBase, QColor("#19232D"))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor("#2E3440"))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Highlight, QColor("#5294E2"))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
