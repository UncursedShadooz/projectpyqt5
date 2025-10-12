from PyQt5.QWidgets import QApplication, QLabel 
import sys

app = QApplication(sys.argv)
label = QLabel("PyQt5 is working!")
label.show()
sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# # Create a class for the main window
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Set window properties
#         self.setWindowTitle("My PyQt5 Window")
#         self.setGeometry(200, 200, 400, 300)

#         # Create widgets
#         self.label = QLabel("Hello, PyQt5!", self)
#         self.button = QPushButton("Click Me", self)
#         self.button.clicked.connect(self.on_click)

#         # Layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)

#         self.setLayout(layout)

#     def on_click(self):
#         self.label.setText("Button clicked!")

# # Run the app
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())
