import tkinter as tk
root = tk.Tk()
root.title("Clicker Game")
root.geometry("300x400")
counter = 0 

label = tk.Label(root, text=f"Score: {counter}")

def on_click():
    global counter
    counter += 1
    label.config(text=f"Score: {counter}")

button = tk.Button(root, text="Add +1 to counter", command=on_click)

label.pack(pady=20)
button.pack(pady=10)

root.mainloop()