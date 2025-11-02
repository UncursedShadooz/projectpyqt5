import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel, QComboBox, QProgressBar
)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# import matplotlib
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import numpy as np

# customizes all of the panels
class BlockFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: #3b3b3b;
                border: 2px solid black;
            }
        """)
        self.setMinimumSize(150, 250)


# sets up the main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project PyQt5")
        self.resize(900, 400)

        # main layout
        main_layout = QHBoxLayout(self)

        # left panel
        left_panel = QWidget()
        left_panel.setStyleSheet("background-color: gray; border: 2px solid black;")
        grid = QGridLayout(left_panel)
        grid.setSpacing(10)

        # Add 3 or 6 dark blocks
        blocks = [BlockFrame() for i in range(6)]  # change to 6 for two rows
        
        for i, block in enumerate(blocks):
            grid.addWidget(block, i // 3, i % 3)   

        # Right green chart panel
        chart_panel = QWidget()
        chart_panel.setStyleSheet("background-color: gray; border: 2px solid black;")
        chart_panel.setMinimumWidth(300)

        # Add panels to layout
        main_layout.addWidget(left_panel, 3)  # stretch factor bigger
        main_layout.addWidget(chart_panel, 2)

# class MatplotlibWidget(FigureCanvas):
#     def __init__(self, parent=None):
#         fig = Figure(facecolor='#19232D')
#         super().__init__(fig)
#         self.ax = fig.add_subplot(111)
#         self.ax.set_facecolor('#19232D')
#         self.ax.tick_params(colors='white')
#         self.ax.spines[:].set_color('white')
#         self.plot_data()

#     def plot_data(self):
#         x = np.arange(1, 11)
#         y1 = np.random.randint(2, 10, size=10)
#         y2 = np.random.randint(1, 8, size=10)

#         self.ax.fill_between(x, y1, color='#2ECC71', alpha=0.6)
#         self.ax.fill_between(x, y2, color='#E67E22', alpha=0.8)
#         self.ax.plot(x, y1, color='white', lw=1)
#         self.ax.plot(x, y2, color='white', lw=1)
#         self.draw()


# class Dashboard(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Dashboard Example")
#         self.resize(900, 500)
#         self.set_dark_theme()

#         main_layout = QHBoxLayout()
#         control_panel = self.create_controls()
#         chart = MatplotlibWidget(self)

#         main_layout.addLayout(control_panel, 1)
#         main_layout.addWidget(chart, 3)
#         self.setLayout(main_layout)

#     def create_controls(self):
#         layout = QVBoxLayout()
#         layout.setAlignment(Qt.AlignTop)

#         layout.addWidget(QLabel("Controls"))
#         layout.addWidget(QPushButton("Start"))
#         layout.addWidget(QPushButton("Stop"))

#         combo = QComboBox()
#         combo.addItems(["Option 1", "Option 2", "Option 3"])
#         layout.addWidget(combo)

#         layout.addWidget(QLabel("Progress"))
#         progress = QProgressBar()
#         progress.setValue(30)
#         layout.addWidget(progress)

#         layout.addWidget(QLabel("Adjust Value"))
#         slider = QSlider(Qt.Horizontal)
#         layout.addWidget(slider)

#         return layout
    
#     #palette for the gui
#     def set_dark_theme(self):
#         palette = QPalette()
#         palette.setColor(QPalette.Window, QColor("#19232D"))
#         palette.setColor(QPalette.WindowText, Qt.white)
#         palette.setColor(QPalette.Base, QColor("#1E1E1E"))
#         palette.setColor(QPalette.AlternateBase, QColor("#19232D"))
#         palette.setColor(QPalette.ToolTipBase, Qt.white)
#         palette.setColor(QPalette.ToolTipText, Qt.white)
#         palette.setColor(QPalette.Text, Qt.white)
#         palette.setColor(QPalette.Button, QColor("#2E3440"))
#         palette.setColor(QPalette.ButtonText, Qt.white)
#         palette.setColor(QPalette.BrightText, Qt.red)
#         palette.setColor(QPalette.Highlight, QColor("#5294E2"))
#         palette.setColor(QPalette.HighlightedText, Qt.black)
#         self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
