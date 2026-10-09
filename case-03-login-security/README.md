# Studi Kasus 3 — Sistem Keamanan Akun dan Audit Log Login

## Deskripsi
Program ini dibuat untuk melakukan validasi username dan password serta mencatat setiap percobaan login. Sistem mencatat waktu, username, status login, dan alasan penolakan apabila terjadi kegagalan.

## Konsep Python yang Digunakan

1. **RegEx:** menggunakan modul `re` untuk memvalidasi format username dan password.
2. **Class dan OOP:** menggunakan class `User` untuk merepresentasikan pengguna.
3. **Property Decorator:** menggunakan `@property` dan setter untuk mengelola serta memvalidasi atribut username dan password.
4. **Decorator dan Closure:** menggunakan `audit_log()` untuk membungkus fungsi login dan mencatat setiap percobaan.
5. **Exception Handling:** menggunakan `try-except` untuk menangani kesalahan validasi menggunakan `ValueError`.

## Aturan Validasi

- Username minimal 5 karakter dan hanya boleh terdiri dari huruf serta angka.
- Password minimal 8 karakter dan wajib mengandung setidaknya satu angka.

## Skenario Pengujian

1. Login ditolak karena format username tidak valid.
2. Login ditolak karena password terlalu pendek.
3. Login ditolak karena password tidak mengandung angka.
4. Login berhasil ketika username dan password valid serta cocok dengan akun terdaftar.

## Cara Menjalankan

Pastikan Python sudah terpasang, kemudian jalankan perintah berikut dari folder kasus:

```bash
python main.py
```

## Hasil Pengujian
Program menampilkan audit log setiap kali fungsi login dipanggil, termasuk timestamp, username, status, dan alasan penolakan jika terjadi kegagalan. Password tidak dicetak dalam log.

## Bukti Eksekusi
Screenshot output terminal disimpan dengan nama `output.png` di folder ini.