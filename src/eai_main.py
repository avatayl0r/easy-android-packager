import subprocess as subproc
import glob
import os

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

import eai_config as config

class eai_main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config.APP_TITLE)
        self.geometry('512x128')
        self.resizable(width='false', height='false')
        self.eval('tk::PlaceWindow . center')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ctk.set_appearance_mode('dark')

        self.text_dir = ctk.StringVar()
        self.install_dir = ''
        self.current_mode = False

        self.eai_ui_components()

    def eai_ui_components(self):
        self.label1 = ctk.CTkLabel(
            self,
            text= 'APK Build Location:'
        )
        self.label1.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.ask_dir_text = ctk.CTkEntry(
            self,
            textvariable= self.text_dir,
            width=420,
            placeholder_text= 'Enter Build Directory...'
        )
        self.ask_dir_text.grid(row=1, column=0, columnspan=2, padx=20, pady=0, sticky='w')

        self.ask_dir_button = ctk.CTkButton(
            self,
            width=32,
            height=32,
            text='',
            image=config.FILEDIALOG_IMAGE,
            command=self.ask_dir
        )
        self.ask_dir_button.grid(row=1, column=1, padx=20, pady=0, sticky='w')

        self.install_button = ctk.CTkButton(
            self,
            text = 'Install',
            command = self.install
            )
        self.install_button.grid(row=2, column=0, padx=20, pady=10, sticky='w')

    def ask_dir(self):
        self.install_dir = filedialog.askdirectory()
        self.ask_dir_text.delete(0, ctk.END)
        self.ask_dir_text.insert(0, self.install_dir)
        return

    def install(self):
        self.install_dir = self.ask_dir_text.get()

        assert os.path.exists(self.install_dir), messagebox.showerror(
            r'ERROR: Path Not Found',r'Have you entered a valid filepath location? eg. D:\Projects\AndroidProject\Build '
            )

        apk_glob = glob.glob(self.install_dir + '**/*.apk')
        apk_file_os_path = os.path.basename(str(apk_glob)).split('/')[-1]
        apk_file = apk_file_os_path.replace("'", ' ').replace(']', ' ')
        print(self.install_dir)

        try:
            install_project = subproc.run(
            ['powershell', 
            config.ADB_PATH1 
            + ' ' 
            + self.install_dir 
            + '/' 
            + apk_file]
            )
        except:
            try:
                install_project = subproc.run(
                ['powershell', 
                config.ADB_PATH2
                + ' ' 
                + self.install_dir 
                + '/' 
                + apk_file]
                )
            except:
                try:
                    install_project = subproc.run(
                    ['powershell', 
                    config.ADB_PATH3
                    + ' ' 
                    + self.install_dir 
                    + '/' 
                    + apk_file]
                    )
                except:
                    messagebox.showerror('ERROR: ADB Not Found','Is Android Debug Bridge (ADB) installed?')
                    return

if __name__ == '__main__':
    eai_main()
    tk.mainloop()
