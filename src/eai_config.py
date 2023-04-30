# This is the config file for eai_main.py


# This is the config file for eai_main.py

from PIL import Image, ImageTk
import customtkinter as ctk

APP_TITLE = 'EAI - Easy Android Installer'
COLORMODE_IMAGE = ctk.CTkImage(dark_image=Image.open(r"assets/icon_cm.png"))
FILEDIALOG_IMAGE = ctk.CTkImage(dark_image=Image.open(r"assets/icon_file.png"))

ADB_PATH1 = r'adb install -r'
ADB_PATH2 = r'C:\Users\%userprofile%\AppData\Local\Android\Sdk\platform-tools\adb.exe install -r'
ADB_PATH3 = r'C:NVPACK\android-sdk-windows\platform-tools\adb.exe install -r'