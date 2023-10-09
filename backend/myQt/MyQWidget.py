import re
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QDialog, QDialogButtonBox, QLabel

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class CustomDialog(QDialog):
    def __init__(self, message="CustomDialog", parent=None, children=None):
        super().__init__(parent)

        self.setWindowTitle("Graphics")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        if isinstance(message, list):
            for msg in message:
                self.layout.addWidget(QLabel(msg))
        else:
            self.layout.addWidget(QLabel(message))
        if isinstance(children, list):
            hbox = QHBoxLayout()
            for child in children:
                hbox.addWidget(child)
            self.layout.addLayout(hbox)
        else:
            self.layout.addWidget(children)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, y_xis, x_xis=None, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        if x_xis is None:
            x_xis = [i for i in range(1, len(y_xis) + 1)]
        # print("MplCanvas")
        # print(x_xis)
        # print(y_xis)
        self.axes.bar(x_xis, y_xis)
        # self.axes.plot(x_xis, y_xis)
        super(MplCanvas, self).__init__(fig)


class MyQLineEdit(QLineEdit):
    def __init__(self, password="Pa$$w0rd.onl1ne", wg=None):
        self.wg = wg
        self.password = password
        self.count_error = 0
        self.num_char = []
        self.char = {}
        # self.graph = 0
        super().__init__(wg)
        self.setFocus()

    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        text = self.text()
        # print(text)
        if text and not text[-1] == self.password[len(text) - 1]:
            self.count_error += 1
            self.num_char.append(len(text))
            if text[-1] in self.char:
                self.char[text[-1]] += 1
            else:
                self.char[text[-1]] = 1


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    m = QWidget()

    vbox = QVBoxLayout()
    ql = MyQLineEdit()
    vbox.addWidget(ql)

    hbox = QHBoxLayout()
    gr = MplCanvas([1, 2, 3], [3, 4, 1], width=4, height=3)
    gr2 = MplCanvas([1, 2, 3], [3, 4, 1], width=4, height=3)
    hbox.addWidget(gr)
    hbox.addWidget(gr2)

    vbox.addLayout(hbox)

    m.setLayout(vbox)
    m.show()
    sys.exit(app.exec_())
