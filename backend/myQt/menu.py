# menu.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from backend.myQt.MyQWidget import MplCanvas, CustomDialog, MyQLineEdit
from backend.decorators import validate_password
from backend.service import generate_password


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.warning_password = {
            "char": [],
            "num_ch": [],
            "total_er": 0,
            "option_passwd": [],
        }
        self.warning_password_count = []
        self.warning_password_symbols = []

        self.central_widget = QWidget()

        self.initializeStyle()
        self.initializeUI()

        self.setCentralWidget(self.central_widget)

        self.show()

    def initializeStyle(self):
        self.setMinimumSize(750, 450)
        self.setWindowTitle("Generate password")
        self.setObjectName("Menu")

        with open("./static/style.css", 'r') as f:
            style = f.read()
            self.setStyleSheet(style)

    def initializeUI(self):
        vbox = QVBoxLayout()

        top_vbox = QVBoxLayout()
        title_label = QLabel("Авторизация")
        title_label.setObjectName("Title")
        top_vbox.addWidget(title_label, alignment=Qt.AlignCenter)

        middle_hbox = QHBoxLayout()
        input_passwd_label = QLabel("Введите пароль:")
        self.input_passwd_lineedit = QLineEdit()
        self.input_passwd_lineedit.setMinimumHeight(50)
        self.input_passwd_lineedit.setPlaceholderText('Password.103')
        btn_delete_text_inp_pas = QPushButton("X")
        btn_delete_text_inp_pas.setFixedSize(40, 40)
        btn_delete_text_inp_pas.clicked.connect(self.event_btn_delete_text_inp_pas)
        btn_generate_passwd = QPushButton("Сгенерировать пароль")
        btn_generate_passwd.setObjectName("BtnSubmit")
        btn_generate_passwd.setFixedWidth(190)
        btn_generate_passwd.clicked.connect(self.event_btn_generate_passwd)
        middle_hbox.addWidget(input_passwd_label)
        middle_hbox.addWidget(self.input_passwd_lineedit)
        middle_hbox.addWidget(btn_delete_text_inp_pas)
        middle_hbox.addWidget(btn_generate_passwd)

        bottom_hbox = QHBoxLayout()
        btn_submit = QPushButton("Отправить")
        btn_submit.setObjectName("BtnSubmit")
        btn_submit.setFixedWidth(150)
        btn_submit.clicked.connect(self.event_btn_submit)
        bottom_hbox.addWidget(btn_submit)

        vbox.addStretch(1)
        vbox.addLayout(top_vbox)
        vbox.addStretch(2)
        vbox.addLayout(middle_hbox)
        vbox.addStretch(2)
        vbox.addLayout(bottom_hbox)
        vbox.addStretch(1)

        self.central_widget.setLayout(vbox)

    def event_btn_generate_passwd(self):
        password = str(generate_password())
        self.input_passwd_lineedit.setText(password)

    def event_btn_delete_text_inp_pas(self):
        self.input_passwd_lineedit.setText("")

    def event_btn_submit(self):
        passwd = self.input_passwd_lineedit.text()
        res = self.check_password(passwd)
        if res == "Success":
            self.show_dialog_check_password(passwd)
        else:
            self.show_warning_messagebox("Пароль не удовлетворяет требованиям")

    @validate_password
    def check_password(self, password: str):
        return password

    def show_dialog_check_password(self, passwd):
        child = MyQLineEdit(passwd)
        msg = CustomDialog(children=child)
        retval = msg.exec_()
        input_passwd = child.text()

        if int(retval) == 0:
            return
        if str(passwd) == str(input_passwd):
            message = ["Вы успешно вошли в систему",
                       f"Общее число ошибок: {self.warning_password['total_er']}",
                       "Ошибочные пароли:"]
            for pswd in self.warning_password["option_passwd"]:
                message.append(pswd)
            self.show_info_messagebox(y_xis=self.warning_password["num_ch"],
                                      x_xis=self.warning_password["char"],
                                      message=message)
        else:
            for ch, num in child.char.items():
                self.warning_password["char"].append(ch)
                self.warning_password["num_ch"].append(num)
            self.warning_password["total_er"] += child.count_error
            self.warning_password["option_passwd"].append(input_passwd)

            self.show_warning_messagebox("Вы допустили ошибку")
            self.show_dialog_check_password(passwd)

    def show_info_messagebox(self, y_xis, x_xis=None, message: str | list = "Success"):
        child = MplCanvas(y_xis=y_xis, x_xis=x_xis, width=4, height=3)
        # child_2 = MplCanvas(y_xis=y_, x_xis=x_, width=4, height=3)
        # msg = CustomDialog(message, children=[child, child_2])
        msg = CustomDialog(message, children=child)
        retval = msg.exec_()
        # print("end___")

    def show_warning_messagebox(self, message="error"):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Warning MessageBox")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def keyPressEvent(self, e):
        """ keyboard events """
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Return:
            # print(self.input_passwd_lineedit.text())
            if self.input_passwd_lineedit.text() is not None:
                self.event_btn_submit()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    m = Menu()
    m.show()
    sys.exit(app.exec_())
