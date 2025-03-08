import sys

from PyQt5.QtWidgets import QApplication

from Style import Style

if __name__ == "__main__":
    app = QApplication(sys.argv)
    style1 = Style()
    #window = HBR_Win()
    style1.show()

    sys.exit(app.exec_())