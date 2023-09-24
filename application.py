import string
import tkinter

import customtkinter
from CTkMessagebox import CTkMessagebox
from password_generator import Password_generator

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        self.count = 0
        self.f_key_press = False
        self.s_key_press = False
        self.password_generator = None

        super().__init__()
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{480}x{400}")


        self.tabview = customtkinter.CTkTabview(self, width=435, height=300)
        self.tabview.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")


        self.tabview.add("Generate password")
        self.tabview.tab("Generate password").grid_columnconfigure(0, weight=1)

        self.check_box_a_z = customtkinter.CTkCheckBox(master=self.tabview.tab("Generate password"), text="a - z")
        self.check_box_A_Z = customtkinter.CTkCheckBox(master=self.tabview.tab("Generate password"), text="A - Z")
        self.check_box_0_9 = customtkinter.CTkCheckBox(master=self.tabview.tab("Generate password"), text="0 - 9")
        self.check_box_special_cymbol = customtkinter.CTkCheckBox(master=self.tabview.tab("Generate password"), text="!@#$%^&*()?")
        self.entry_other = customtkinter.CTkEntry(master=self.tabview.tab("Generate password"), placeholder_text="U'r cymbols", width=200)

        self.check_box_a_z.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")
        self.check_box_A_Z.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.check_box_0_9.grid(row=0, column=1, padx=20, pady=5, sticky="w")
        self.check_box_special_cymbol.grid(row=1, column=1, padx=20, pady=5, sticky="w")
        self.entry_other.grid(row=3, column=0, padx=20, pady=20,sticky="w")


        self.entry_password = customtkinter.CTkEntry(master=self.tabview.tab("Generate password"), placeholder_text="Generated password", width=200)
        self.optionemenu_size = customtkinter.CTkComboBox(master=self.tabview.tab("Generate password"), values=[str(i*10) for i in range(1, 10)])
        self.button_generate = customtkinter.CTkButton(master=self.tabview.tab("Generate password"), command=self.execute, text="Generate")

        self.entry_password.grid(row=5, column=0, padx=20, pady=(50, 5), sticky="w")
        self.optionemenu_size.grid(row=3, column=1, padx=20, pady=20, sticky="w")
        self.button_generate.grid(row=5, column=1, padx=20, pady=(50, 5), sticky="w")



        self.tabview.add("Test")
        self.tabview.tab("Test").grid_columnconfigure(0, weight=1)

        self.password_label = customtkinter.CTkLabel(master=self.tabview.tab("Test"), text="Entering a phrase", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.entry_test = customtkinter.CTkEntry(master=self.tabview.tab("Test"), placeholder_text="Enter words", width=200)
        self.label_count = customtkinter.CTkLabel(master=self.tabview.tab("Test"), text="Count: 0", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.button_clear = customtkinter.CTkButton(master=self.tabview.tab("Test"), command=self.clear, text="Clear")

        self.password_label.grid(row=0, column=0, padx=20, pady=10,  sticky="w")
        self.entry_test.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.label_count.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.button_clear.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)

    def key_press(self, event):

        if not self.f_key_press:
            self.f_key_press = True
        elif not self.s_key_press:
            self.s_key_press = True
            self.count+=1
            self.set_lbl()
        else:
            self.f_key_press = False
            self.s_key_press = False

    def key_release(self, event):
        if self.s_key_press:
            self.s_key_press = False
        elif self.f_key_press:
            self.f_key_press = False

    def clear(self):
        self.count = 0
        self.set_lbl()
        self.entry_test.grid_forget()
        self.entry_test = customtkinter.CTkEntry(master=self.tabview.tab("Test"), placeholder_text="Enter words", width=200)
        self.entry_test.grid(row=1, column=0, padx=20, pady=10, sticky="w")


    def set_lbl(self):
        self.label_count.grid_forget()
        self.label_count = customtkinter.CTkLabel(master=self.tabview.tab("Test"), text="Count: {}".format(self.count), font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_count.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.update()

    def execute(self):
        cymbols = ''
        if self.check_box_a_z.get():
            cymbols += string.ascii_lowercase
        if self.check_box_A_Z.get():
            cymbols += string.ascii_uppercase
        if self.check_box_0_9.get():
            cymbols += string.digits
        if self.check_box_special_cymbol.get():
            cymbols += string.punctuation
        cymbols+=self.entry_other.get()


        try:
            int(self.optionemenu_size.get())
        except:
            CTkMessagebox(title="Error", message='Password length must be int', icon="cancel")
            return

        self.password_generator = Password_generator(cymbols, int(self.optionemenu_size.get())
)
        password = self.password_generator.generate()
        if isinstance(password, str):
            self.entry_password.delete(0, tkinter.END)
            self.entry_password.insert(0, password)
        else:
            CTkMessagebox(title="Error", message=password().__str__(), icon="cancel")







