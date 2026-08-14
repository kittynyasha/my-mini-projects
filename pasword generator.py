import random as rd
import string
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Password Generator")

all_chars = string.ascii_letters + string.digits + string.punctuation

title_label = tk.Label(root, text="Password Generator")
title_label.pack(pady=20)

length_scale = tk.Scale(root, from_=8, to=32, orient="horizontal")
length_scale.pack(pady=10)

password_entry = tk.Entry(root, width=35, justify="center")
password_entry.insert(0, "Your password will appear here")
password_entry.pack(pady=10)

password = ""


def generate_password():
    global password
    password_length = length_scale.get()

    password = "".join(rd.choice(all_chars) for _ in range(password_length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


generate_btn = tk.Button(
    root, text="Generate Password", command=generate_password
)
generate_btn.pack(pady=20)

root.mainloop()