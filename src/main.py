import subprocess as sp
import glob
import os

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog as fg
from tkinter import messagebox
from PIL import Image, ImageTk

currentMode = False
installDir = ' '
fgImage = ctk.CTkImage(dark_image=Image.open(r"src\assets\icon_file.png"))
cmImage = ctk.CTkImage(dark_image=Image.open(r"src\assets\icon_cm.png"))

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Easy Android Installer')
        self.geometry('512x128')
        self.resizable(width='false', height='false')
        self.eval('tk::PlaceWindow . center')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        ctk.set_appearance_mode('dark')

        textDir = ctk.StringVar()

        self.label1 = ctk.CTkLabel(
            self,
            text= 'APK Build Location:'
        )
        self.label1.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.colorModeButton = ctk.CTkButton(
            self,
            width=32,
            height=32,
            text='',
            image=cmImage,
            command = self.toggleColorMode
            )
        self.colorModeButton.grid(row=0, column=1, padx=20, pady=10, sticky='w')

        self.askDirText = ctk.CTkEntry(
            self,
            textvariable= textDir,
            width=420,
            placeholder_text= 'Enter Build Directory...'
        )
        self.askDirText.grid(row=1, column=0, columnspan=2, padx=20, pady=0, sticky='w')

        self.askDirButton = ctk.CTkButton(
            self,
            width=32,
            height=32,
            text='',
            image=fgImage,
            command=self.askDir
        )
        self.askDirButton.grid(row=1, column=1, padx=20, pady=0, sticky='w')

        self.installButton = ctk.CTkButton(
            self,
            text = 'Install',
            command = self.install
            )
        self.installButton.grid(row=2, column=0, padx=20, pady=10, sticky='w')

    def toggleColorMode(self):
        global currentMode
        if currentMode == True:
            self.colorModeButton.configure(ctk.set_appearance_mode('dark'))
            currentMode = False
        
        else:
            self.colorModeButton.configure(ctk.set_appearance_mode('light'))
            currentMode = True

    def askDir(self):
        global installDir
        installDir = fg.askdirectory()
        self.askDirText.delete(0, ctk.END)
        self.askDirText.insert(0, installDir)
        return

    def install(self):
        installDir = self.askDirText.get()

        assert os.path.exists(installDir), messagebox.showerror(
            r'ERROR: Path Not Found',r'Have you entered a valid filepath location? eg. D:\Projects\AndroidProject\Build '
            )

        apkGlob = glob.glob(installDir+'**/*.apk')
        apkFileOSPath = os.path.basename(str(apkGlob)).split('/')[-1]
        apkFile = apkFileOSPath.replace("'",' ').replace(']', ' ')
        print(installDir)

        try:
            installProject = sp.run(
            ['powershell', 
            r'adb install -r' 
            + ' ' 
            + installDir 
            + '/' 
            + apkFile]
            )
        except:
            try:
                installProject = sp.run(
                ['powershell', 
                r'C:\Users\%userprofile%\AppData\Local\Android\Sdk\platform-tools\adb.exe install -r' 
                + ' ' 
                + installDir 
                + '/' 
                + apkFile]
                )
            except:
                try:
                    installProject = sp.run(
                    ['powershell', 
                    r'C:NVPACK\android-sdk-windows\platform-tools\adb.exe install -r' 
                    + ' ' 
                    + installDir 
                    + '/' 
                    + apkFile]
                    )
                except:
                    messagebox.showerror('ERROR: ADB Not Found','Is Android Debug Bridge (ADB) installed?')
                    return

root = Main()
root.mainloop()