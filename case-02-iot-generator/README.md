# Studi Kasus 2 — Streaming Data Sensor IoT Hemat Memori

## Deskripsi
Program ini merupakan simulasi sistem pembacaan sensor suhu pada stasiun pemantau cuaca. Data suhu dihasilkan dan diproses secara bertahap untuk mengurangi kebutuhan penyimpanan data di memori.

## Konsep Python yang Digunakan

1. **Generator Function:** menggunakan fungsi `pembacaan_sensor()` dengan kata kunci `yield` untuk menghasilkan data suhu secara bertahap.
2. **Iterator Pattern:** menggunakan objek generator dan fungsi `next()` untuk mengambil data satu per satu.
3. **Efisiensi Memori:** program tidak menyimpan seluruh hasil pembacaan dalam list besar.
4. **Conditional Statement:** menggunakan `if`, `elif`, dan `else` untuk menentukan kategori suhu.

## Aturan Kategori Suhu

- Dingin: suhu kurang dari 20°C.
- Normal: suhu antara 20°C sampai 30°C.
- Panas: suhu lebih dari 30°C.

## Cara Menjalankan

Pastikan Python sudah terpasang. Jalankan perintah berikut dari folder kasus:

```bash
python main.py
```

## Hasil Pengujian

Program menampilkan 10 pembacaan suhu sensor beserta kategori masing-masing. Pembacaan diproses secara bertahap menggunakan generator.

## Bukti Eksekusi

Screenshot output terminal disimpan dengan nama `output.png` di folder ini.