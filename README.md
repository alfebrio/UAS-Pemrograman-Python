# UAS-Pemrograman-Python

## Deskripsi
Repositori ini merupakan implementasi tugas Ujian Akhir Semester (UAS) untuk mata kuliah Pemrograman Python. Project ini menggunakan arsitektur client-server untuk mengelola data melalui database MySQL.

## Struktur
- `server.py` – Backend yang menangani operasi CRUD ke database.
- `db_phone.sql` – Skrip SQL sebagai isi tabel database.
- `client.py` – Aplikasi yang berkomunikasi dengan server.

## Fitur
- Menambahkan data baru ke database melalui client.
- Menampilkan dan memperbarui data yang tersimpan.
- Menghapus data yang tidak dibutuhkan.
- Komunikasi client–server menggunakan protokol HTTP (dengan Flask).

## Komponen
| Bagian        | Library               |
|---------------|-----------------------|
| Backend       | Python + Flask        |
| Database      | MySQL                 |
| Komunikasi    | HTTP REST API         |

## Setup
```bash
mysql -u [user] -p > db_phone.sql

