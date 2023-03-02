import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Easy Android Packager")
        self.window.resizable(width=False, height=False)
        self.window.geometry("350x150")

        self.label = tk.Label(self.window, text="Tester", font=('Roboto', 18))
        self.label.pack(padx=20, pady=10)

        self.filePathFrame = tk.Frame(self.window)
        self.filePathFrame.columnconfigure(0, weight=1)
        self.filePathFrame.columnconfigure(1, weight=1)

        self.textFilePath = tk.Entry(self.filePathFrame, font=('Roboto', 14))
        self.textFilePath.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.button = tk.Button(self.filePathFrame, text="F", font=('Roboto', 16))
        self.button.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.filePathFrame.pack(fill='x', padx=10)

        self.window.mainloop()