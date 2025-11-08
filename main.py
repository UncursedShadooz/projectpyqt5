import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QProgressBar,
    QGridLayout, QCheckBox, QRadioButton, QSpinBox, QDoubleSpinBox, QLineEdit, QFrame
)
from PyQt5.QtCore import Qt
# import matplotlib.pyplot as plt
# import numpy as np

# # years (x)
# years = np.arange(2000, 2011 + 1)

# us =     [3, 1, 0, 0, 1, 0, 1, 3, 0, 0, 0, 0]
# russian = [0, 0, 1, 0, 0, 0, 0, 1, 4, 0, 0, 0]
# taiwan =  [2, 1, 0, 3, 0, 1, 1, 0, 0, 2, 2, 1]

# plt.figure(figsize=(10, 6))
# plt.stackplot(years, us, russian, taiwan, labels=["The U.S.", "Russian", "Taiwan"],
#               colors=["#2ca02c", "#1f77b4", "#ff7f0e"], alpha=0.8)

# plt.legend(loc="upper left")
# plt.title("Stacked Area Chart Example")
# plt.xlabel("Year")
# plt.ylabel("Value")
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.show()

# customizes all of the panels
class BlockFrame(QFrame):
    def __init__(self, label_text="Block", content_type="button"):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: #3b3b3b;
                border: 2px solid black;
                border-radius: 5px;
            }
            QPushButton, QCheckBox, QRadioButton, QComboBox, QSpinBox, QDoubleSpinBox, QLineEdit {
                background-color: #5a5a5a;
                color: white;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #777;
            }
            QLabel {
                color: white;
            }
        """)
        self.setMinimumSize(150, 250)
        self.label_text = label_text

        layout = QVBoxLayout(self)

        # label
        label = QLabel(label_text)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # different types of content
        if content_type == "button":
            self.button = QPushButton("Click Me")
            self.button.clicked.connect(self.on_button_click)
            layout.addWidget(self.button)

        elif content_type == "checkbox":
            self.checkbox = QCheckBox("Enable Feature")
            self.checkbox.stateChanged.connect(self.on_checkbox_change)
            layout.addWidget(self.checkbox)

        elif content_type == "dropdown":
            self.combo = QComboBox()
            self.combo.addItems(["Option 1", "Option 2", "Option 3"])
            self.combo.currentIndexChanged.connect(self.on_dropdown_change)
            layout.addWidget(self.combo)

        elif content_type == "spinbox":
            self.spin = QSpinBox()
            self.spin.setRange(0, 100)
            self.spin.valueChanged.connect(self.on_spin_change)
            layout.addWidget(self.spin)

            self.double_spin = QDoubleSpinBox()
            self.double_spin.setRange(0, 10)
            self.double_spin.setSingleStep(0.1)
            self.double_spin.valueChanged.connect(self.on_double_spin_change)
            layout.addWidget(self.double_spin)

        elif content_type == "radiobutton":
            self.radio1 = QRadioButton("Option A")
            self.radio2 = QRadioButton("Option B")
            self.radio1.toggled.connect(self.on_radio_change)
            self.radio2.toggled.connect(self.on_radio_change)
            layout.addWidget(self.radio1)
            layout.addWidget(self.radio2)

        elif content_type == "progress":
            self.progress = QProgressBar()
            self.progress.setRange(0, 100)
            self.progress.setValue(70)
            self.progress.setTextVisible(False)
            layout.addWidget(self.progress)

        elif content_type == "comboboxes":
            self.combo1 = QComboBox()
            self.combo1.addItems(["Red", "Green", "Blue"])
            self.combo2 = QComboBox()
            self.combo2.addItems(["Small", "Medium", "Large"])
            layout.addWidget(self.combo1)
            layout.addWidget(self.combo2)

        elif content_type == "textinput":
            self.text = QLineEdit()
            self.text.setPlaceholderText("Type here...")
            self.text.textChanged.connect(self.on_text_change)
            layout.addWidget(self.text)

        else:
            info = QLabel("(Empty)")
            info.setAlignment(Qt.AlignCenter)
            layout.addWidget(info)

        layout.addStretch()

    # interaction handlers
    def on_button_click(self):
        print(f"{self.label_text} button clicked!")

    def on_checkbox_change(self, state):
        print(f"{self.label_text} checkbox = {'Checked' if state else 'Unchecked'}")

    def on_dropdown_change(self, index):
        print(f"{self.label_text} -> Option {index + 1}")

    def on_spin_change(self, value):
        print(f"{self.label_text} spinbox = {value}")

    def on_double_spin_change(self, value):
        print(f"{self.label_text} double spinbox = {value:.1f}")

    def on_radio_change(self):
        sender = self.sender()
        if sender.isChecked():
            print(f"{self.label_text} selected {sender.text()}")

    def on_text_change(self, text):
        print(f"{self.label_text} text: {text}")


# sets up the main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project PyQt5")
        self.resize(1000, 600)

        # main layout
        main_layout = QHBoxLayout(self)

        # left panel
        left_panel = QWidget()
        left_panel.setStyleSheet("background-color: gray; border: 2px solid black;")
        grid = QGridLayout(left_panel)
        grid.setSpacing(10)

        # 8 boxes as requested
        blocks = [
            BlockFrame("Box 1", "button"),
            BlockFrame("Box 2", "checkbox"),
            BlockFrame("Box 3", "dropdown"),
            BlockFrame("Box 4", "spinbox"),
            BlockFrame("Box 5", "radiobutton"),
            BlockFrame("Box 6", "progress"),
            BlockFrame("Box 7", "comboboxes"),
            BlockFrame("Box 8", "textinput"),
        ]

        for i, block in enumerate(blocks):
            grid.addWidget(block, i // 4, i % 4)

        # Right chart panel placeholder
        chart_panel = QWidget()
        chart_panel.setStyleSheet("background-color: gray; border: 2px solid black;")
        chart_panel.setMinimumWidth(300)

        # Add panels to layout
        main_layout.addWidget(left_panel, 3)
        main_layout.addWidget(chart_panel, 2)

# executes the code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
