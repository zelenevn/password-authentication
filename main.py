from datetime import datetime
import alphabet_gen
import password_gen
from tkinter import *
import tkinter.messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

from speed import speed_array, update_time


class SampleApp(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.geometry("400x400")
        self.frames = {}
        for F in (StartPage, Auth, Generate):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tkinter.Button(self, text="Генерация пароля",
                            command=lambda: controller.show_frame("Generate"))
        button2 = tkinter.Button(self, text="Авторизация",
                            command=lambda: controller.show_frame("Auth"))
        button1.pack()
        button2.pack()


class Auth(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        button = tkinter.Button(self, text="Вернуться на стартовую страницу",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        def plot(event):
            intervals = speed_array(start_times)
            fig = Figure(figsize=(5, 5),
                         dpi=100)
            plot1 = fig.add_subplot(111)
            plot1.plot(intervals)
            canvas = FigureCanvasTkAgg(fig,
                                       master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()
            toolbar = NavigationToolbar2Tk(canvas,
                                           self)
            toolbar.update()
            canvas.get_tk_widget().pack()


        # Функция для обновления времени начала ввода буквы
        def update_start_time(event):
            start_times.append(update_time())

        start_times = list()
        Label(self, text='Введите пароль: ').pack()
        password = StringVar()
        entry = Entry(self, show="*", textvariable=password)
        entry.pack()
        btn = Button(self, text='График')
        btn.pack()
        entry.bind('<Key>', update_start_time)
        btn.bind('<Button>', plot)


class Generate(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        def generate_password():
            alp_get = alph.get()
            passw_get = passw.get()
            al = alphabet_gen.error_processing(alp_get)
            pssw = password_gen.error_processing(passw_get)
            if al != 0:
                Label(self, text=al).pack()
            if pssw != 0:
                Label(self, text=pssw).pack()
            if al == 0 and pssw == 0:
                res_alphabet = alphabet_gen.generate(alp_get)
                pas = password_gen.generate(passw_get, res_alphabet)
                print(pas)
                text_box.insert(END, pas)
                text_box.config(state='disabled')

        text_box = Text(
            self,
            width=40,
            height=3,
            bg = "light cyan"
        )
        button = tkinter.Button(self, text="Вернуться на стартовую страницу",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        Label(self, text="Длина алфавита: ").pack()
        alph = Entry(self)
        alph.pack()

        Label(self, text="Длина пароля: ").pack()
        passw = Entry(self)
        passw.pack()

        Button(self, text='Сгенерировать пароль', command=generate_password).pack()
        text_box.pack(expand=True)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

