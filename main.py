import tkinter as tk
import string
import random
import time

def generate_password(length, use_english, use_russian, use_special_chars):
    characters = ''
    if use_english:
        characters += string.ascii_letters
    if use_russian:
        characters += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if use_special_chars:
        characters += string.punctuation
    if not characters:
        return "Ошибка: не выбран ни один алфавит"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password(event):
    global start_time
    entered_password = password_entry.get()

    if entered_password == generated_password:
        elapsed_time = time.time() - start_time
        result_label.config(text=f"Время удержания клавиш: {elapsed_time:.2f} секунд")
    else:
        result_label.config(text="Неверный пароль!")

        password_entry.delete(0, tk.END)

def generate_button_clicked():
    global generated_password, start_time

    length = int(length_entry.get())
    use_english = english_var.get()
    use_russian = russian_var.get()
    use_special_chars = special_chars_var.get()

    generated_password = generate_password(length, use_english, use_russian, use_special_chars)

    password_label.config(text=generated_password)

    password_entry.delete(0, tk.END)
    password_entry.focus()

start_time = time.time()

root = tk.Tk()
root.title("Генератор паролей")

length_label = tk.Label(root, text="Длина пароля:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

english_var = tk.BooleanVar()
english_checkbutton = tk.Checkbutton(root, text="Использовать английский алфавит", variable=english_var)
english_checkbutton.pack()

russian_var = tk.BooleanVar()
russian_checkbutton = tk.Checkbutton(root, text="Использовать русский алфавит", variable=russian_var)
russian_checkbutton.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbutton = tk.Checkbutton(root, text="Использовать специальные символы", variable=special_chars_var)
special_chars_checkbutton.pack()

generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_button_clicked)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack()
password_entry.bind('<Return>', check_password)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()