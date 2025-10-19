from PyQt5.QWidgets import QApplication, QLabel 
import sys

app = QApplication(sys.argv)
label = QLabel("test")
label.show()
sys.exit(app.exec_())
