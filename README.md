ZIP Tool GUI - L4F


 ZIP Tool GUI - L4F adalah aplikasi berbasis Python dengan antarmuka grafis (GUI) yang berfungsi
 untuk:- Melakukan bruteforce password pada file ZIP dengan menggunakan wordlist- Membuat file ZIP berpassword dengan mudah dan cepat
 Aplikasi ini memudahkan pengguna yang ingin mengelola file ZIP yang diproteksi password,
 khususnya bagi pemula.--
 
Fitur- Bruteforce Password ZIP: Mencoba password satu per satu dari file wordlist untuk membuka ZIP
 yang terkunci.- Buat ZIP Berpassword: Membuat file ZIP baru yang diproteksi dengan password, dengan
 menambahkan file-file yang diinginkan.- GUI Interaktif: Menggunakan Tkinter untuk antarmuka yang mudah dipahami.- Status Output: Menampilkan proses dan hasil pada jendela output.- Animasi footer dan banner untuk tampilan menarik.--
Prasyarat (Requirements)
 Agar aplikasi berjalan dengan baik, silakan install beberapa dependensi berikut:- Python 3.7+ (disarankan versi terbaru)- pyzipper: Untuk manipulasi file ZIP dengan enkripsi AES- pyfiglet: Untuk membuat banner ASCII art- tkinter: GUI toolkit bawaan Python (biasanya sudah terinstall secara default)
--
Cara Install
 1. Install Python
   Jika belum punya, unduh dan install Python 3.x dari https://www.python.org/downloads/
   Pastikan Python sudah terpasang dengan benar dan bisa diakses lewat command line.
 2. Install library yang dibutuhkan
   Buka terminal / command prompt lalu jalankan perintah berikut:
   pip install pyzipper pyfiglet
 3. Pastikan tkinter sudah terpasang
   - Pada Windows dan macOS, tkinter biasanya sudah termasuk saat instalasi Python.
   - Pada Linux (Ubuntu/Debian), jika belum terpasang, install dengan:
     sudo apt-get install python3-tk--
Cara Menjalankan Aplikasi
 1. Simpan file kode Python (ZipZrackL4F atau nama file yang kamu gunakan) di komputer kamu.
 2. Buka terminal / command prompt, arahkan ke folder tempat file tersebut disimpan.
 3. Jalankan aplikasi dengan perintah:
   python ZipZrackL4F 
 4. GUI akan muncul, kamu bisa:
   - Tab "Bruteforce ZIP": Pilih file ZIP, wordlist, dan folder output lalu klik "Mulai Bruteforce"
   - Tab "Buat ZIP Password": Masukkan nama file ZIP baru, password, dan tambahkan file yang
 ingin dikompres, lalu klik "Buat ZIP Berpassword"
--
Struktur File
 ZipZrackL4F       # Script utama aplikasi
 README.md             # Dokumentasi ini
 wordlist.txt          # (Opsional) contoh wordlist password untuk percobaan bruteforce--
Catatan Penting- File ZIP yang diuji menggunakan enkripsi AES (wzAES), yang didukung oleh pyzipper. ZIP standar
 (ZipCrypto) juga biasanya didukung.- Wordlist harus berupa file teks dengan satu password per baris.- Jangan gunakan aplikasi ini untuk membobol file ZIP tanpa izin pemiliknya. Gunakan hanya untuk
 pembelajaran dan kebutuhan legal.- Jika ingin fitur tambahan (misal toggle show/hide password), bisa dimodifikasi lebih lanjut.--
Lisensi
 MIT License (bebas digunakan dan dimodifikasi, tapi harap cantumkan kredit pembuat asli)--
Kontak / Author
 Created by Ramdhanisheva
 Email: ramdhanisheva@gmail.com
