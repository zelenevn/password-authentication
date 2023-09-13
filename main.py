#!/usr/bin/python3
import io
import logging
import os
import time
from collections.abc import Iterable
import tkinter as tk
from datetime import datetime
from enum import Enum
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


# class WindowType(Enum):
#     MAIN = 1
#     ACCESS_CODE = 2
#     METRICS_CALCULATION = 3
#
#
# class WindowFactory:
#     @staticmethod
#     def create_window(window_type):
#         if window_type == WindowType.MAIN:
#             return MainWindowForAuthentication()
#         elif window_type == WindowType.ACCESS_CODE:
#             return WindowForGenerationAccessCode()
#         elif window_type == WindowType.METRICS_CALCULATION:
#             pass
#         else:
#             raise ValueError("Invalid window type")
#
#
# class WindowForGenerationAccessCode(tk.Toplevel):
#     def __init__(self):
#         super().__init__()
#         logging.info('Создание начального окна для ввода пароля!')
#         self.__geometry(offset=(200, 250), size=(400, 400))
#         self.__content()
#         self._access_code: AccessCode | None = None
#
#     def __geometry(self, *, offset: tuple[int, int], size: tuple[int, int]):
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()
#
#         x = (screen_width - self.winfo_reqwidth() - offset[0]) / 2
#         y = (screen_height - self.winfo_reqheight() - offset[1]) / 2
#
#         self.geometry('%dx%d+%d+%d' % (size[0], size[1], x, y))
#
#     def __content(self):
#         self.lower_case_flag = tk.BooleanVar()
#         self.lower_case_check = tk.Checkbutton(text='Lower case', variable=self.lower_case_flag)
#         self.lower_case_check.pack()
#
#         self.upper_case_flag = tk.BooleanVar()
#         self.upper_case_check = tk.Checkbutton(text='Upper case', variable=self.upper_case_flag)
#         self.upper_case_check.pack()
#
#         self.digits_flag = tk.BooleanVar()
#         self.digits_check = tk.Checkbutton(text='Digits', variable=self.digits_flag)
#         self.digits_check.pack()
#
#         self.punctuation_flag = tk.BooleanVar()
#         self.punctuation_check = tk.Checkbutton(text='Punctuation', variable=self.punctuation_flag)
#         self.punctuation_check.pack()
#
#         self.length_label = tk.Label(text='Length:')
#         self.length_label.pack()
#
#         self.length_entry = tk.Entry()
#         self.length_entry.pack()
#
#         self.s = tk.Label()
#         self.s.pack(pady=15, fill=tk.NONE, expand=True)
#
#         self.generation_button = tk.Button(text='Generate the access code', command=self.__generate_an_access_code)
#         self.generation_button.pack(fill=tk.NONE, expand=True)
#
#         self.registration_button = tk.Button(text='Register and save as',
#                                              command=lambda: self.__save_and_register_access_code([1, 2, 3]))
#         self.registration_button.pack(fill=tk.NONE, expand=True)
#
#         self.path_entry = tk.Entry()
#         self.path_entry.insert(0, 'output/your_access_code.txt')
#         self.path_entry.pack(fill=tk.NONE, expand=True)
#
#     def __generate_an_access_code(self):
#         chosen_alphabets: tuple = ('LOWER_CASE' if self.lower_case_flag.get() else 'None',
#                                    'UPPER_CASE' if self.upper_case_flag.get() else 'None',
#                                    'DIGITS' if self.digits_flag.get() else 'None',
#                                    'PUNCTUATION' if self.punctuation_flag.get() else 'None')
#         my_alphabet: str = assemble_alphabet(chosen_alphabets)
#
#         my_length: int = int(self.length_entry.get())
#
#         logging.info('Код начал генерироваться!')
#         self._access_code = AccessCode(my_alphabet, my_length)
#
#         self.s.config(text=self._access_code.value)
#
#     def __save_and_register_access_code(self, metrics: Iterable[float, float, float]) -> bool | None:
#         try:
#             path = self.path_entry.get()
#
#             current_dir = io.StringIO()
#             dirs = path.split('/')[:-1]
#             for d in dirs:
#                 current_dir.write(f'{d}/')
#                 if not os.path.exists(current_dir.getvalue()):
#                     os.makedirs(current_dir.getvalue())
#
#             with open(path, mode='w', encoding='utf-8') as file:
#                 file.write(self._access_code.value)
#
#             insert_values_in_table_authorized_users(self._access_code.hash_code.hex_hash_value,
#                                                     self._access_code.hash_code.creation_date,
#                                                     self._access_code.hash_code.expiration_date,
#                                                     metrics)
#             return True
#         except Exception as e:
#             logging.exception(e)
#             return None
#
#
# class MainWindowForAuthentication(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.__geometry(offset=(200, 250), size=(400, 400))
#         self.__content()
#         logging.info('Создание начального окна для ввода пароля!')
#
#     def __geometry(self, *, offset: tuple[int, int], size: tuple[int, int]):
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()
#
#         x = (screen_width - self.winfo_reqwidth() - offset[0]) / 2
#         y = (screen_height - self.winfo_reqheight() - offset[1]) / 2
#
#         self.geometry('%dx%d+%d+%d' % (size[0], size[1], x, y))
#
#     def __content(self):
#         self.title('Authentication')
#
#         self.title_1 = tk.Label(text='Authentication')
#         self.title_1.pack(pady=5)
#
#         self.entry1 = tk.Entry()
#         self.entry1.pack(pady=10)
#
#         self.button1 = tk.Button(text='Authenticate',
#                                  command=lambda: self.__user_authentication(access_code=self.entry1.get))
#         self.button1.pack()
#
#         self.title_2 = tk.Label(text='or')
#         self.title_2.pack(pady=5)
#
#         self.button2 = tk.Button(text='Get access code',
#                                  command=lambda: self.__create_window_for_generation_the_access_code)
#         self.button2.pack()
#
#     def __create_window_for_generation_the_access_code(self):
#         window = WindowForGenerationAccessCode()
#         window.__geometry(offset=(200, 250), size=(400, 400))
#         window.__content()
#         window.mainloop()
#         # window.destroy()
#
#     def __user_authentication(self, access_code):
#         pass
#
#
# if __name__ == '__main__':
#     main = MainWindowForAuthentication()
#     main.mainloop()
    # insert_values_in_table_authorized_users('123', datetime.now().strftime(f'%Y/%m/%d'), datetime.now().strftime(f'%Y/%m/%d'), (6, 41, 7))
