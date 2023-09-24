import tkinter

import password
import customtkinter

from PIL import Image
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.pressed_keys = set()
        self.button = ""
        self.password = ""
        self.count = 0

        self.title("Password generator")
        self.geometry("460x400")
        self.resizable(False, False)

        self.background = customtkinter.CTkImage(dark_image=Image.open("art.png"), size=(460, 210))
        self.background_label = customtkinter.CTkLabel(master=self, text="", image=self.background)
        self.background_label.grid(row=0, column=0)

        self.password_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.entry_password = customtkinter.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = customtkinter.CTkButton(master=self.password_frame, text="Generate",
                                                    width=100, command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = customtkinter.CTkFrame(master=self, )
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), sticky="nsew")

        self.password_length_slider = customtkinter.CTkSlider(master=self.settings_frame, from_=0, to=100,
                                                              number_of_steps=100,
                                                              command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = customtkinter.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tkinter.StringVar()

        self.cb_digits = customtkinter.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var,
                                                   onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = customtkinter.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                                  onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = customtkinter.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                                  onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbols_var = tkinter.StringVar()
        self.cb_symbols = customtkinter.CTkCheckBox(master=self.settings_frame, text="@#$%",
                                                    variable=self.cb_symbols_var,
                                                    onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=2, column=3)

        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, "12")

        self.bind("<KeyPress>", self.key_pressed)
        self.bind("<KeyRelease>", self.key_released)
        self.mainloop()

    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get()
                        + self.cb_upper_var.get() + self.cb_symbols_var.get())
        return chars

    def set_password(self):
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password.Generator().create_new(length=int(self.password_length_slider.get()),
                                                                      characters=self.get_characters()))
        self.password = self.entry_password.get()
        # self.test_button_1()
        # self.get_input()

    def key_pressed(self, event):
        self.pressed_keys.add(event.keysym)
        if len(self.pressed_keys) == 2:
            self.count += 1
            print("Кол-во наложений", self.count)

    def key_released(self, event):
        self.pressed_keys.remove(event.keysym)


