import tkinter as tk

root = tk.Tk()
root.title("Приветствие")

label = tk.Label(root, text="Привет!", font=("Arial", 24))
label.pack(padx=50, pady=50)

root.mainloop()
