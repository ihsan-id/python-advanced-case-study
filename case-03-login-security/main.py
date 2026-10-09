
# Studi Kasus 3: Sistem Keamanan Akun & Audit Log Login

import re
from datetime import datetime
from functools import wraps


# 1. Class User dengan validasi dan property
class User:
    def __init__(self, username, password):
        self._username = None
        self._password = None

        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        pola_username = r"[A-Za-z0-9]{5,}"

        if not isinstance(value, str) or not re.fullmatch(
            pola_username, value
        ):
            raise ValueError(
                "Username harus minimal 5 karakter "
                "dan hanya boleh berisi huruf dan angka."
            )

        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        pola_password = r"(?=.*[0-9]).{8,}"

        if not isinstance(value, str) or not re.fullmatch(
            pola_password, value
        ):
            raise ValueError(
                "Password harus minimal 8 karakter "
                "dan mengandung setidaknya satu angka."
            )

        self._password = value


# 2. Decorator untuk mencatat audit log login
def audit_log(fungsi_login):
    @wraps(fungsi_login)
    def wrapper(username, password, akun_terdaftar):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            berhasil = fungsi_login(
                username, password, akun_terdaftar
            )

            if berhasil:
                status = "BERHASIL"
                alasan = ""
            else:
                status = "DITOLAK"
                alasan = "Username atau password tidak cocok."

        except ValueError as error:
            berhasil = False
            status = "DITOLAK"
            alasan = str(error)

        # Username dicatat, tetapi password tidak pernah dicetak.
        print(f"\nWaktu   : {waktu}")
        print(f"Username: {username}")
        print(f"Status  : {status}")

        if alasan:
            print(f"Alasan  : {alasan}")

        return berhasil

    return wrapper


# 3. Fungsi login yang dibungkus decorator
@audit_log
def login(username, password, akun_terdaftar):
    # Membuat objek User sekaligus memvalidasi formatnya.
    pengguna = User(username, password)

    # Memeriksa kecocokan dengan akun yang terdaftar.
    return (
        pengguna.username == akun_terdaftar.username
        and pengguna.password == akun_terdaftar.password
    )


# 4. Pengujian program
def main():
    print("=" * 60)
    print("       SISTEM KEAMANAN AKUN DAN AUDIT LOG")
    print("=" * 60)

    # Akun resmi untuk simulasi pengujian.
    akun_resmi = User("admin01", "aman12345")

    print("\n[UJI 1] Username tidak valid")
    login("ad!", "aman12345", akun_resmi)

    print("\n[UJI 2] Password terlalu pendek")
    login("admin01", "abc12", akun_resmi)

    print("\n[UJI 3] Password tidak mengandung angka")
    login("admin01", "passwordaman", akun_resmi)

    print("\n[UJI 4] Login berhasil")
    login("admin01", "aman12345", akun_resmi)

    print("\n" + "=" * 60)
    print("Pengujian selesai.")
    print("=" * 60)


if __name__ == "__main__":
    main()
