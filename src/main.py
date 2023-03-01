import tkinter as tk

window = tk.Tk()
window.title("Easy Android Packager")
window.resizable(width=False, height=False)

frame = tk.Frame(master=window)
desc = tk.Entry(master=frame, width=10)
desc.pack(padx=20, pady=20)

window.mainloop()