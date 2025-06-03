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
        self.colors = ["gray", "black", "gray"]
        self.index = 0
        self.animate()

    def animate(self):
        self.config(fg=self.colors[self.index])
        self.index = (self.index + 1) % len(self.colors)
        self.after(500, self.animate)

class ZipToolGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ZIP Tool GUI - L4F")
        self.geometry("700x650")
        self.dark_mode = False
        self.style = ttk.Style(self)
        self.set_theme()

        banner_text = pyfiglet.figlet_format("L4F", font="slant")
        lbl_banner = tk.Label(self, text=banner_text, font=("Courier", 16), fg="#6a0dad", justify="left")
        lbl_banner.pack(pady=(10, 0))

        footer = AnimatedFooter(self, text="Created by Ramdhanisheva", font=("Arial", 10))
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

    def create_bruteforce_tab(self):
        tk.Label(self.tab_bruteforce, text="File ZIP:").pack(anchor='w', padx=10, pady=(10,0))
        frame_zip = tk.Frame(self.tab_bruteforce)
        self.entry_zip_bruteforce = tk.Entry(frame_zip, width=50)
        self.entry_zip_bruteforce.pack(side=tk.LEFT, padx=(0,5))
        btn_zip = tk.Button(frame_zip, text="Pilih", command=self.pilih_zip)
        btn_zip.pack(side=tk.LEFT)
        frame_zip.pack(anchor='w', padx=10)

        tk.Label(self.tab_bruteforce, text="File Wordlist:").pack(anchor='w', padx=10, pady=(10,0))
        frame_wordlist = tk.Frame(self.tab_bruteforce)
        self.entry_wordlist = tk.Entry(frame_wordlist, width=50)
        self.entry_wordlist.pack(side=tk.LEFT, padx=(0,5))
        btn_wordlist = tk.Button(frame_wordlist, text="Pilih", command=self.pilih_wordlist)
        btn_wordlist.pack(side=tk.LEFT)
        frame_wordlist.pack(anchor='w', padx=10)

        tk.Label(self.tab_bruteforce, text="Folder Ekstrak (optional):").pack(anchor='w', padx=10, pady=(10,0))
        frame_output = tk.Frame(self.tab_bruteforce)
        self.entry_output = tk.Entry(frame_output, width=50)
        self.entry_output.pack(side=tk.LEFT, padx=(0,5))
        btn_output = tk.Button(frame_output, text="Pilih", command=self.pilih_output)
        btn_output.pack(side=tk.LEFT)
        frame_output.pack(anchor='w', padx=10)

        self.btn_start = tk.Button(self.tab_bruteforce, text="Mulai Bruteforce", command=self.mulai_bruteforce,
                                   bg="#6a0dad", fg="white", font=("Arial", 12, "bold"))
        self.btn_start.pack(pady=15)

        btn_clear = tk.Button(self.tab_bruteforce, text="Clear Output", command=lambda: self.txt_output.delete(1.0, tk.END))
        btn_clear.pack()

        self.txt_output = scrolledtext.ScrolledText(self.tab_bruteforce, width=80, height=15)
        self.txt_output.pack(padx=10, pady=10)

    def pilih_zip(self):
        file = filedialog.askopenfilename(title="Pilih file ZIP", filetypes=[("ZIP files", "*.zip")])
        if file:
            self.entry_zip_bruteforce.delete(0, tk.END)
            self.entry_zip_bruteforce.insert(0, file)

    def pilih_wordlist(self):
        file = filedialog.askopenfilename(title="Pilih file Wordlist", filetypes=[("Text files", "*.txt")])
        if file:
            self.entry_wordlist.delete(0, tk.END)
            self.entry_wordlist.insert(0, file)

    def pilih_output(self):
        folder = filedialog.askdirectory(title="Pilih folder untuk ekstrak")
        if folder:
            self.entry_output.delete(0, tk.END)
            self.entry_output.insert(0, folder)

    def mulai_bruteforce(self):
        zip_file = self.entry_zip_bruteforce.get().strip()
        wordlist_file = self.entry_wordlist.get().strip()
        output_dir = self.entry_output.get().strip()
        if not zip_file or not os.path.isfile(zip_file):
            messagebox.showerror("Error", "File ZIP tidak valid atau tidak ditemukan!")
            return
        if not wordlist_file or not os.path.isfile(wordlist_file):
            messagebox.showerror("Error", "File wordlist tidak valid atau tidak ditemukan!")
            return
        if not output_dir:
            output_dir = "."

        self.btn_start.config(state=tk.DISABLED)
        self.txt_output.delete(1.0, tk.END)

        threading.Thread(target=self.crack_zip, args=(zip_file, wordlist_file, output_dir), daemon=True).start()

    def crack_zip(self, zip_file, wordlist_file, output_dir):
        try:
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = f.read().splitlines()
        except Exception as e:
            self.tampilkan_output(f"Gagal membaca wordlist: {e}\n")
            self.after(0, lambda: self.btn_start.config(state=tk.NORMAL))
            return

        self.tampilkan_output(f"Mencoba membuka {zip_file} dengan {len(passwords)} password...\n")

        try:
            with pyzipper.AESZipFile(zip_file) as zf:
                self.tampilkan_output("Isi file ZIP:\n")
                for info in zf.infolist():
                    self.tampilkan_output(f" - {info.filename}\n")

                for i, pw in enumerate(passwords, start=1):
                    try:
                        zf.pwd = pw.encode('utf-8')
                        zf.extractall(path=output_dir)
                        self.tampilkan_output(f"\n[+] Password ditemukan: {pw}\n")
                        self.tampilkan_output(f"[+] File diekstrak ke: {os.path.abspath(output_dir)}\n")

                        with open(os.path.join(output_dir, "password_tertemukan.txt"), "w", encoding="utf-8") as f:
                            f.write(pw)

                        self.after(0, lambda: self.btn_start.config(state=tk.NORMAL))
                        return
                    except RuntimeError:
                        if i % 100 == 0:
                            self.tampilkan_output(f"[-] Mencoba password ke-{i}: {pw}\n")
                    except pyzipper.zipfile.BadZipFile:
                        if i % 100 == 0:
                            self.tampilkan_output(f"[-] Mencoba password ke-{i}: {pw}\n")
                    except Exception as e:
                        self.tampilkan_output(f"[-] Error saat mencoba password '{pw}': {e}\n")
                        self.after(0, lambda: self.btn_start.config(state=tk.NORMAL))
                        return
        except Exception as e:
            self.tampilkan_output(f"[-] Gagal membuka file ZIP: {e}\n")

        self.tampilkan_output("\n[-] Password tidak ditemukan dalam wordlist.\n")
        self.after(0, lambda: self.btn_start.config(state=tk.NORMAL))

    def tampilkan_output(self, text):
        def append_text():
            self.txt_output.insert(tk.END, text)
            self.txt_output.see(tk.END)
        self.after(0, append_text)

    def create_createzip_tab(self):
        tk.Label(self.tab_createzip, text="Nama file ZIP (contoh: secret.zip):").pack(anchor='w', padx=10, pady=(10,0))
        self.entry_zip_buat = tk.Entry(self.tab_createzip, width=60)
        self.entry_zip_buat.pack(anchor='w', padx=10, pady=(0,10))

        tk.Label(self.tab_createzip, text="Password untuk ZIP:").pack(anchor='w', padx=10, pady=(0,0))
        self.entry_password = tk.Entry(self.tab_createzip, show='*', width=60)
        self.entry_password.pack(anchor='w', padx=10, pady=(0,10))

        tk.Label(self.tab_createzip, text="File yang akan dimasukkan ke ZIP:").pack(anchor='w', padx=10, pady=(0,0))

        frame_files = tk.Frame(self.tab_createzip)
        self.list_files = tk.Listbox(frame_files, width=60, height=10)
        self.list_files.pack(side=tk.LEFT, padx=(0,5))

        scroll_files = tk.Scrollbar(frame_files, command=self.list_files.yview)
        scroll_files.pack(side=tk.LEFT, fill=tk.Y)
        self.list_files.config(yscrollcommand=scroll_files.set)
        frame_files.pack(anchor='w', padx=10, pady=(0,10))

        frame_btn_files = tk.Frame(self.tab_createzip)
        btn_add_file = tk.Button(frame_btn_files, text="Tambah File", command=self.tambah_file_baru)
        btn_add_file.pack(side=tk.LEFT, padx=(0,5))
        btn_remove_file = tk.Button(frame_btn_files, text="Hapus File", command=self.hapus_file_baru)
        btn_remove_file.pack(side=tk.LEFT)
        frame_btn_files.pack(anchor='w', padx=10, pady=(0,10))

        btn_create_zip = tk.Button(self.tab_createzip, text="Buat ZIP Berpassword", command=self.buat_zip_baru,
                                   bg="#6a0dad", fg="white", font=("Arial", 12, "bold"))
        btn_create_zip.pack(pady=10)

    def tambah_file_baru(self):
        files = filedialog.askopenfilenames(title="Pilih file untuk dimasukkan ke ZIP")
        if files:
            for f in files:
                if f not in self.list_files.get(0, tk.END):
                    self.list_files.insert(tk.END, f)

    def hapus_file_baru(self):
        selected = self.list_files.curselection()
        for index in reversed(selected):
            self.list_files.delete(index)

    def buat_zip_baru(self):
        zip_name = self.entry_zip_buat.get().strip()
        password = self.entry_password.get()

        if not zip_name:
            messagebox.showerror("Error", "Masukkan nama file ZIP yang akan dibuat!")
            return
        if not password:
            messagebox.showerror("Error", "Masukkan password untuk ZIP!")
            return
        files = self.list_files.get(0, tk.END)
        if not files:
            messagebox.showerror("Error", "Tambahkan minimal satu file untuk dimasukkan ke ZIP!")
            return

        if not zip_name.endswith('.zip'):
            zip_name += '.zip'

        try:
            with pyzipper.AESZipFile(zip_name, 'w', compression=pyzipper.ZIP_DEFLATED,
                                     encryption=pyzipper.WZ_AES) as zf:
                zf.setpassword(password.encode('utf-8'))
                for file in files:
                    if os.path.isfile(file):
                        zf.write(file, arcname=os.path.basename(file))
                    else:
                        messagebox.showwarning("Warning", f"File tidak ditemukan dan dilewati: {file}")
            messagebox.showinfo("Sukses", f"File ZIP '{zip_name}' berhasil dibuat dengan password.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuat ZIP: {e}")

if __name__ == "__main__":
    app = ZipToolGUI()
    app.mainloop()
