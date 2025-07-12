# Proyek Basis Data - Aplikasi Manajemen Hotel
Proyek ini adalah aplikasi **manajemen hotel** sederhana yang dibuat untuk menambah nilai pada mata kuliah Basis Data. Aplikasi ini memungkinkan pengguna untuk melakukan reservasi kamar hotel, mengelola data tamu, dan melihat riwayat transaksi.

## Fitur
* **Pesan Kamar**: Memungkinkan pengguna untuk memesan kamar dengan memasukkan data tamu, memilih tipe dan nomor kamar, serta menentukan tanggal *check-in* dan *check-out*.
* **Lihat Daftar Kamar**: Menampilkan daftar kamar yang tersedia beserta tipe, nomor, harga, dan status ketersediaannya.
* **Lihat Daftar Tamu**: Menampilkan daftar semua tamu yang pernah menginap.
* **Lihat Daftar Reservasi**: Menampilkan riwayat reservasi yang pernah dilakukan.
* **Lihat Riwayat Pembayaran**: Menampilkan riwayat transaksi pembayaran yang telah dilakukan.

---
## Teknologi yang Digunakan
* **Python**: Bahasa pemrograman utama yang digunakan untuk membangun aplikasi.
* **MySQL**: Sistem manajemen basis data untuk menyimpan semua data terkait hotel, seperti data tamu, kamar, reservasi, dan pembayaran.
* **Tkinter**: *Library* Python yang digunakan untuk membuat antarmuka pengguna grafis (GUI).
* **PrettyTable**: *Library* Python untuk membuat tabel ASCII yang rapi di konsol.
* **tkcalendar**: *Library* Python untuk menambahkan widget kalender di Tkinter.

---
## Cara Menjalankan Aplikasi
1.  ***Clone* repositori ini** ke komputer lokal Anda dengan menggunakan perintah berikut:
    ```bash
    git clone https://github.com/idrmdhni/BasisData-UAS.git
    ```
2.  **Pastikan MySQL sudah terpasang dan berjalan.**
3.  **Buat *database* baru** dengan nama `manajemen_hotel`.
4.  **Impor file `manajemen_hotel.sql`** ke dalam *database* yang baru saja dibuat untuk membuat tabel-tabel yang diperlukan.
5.  **Pasang semua *dependency*** yang dibutuhkan dengan menjalankan perintah berikut di terminal:
    ```bash
    pip install -r requirements.txt
    ```
6.  **Jalankan aplikasi** dengan memilih salah satu dari dua file berikut:
    * Untuk versi CLI:
        ```bash
        python apl_hotel.py
        ```
    * Untuk versi GUI:
        ```bash
        python apl_hotel_with_gui.py
        ```
