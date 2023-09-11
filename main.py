#!/usr/bin/python3
import io
import logging
import os
import threading
import time
from collections.abc import Iterable
import tkinter as tk
from datetime import datetime
from tkinter import ttk
import keyboard
from repository import insert_values_in_table_authorized_users
from alphabet_module import assemble_alphabet
from access_code_module import AccessCode

with open('logfile.log', mode='w') as logfile:
    pass

logging.basicConfig(filename='logfile.log',
                    encoding='cp1251',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


def save_and_register_access_code(path: str, access_code: AccessCode, metrics: Iterable[float, float, float]) -> bool:
    try:
        dirs = path.split('/')[:-1]

        new_dirs = io.StringIO()
        for d in dirs:
            new_dirs.write(f'{d}/')
            if not os.path.exists(new_dirs.getvalue()):
                os.makedirs(new_dirs.getvalue())
    except Exception as e:
        logging.exception(e)
    try:
        with open(path, mode='w', encoding='utf-8') as file:
            file.write(access_code.value)

        insert_values_in_table_authorized_users(access_code.hashed_value,
                                                access_code.creation_date,
                                                access_code.expiration_date,
                                                metrics)
        return True
    except Exception as e:
        logging.exception(e)


def create_main_window_generation_access_code():
    logging.info('Создание начального окна!')
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - root.winfo_reqwidth() - 400) / 2
    y = (screen_height - root.winfo_reqheight() - 400) / 2

    root.geometry('600x500+%d+%d' % (x, y))

    title_1 = tk.Label(root, text='\naccess_code generator\n')
    title_1.pack()

    label1 = tk.Label(root, text='Lower case?')
    label1.pack()

    values1 = {'yes': 'LOWER_CASE', 'no': None}
    combo1 = ttk.Combobox(root, values=list(values1.keys()))
    combo1.pack()

    label2 = tk.Label(root, text='Upper case?')
    label2.pack()

    values2 = {'yes': 'UPPER_CASE', 'no': None}
    combo2 = ttk.Combobox(root, values=list(values2.keys()))
    combo2.pack()

    label3 = tk.Label(root, text='Digits?')
    label3.pack()

    values3 = {'yes': 'DIGITS', 'no': None}
    combo3 = ttk.Combobox(root, values=list(values3.keys()))
    combo3.pack()

    label4 = tk.Label(root, text='Punctuation?')
    label4.pack()

    values4 = {'yes': 'PUNCTUATION', 'no': None}
    combo4 = ttk.Combobox(root, values=list(values4.keys()))
    combo4.pack()

    label4 = tk.Label(root, text='Length:')
    label4.pack()

    entry1 = tk.Entry(root)
    entry1.pack()

    def generation(length: int, *alphabets: Iterable) -> AccessCode:
        my_alphabet: str = assemble_alphabet(alphabets)
        logging.info('Пароль начал генерацию!')
        return AccessCode(my_alphabet, length)

    s = tk.Label(root, padx=15, pady=15)
    s.pack(fill=tk.NONE, expand=True)

    access_code: AccessCode = None

    def generate_access_code():
        nonlocal access_code
        access_code = generation(int(entry1.get()),
                                 values1[combo1.get()],
                                 values2[combo2.get()],
                                 values3[combo3.get()],
                                 values4[combo4.get()])
        s.config(text=access_code.value)

    button1 = tk.Button(root, text='Generate the access code', command=generate_access_code)
    button1.pack(fill=tk.NONE, expand=True)

    class RegisterWindow(tk.Toplevel):
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent
            self.title("Password Register")
            self.geometry("300x200")
            self.password = ""
            self.start_time = 0
            self.end_time = 0
            self.interval_list = []
            self.error_count = 0

            self.input_field = tk.Entry(self)
            self.input_field.pack(pady=10)
            self.input_field.focus_set()

            self.bind("<Key>", self.on_key_press)
            self.bind("<Return>", self.on_enter_press)

        def on_key_press(self, event):
            if event.keysym == "BackSpace":
                if len(self.password) > 0:
                    self.password = self.password[:-1]
                else:
                    self.error_count += 1
            else:
                self.password += event.char
            if len(self.password) == 1:
                self.start_time = time.time()
            elif len(self.password) > 1:
                self.interval_list.append(time.time() - self.end_time)
            self.end_time = time.time()

        def on_enter_press(self, event):
            self.parent.clipboard_clear()
            self.parent.clipboard_append(self.password)
            self.destroy()

        def wait_for_typing(self):
            self.grab_set()
            self.wait_window()

    def register_and_save():
        window = RegisterWindow(root)
        window.wait_for_typing()
        print("Password:", window.password)
        print("Start Time:", window.start_time)
        print("End Time:", window.end_time)
        print("Interval List:", window.interval_list)
        print("Error Count:", window.error_count)

    button_register = tk.Button(root, text='Register and save as', command=lambda: register_and_save)
    button_register.pack(fill=tk.NONE, expand=True)

    entry = tk.Entry(root)
    entry.insert(0, 'output/your_access_code.txt')
    entry.pack(fill=tk.NONE, expand=True)

    root.mainloop()


def user_authentication(access_code):
    pass


def create_main_window_input():
    logging.info('Создание начального окна для ввода пароля!')
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - root.winfo_reqwidth() - 400) / 2
    y = (screen_height - root.winfo_reqheight() - 400) / 2

    root.geometry('600x500+%d+%d' % (x, y))

    title_1 = tk.Label(root, text='\nAuthentication\n')
    title_1.pack()

    entry1 = tk.Entry(root)
    entry1.pack()

    button1 = tk.Button(root, text='Authenticate', command=lambda: user_authentication(access_code=entry1.get()))
    button1.pack()

    title_2 = tk.Label(root, text='\nor\n')
    title_2.pack()

    button2 = tk.Button(root, text='Get access code', command=lambda: create_main_window_generation_access_code())
    button2.pack()

    root.mainloop()


if __name__ == '__main__':
    # create_main_window_input()
    insert_values_in_table_authorized_users('123', datetime.now().strftime(f'%Y/%m/%d'), datetime.now().strftime(f'%Y/%m/%d'), (6, 41, 7))
