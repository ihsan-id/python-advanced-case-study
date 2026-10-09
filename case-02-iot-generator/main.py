
# Studi Kasus 2: Streaming Data Sensor IoT Hemat Memori

def pembacaan_sensor():
    """
    Generator untuk menghasilkan data suhu sensor
    secara bertahap menggunakan yield.
    """
    for indeks in range(10):
        suhu = 15 + ((indeks * 7.3) % 23)
        yield round(suhu, 1)


def kategori_suhu(suhu):
    """Menentukan kategori berdasarkan nilai suhu."""
    if suhu < 20:
        return "Dingin"
    elif suhu <= 30:
        return "Normal"
    else:
        return "Panas"


def main():
    print("=" * 55)
    print("       STREAMING DATA SENSOR IoT")
    print("=" * 55)

    # Membuat objek generator tanpa menyimpan semua data.
    sensor = pembacaan_sensor()

    # Mengambil data satu per satu menggunakan next().
    for nomor in range(1, 11):
        suhu = next(sensor)
        status = kategori_suhu(suhu)

        print(
            f"Pembacaan ke-{nomor:02d} | "
            f"Suhu: {suhu:4.1f} °C | "
            f"Status: {status}"
        )

    print("-" * 55)
    print("Selesai: 10 pembacaan sensor telah diproses.")
    print("=" * 55)


if __name__ == "__main__":
    main()
