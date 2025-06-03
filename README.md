
# ZIP Tool GUI - L4F (ZipZrackL4F.py)

Aplikasi GUI Python untuk melakukan bruteforce pada file ZIP berpassword dan membuat file ZIP dengan password. Dirancang untuk penggunaan yang mudah, termasuk oleh pemula.

---

## 🎯 Fitur

- **Bruteforce ZIP:** Coba password satu per satu dari wordlist untuk membuka file ZIP terenkripsi.
- **Buat ZIP Berpassword:** Kompres beberapa file ke dalam ZIP dengan password.
- **GUI Interaktif:** Antarmuka pengguna menggunakan Tkinter.
- **ASCII Banner & Animasi:** Banner keren dengan `pyfiglet`, animasi footer.
- **Support Ekstrak Otomatis:** Setelah berhasil bruteforce, file langsung diekstrak.

---

## 🛠️ Instalasi & Dependensi

### 1. **Install Python**
Pastikan Python 3.x sudah terpasang. Bisa unduh dari: https://www.python.org/downloads/  
Centang “Add Python to PATH” saat instalasi.

### 2. **Install Library Python**

#### 📦 Cara Otomatis (disarankan):
Jalankan perintah berikut (gunakan file `requirements.txt`):

```bash
pip install -r requirements.txt
```

#### 📦 Cara Manual:
Jalankan perintah ini satu per satu:

```bash
pip install pyzipper
pip install pyfiglet
```

### 3. **Install Tkinter (jika diperlukan)**

#### Windows/macOS:
Sudah terinstall secara default.

#### Linux (Ubuntu/Debian):
```bash
sudo apt-get install python3-tk
```

---

## 🧾 Daftar Library Python yang Digunakan

| Library         | Fungsi                                                                 |
|------------------|------------------------------------------------------------------------|
| `tkinter`        | Membuat antarmuka grafis (GUI)                                         |
| `pyzipper`       | Membaca dan membuat file ZIP dengan enkripsi AES                      |
| `pyfiglet`       | Membuat teks banner ASCII keren di GUI                                |
| `threading`      | Menjalankan proses di background agar GUI tidak hang                  |
| `os`             | Mengakses path file dan folder                                         |
| `filedialog`     | Memilih file dan folder secara grafis                                 |
| `messagebox`     | Menampilkan notifikasi dan error dialog                               |
| `scrolledtext`   | Menampilkan output log panjang di GUI                                 |
| `ttk`            | Komponen tambahan GUI dari tkinter                                    |

---

## 🚀 Cara Menjalankan

1. Simpan script Python sebagai `ZipZrackL4F.py`
2. Jalankan lewat terminal atau CMD:

```bash
python ZipZrackL4F.py
```

---

## 📁 Struktur Folder (Contoh)

```
ZIP-Tool-GUI-L4F/
├── ZipZrackL4F.py
├── wordlist.txt       # Opsional: wordlist untuk bruteforce
├── requirements.txt   # Daftar dependensi Python
└── README.md
```

---

## ⚠️ Catatan Penting

- Gunakan hanya untuk keperluan legal dan pembelajaran.
- Jangan gunakan untuk membobol file ZIP tanpa izin pemiliknya.
- Password akan terlihat saat pembuatan ZIP — agar edukatif.

---

## 👤 Author

Created by **Ramdhanisheva**  
Email: ramdhanisheva@gmail.com

Lisensi: MIT
