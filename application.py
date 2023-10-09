import sys
from PyQt5.QtWidgets import QApplication

from backend.myQt.menu import Menu


def application():
    app = QApplication(sys.argv)
    m = Menu()
    m.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
