# UAS-Pemrograman-Python

## Deskripsi
Repositori ini merupakan implementasi tugas Ujian Akhir Semester (UAS) untuk mata kuliah Pemrograman Python. Project ini menggunakan arsitektur client-server untuk mengelola data kontak melalui database SQLite/MySQL.

## Struktur
- `server.py` – Backend server yang menangani operasi CRUD ke database.
- `db_phone.sql` – Skrip SQL untuk membuat dan mengisi tabel database (misal: tabel chipset).
- `client.py` – Aplikasi client yang berkomunikasi dengan server untuk menampilkan atau memanipulasi data.

## Fitur Utama
- Menambahkan kontak baru ke database melalui client.
- Menampilkan dan memperbarui data kontak yang tersimpan.
- Menghapus kontak yang tidak dibutuhkan dengan aman.
- Komunikasi client–server menggunakan protokol HTTP (dengan Flask/Socket).

## Komponen
| Bagian        | Library               |
|---------------|-----------------------|
| Backend       | Python + Flask        |
| Database      | MySQL                 |
| Komunikasi    | HTTP REST API         |

## Setup
   ```bash
   mysql -u [user] -p < db_phone.sql

