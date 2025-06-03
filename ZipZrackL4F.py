import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import pyzipper
import threading
import pyfiglet

class AnimatedFooter(tk.Label):
    def __init__(self, master, text, font, **kwargs):
        super().__init__(master, text=text, font=font, **kwargs)
        self.colors = ["#6a0dad", "#7f3ff5", "#9b59b6", "#8e44ad"]
        self.index = 0
        self.animate()

    def animate(self):
        self.config(fg=self.colors[self.index])
        self.index = (self.index + 1) % len(self.colors)
        self.after(400, self.animate)

class ColorFadeLabel(tk.Label):
    def __init__(self, master, text, font, **kwargs):
        super().__init__(master, text=text, font=font, **kwargs)
        self.colors = ["#6a0dad", "#7f3ff5", "#9b59b6", "#8e44ad"]
        self.index = 0
        self.animate()

    def animate(self):
        self.config(fg=self.colors[self.index])
        self.index = (self.index + 1) % len(self.colors)
        self.after(300, self.animate)

class ZipToolGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ZIP Tool GUI - L4F")
        self.geometry("700x650")
        self.dark_mode = False
        self.style = ttk.Style(self)
        self.set_theme()

        banner_text = pyfiglet.figlet_format("L4F", font="big")  # font "big" lebih tebal dari slant
        lbl_banner = ColorFadeLabel(self, text=banner_text, font=("Courier", 20, "bold"), justify="left")
        lbl_banner.pack(pady=(10, 0))

        footer = AnimatedFooter(self, text="Created by Ramdhanisheva", font=("Arial", 10, "bold"))
        footer.pack(side="bottom", pady=5)

        self.tab_control = ttk.Notebook(self)

        self.tab_bruteforce = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_bruteforce, text='Bruteforce ZIP')

        self.tab_createzip = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_createzip, text='Buat ZIP Password')

        self.tab_control.pack(expand=1, fill='both')

        self.create_bruteforce_tab()
        self.create_createzip_tab()

    def set_theme(self):
        if self.dark_mode:
            self.style.theme_use('clam')
            self.configure(bg="#2e2e2e")
            self.style.configure('.', background="#2e2e2e", foreground="white")
            self.style.configure('TButton', background="#6a0dad", foreground="white")
            self.style.map('TButton',
                           background=[('active', '#7f3ff5')],
                           foreground=[('active', 'white')])
        else:
            self.style.theme_use('default')
            default_bg = self.cget('bg')
            self.configure(bg=default_bg)
            self.style.configure('.', background=default_bg, foreground="black")

    # ... kode tab dan fungsi lainnya tetap sama ...

if __name__ == "__main__":
    app = ZipToolGUI()
    app.mainloop()
