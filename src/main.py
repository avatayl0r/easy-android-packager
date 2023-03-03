import subprocess as sp
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog as fg
from PIL import Image

currentMode = False
buildDir = ''
fgImage = ctk.CTkImage(dark_image=Image.open(r"assets\icon_file.png"))

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Easy Android Packager')
        self.geometry('300x100')
        self.resizable(width='false', height='false')

        ctk.set_appearance_mode('dark')

        self.colorModeButton = ctk.CTkButton(
            self,
            text = 'Color Mode',
            command = self.toggleColorMode
            )
        self.colorModeButton.pack()

        self.askDirButton = ctk.CTkButton(
            self,
            width=32,
            height=32,
            text='',
            image=fgImage,
            command=self.askDir
        )
        self.askDirButton.pack()

        self.buildButton = ctk.CTkButton(
            self,
            text = 'Build',
            command = self.build
            )
        self.buildButton.pack()

    def toggleColorMode(self):
        global currentMode
        if currentMode == True:
            self.colorModeButton.configure(ctk.set_appearance_mode('dark'))
            currentMode = False
        
        else:
            self.colorModeButton.configure(ctk.set_appearance_mode('light'))
            currentMode = True

    def askDir(self):
        global buildDir
        buildDir = fg.askdirectory()
        return

    def build(self):
        setBuildDir = sp.run(['powershell', 'cd', buildDir])
        buildProject = sp.run(
            ['powershell', 
            r'C:\NVPACK\android-sdk-windows\platform-tools\adb install -r testbuild.apk']
            )
        return

window = Main()
window.mainloop()