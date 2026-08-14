import tkinter as tk
import datetime as dt
root = tk.Tk()
root.geometry("300x300")
label = tk.Label(root, font=("Arial", 30))
label.pack(pady=50)
def upd_time():
    time = dt.datetime.now()
    label.config(text=time.strftime("%H:%M:%S"))
    root.after(200,upd_time )
upd_time()
root.mainloop()