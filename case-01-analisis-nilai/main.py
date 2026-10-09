
# Studi Kasus 1: Analisis Nilai Mahasiswa

# Data awal mahasiswa
data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 95, "uts": 91, "uas": 94},
]


# 1. Menghitung nilai akhir setiap mahasiswa
# Bobot tugas 30%, UTS 30%, dan UAS 40%
mahasiswa_terhitung = [
    {
        **mhs,
        "nilai_akhir": round(
            (mhs["tugas"] * 0.30)
            + (mhs["uts"] * 0.30)
            + (mhs["uas"] * 0.40),
            2
        )
    }
    for mhs in data_mahasiswa
]


# 2. Memfilter mahasiswa dengan nilai akhir di atas 80
mahasiswa_berprestasi = [
    mhs for mhs in mahasiswa_terhitung
    if mhs["nilai_akhir"] > 80
]


# 3. Mengurutkan mahasiswa berdasarkan nilai tertinggi
ranking = sorted(
    mahasiswa_terhitung,
    key=lambda mhs: mhs["nilai_akhir"],
    reverse=True
)


# 4. Menampilkan hasil analisis
def tampilkan_hasil():
    print("=" * 65)
    print("             ANALISIS NILAI MAHASISWA")
    print("=" * 65)

    print("\nDAFTAR NILAI DAN RANKING")
    print("-" * 65)

    for peringkat, mhs in enumerate(ranking, start=1):
        print(
            f"{peringkat}. {mhs['nama']:<10} "
            f"| NIM: {mhs['nim']} "
            f"| Tugas: {mhs['tugas']} "
            f"| UTS: {mhs['uts']} "
            f"| UAS: {mhs['uas']} "
            f"| Nilai Akhir: {mhs['nilai_akhir']:.2f}"
        )

    print("\nMAHASISWA BERPRESTASI (Nilai Akhir > 80)")
    print("-" * 65)

    if mahasiswa_berprestasi:
        for mhs in mahasiswa_berprestasi:
            print(
                f"- {mhs['nama']} "
                f"(NIM: {mhs['nim']}) "
                f"| Nilai Akhir: {mhs['nilai_akhir']:.2f}"
            )
    else:
        print("Tidak ada mahasiswa dengan nilai di atas 80.")

    # Mahasiswa peringkat pertama
    mahasiswa_terbaik = ranking[0]

    print("\nMAHASISWA TERBAIK")
    print("-" * 65)
    print(f"Nama        : {mahasiswa_terbaik['nama']}")
    print(f"NIM         : {mahasiswa_terbaik['nim']}")
    print(f"Nilai Tugas : {mahasiswa_terbaik['tugas']}")
    print(f"Nilai UTS   : {mahasiswa_terbaik['uts']}")
    print(f"Nilai UAS   : {mahasiswa_terbaik['uas']}")
    print(f"Nilai Akhir : {mahasiswa_terbaik['nilai_akhir']:.2f}")

    print("=" * 65)


if __name__ == "__main__":
    tampilkan_hasil()
