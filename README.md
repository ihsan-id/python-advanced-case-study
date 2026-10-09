# Python Advanced Case Study

## Identitas Mahasiswa

- **Nama:** M Afiful Ikhsan
- **NIM:** 2595114031
- **Program Studi:** Teknik Informatika
- **Mata Kuliah:** Pemrograman Berorientasi Objek

## Deskripsi Proyek

Repository ini dibuat untuk memenuhi tugas mandiri Python Advanced Topics. Proyek ini berisi tiga studi kasus yang menerapkan konsep lanjutan Python untuk menyelesaikan permasalahan dalam pengolahan data mahasiswa, pemrosesan data sensor, dan keamanan akun.

## Studi Kasus

### 1. Analisis Nilai Mahasiswa

Program ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan bobot tugas sebesar 30%, UTS sebesar 30%, dan UAS sebesar 40%. Program juga memfilter mahasiswa dengan nilai akhir di atas 80, mengurutkan ranking dari nilai tertinggi hingga terendah, serta menentukan mahasiswa terbaik.

**Konsep Python yang digunakan:**
- List Comprehension
- Lambda Function
- Filtering
- Sorting menggunakan `sorted()`

**Lokasi:** `case-01-analisis-nilai/`

### 2. Streaming Data Sensor IoT Hemat Memori

Program ini menyimulasikan pembacaan data suhu sensor secara bertahap. Setiap data suhu diproses dan dikelompokkan menjadi kategori dingin, normal, atau panas tanpa harus menyimpan seluruh hasil pembacaan ke dalam list besar.

**Konsep Python yang digunakan:**
- Iterator Pattern
- Generator Function
- Kata kunci `yield`
- Fungsi `next()`
- Efisiensi memori

**Lokasi:** `case-02-iot-generator/`

### 3. Sistem Keamanan Akun dan Audit Log Login

Program ini melakukan validasi username dan password menggunakan ekspresi reguler. Class `User` digunakan untuk mengelola atribut pengguna, sedangkan decorator digunakan untuk mencatat waktu percobaan login, username, status, dan alasan penolakan jika login gagal.

**Konsep Python yang digunakan:**
- Regular Expression (RegEx)
- Object-Oriented Programming (OOP)
- Property Decorator (`@property`)
- Decorator dan Closure
- Exception Handling
- Audit Log

**Lokasi:** `case-03-login-security/`

## Struktur Repository

```text
python-advanced-case-study/
├── README.md
├── case-01-analisis-nilai/
│   ├── main.py
│   ├── README.md
│   └── output.png
├── case-02-iot-generator/
│   ├── main.py
│   ├── README.md
│   └── output.png
└── case-03-login-security/
    ├── main.py
    ├── README.md
    └── output.png
```

## Cara Menjalankan Program

Pastikan Python 3 sudah terpasang pada komputer. Buka terminal di folder utama repository, kemudian jalankan setiap program menggunakan perintah berikut.

**Studi Kasus 1:**
```bash
python case-01-analisis-nilai/main.py
```

**Studi Kasus 2:**
```bash
python case-02-iot-generator/main.py
```

**Studi Kasus 3:**
```bash
python case-03-login-security/main.py
```

Semua program menggunakan modul bawaan Python sehingga tidak memerlukan instalasi library tambahan.

## Progres Pengerjaan

- [x] Membuat struktur folder repository.
- [x] Menyusun program analisis nilai mahasiswa.
- [x] Menyusun program generator data sensor IoT.
- [x] Menyusun program keamanan akun dan audit log.
- [ ] Menjalankan dan memeriksa seluruh program.
- [ ] Mengambil screenshot hasil eksekusi untuk setiap studi kasus.
- [ ] Melengkapi bukti eksekusi `output.png`.
- [ ] Mengunggah repository ke GitHub.

## Kesimpulan

Melalui proyek ini, konsep lanjutan Python diterapkan dalam tiga studi kasus yang berbeda. Setiap program dirancang agar mudah dibaca, dijalankan, dan dipahami. Repository ini juga disusun dengan dokumentasi terpisah pada setiap folder kasus untuk memudahkan pemeliharaan dan pengembangan program.