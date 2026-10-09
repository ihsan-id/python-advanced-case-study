# Studi Kasus 1 — Analisis Nilai Mahasiswa

## Deskripsi
Program ini dibuat untuk membantu proses analisis nilai mahasiswa. Program menghitung nilai akhir berdasarkan bobot tugas 30%, UTS 30%, dan UAS 40%, menampilkan mahasiswa berprestasi, mengurutkan ranking, dan menentukan mahasiswa terbaik.

## Konsep Python yang Digunakan
1. **List Comprehension:** digunakan untuk menghitung nilai akhir dan memfilter mahasiswa berprestasi.
2. **Lambda Function:** digunakan sebagai kunci pengurutan nilai akhir.
3. **Filtering:** digunakan untuk memilih mahasiswa dengan nilai akhir di atas 80.
4. **Sorting:** menggunakan fungsi `sorted()` untuk mengurutkan mahasiswa dari nilai tertinggi ke terendah.

## Rumus Nilai Akhir
Nilai Akhir = (Tugas × 30%) + (UTS × 30%) + (UAS × 40%).

## Cara Menjalankan
Pastikan Python sudah terpasang. Buka terminal di folder kasus, lalu jalankan:

```bash
python main.py
```

## Hasil Pengujian
Program diharapkan menampilkan daftar nilai mahasiswa beserta ranking, daftar mahasiswa berprestasi dengan nilai di atas 80, serta informasi mahasiswa dengan peringkat pertama.

## Bukti Eksekusi
Screenshot hasil eksekusi program disimpan dengan nama `output.png` di folder ini.