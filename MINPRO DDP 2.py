import os
import time
import prettytable
import pwinput
import sys

# Inisialisasi data user dan koleksi tenun
data_user = {
    "ADMIN RAIHANUM": {"password": "1234", "role": "admin"},
    "MUTHI": {"password": "ABCD", "role": "user"},
}

koleksi_tenun = {
    ("TS-001", "Belang Hatta", "merah-hitam", "baik (dipamerkan)", 1953),
    ("TS-002", "Pucuk Rebung", "hijau-emas", "Baik (arsip utama)", 2018),
    ("TS-003", "Sabuk Kota Mahakam", "biru-perak", "Butuh restorasi", 2010),
    ("TS-004", "Belang Hatta", "merah-cokelat", "Butuh restorasi", 1995),
    ("TS-005", "Akulturasi Dayak", "Hitam-krem", "Dipamerkan", 2022),
    ("TS-006", "Pucuk Rebung", "biru-krem", "baik (arsip utama)", 2001),
}

# Bersihkan layar
def bersih_layar():
    os.system("cls" if os.name == "nt" else "clear")
    

# Opsi 1 halaman admin: masukkan data baru
def tambah_data():
    bersih_layar()
    print("\n")
    print("\n === MASUKKAN DATA BARU ===")
    kode = input("input kode kain: ").strip().upper()
    if any(kain[0].upper() == kode for kain in koleksi_tenun):
        print("Kode sudah terdaftar")
        return

    motif = input("Input motif: ").strip()
    warna = input("Input warna: ").strip()
    kondisi = input("Input kondisi: ").strip()
    while True:
        tahun_input = input("Input tahun pembuatan: ").strip()
        if tahun_input.isdigit():
            tahun = int(tahun_input)
            koleksi_tenun.add((kode, motif, warna, kondisi, tahun))
            print("Data berhasil ditambah")
            break
        print("Harus angka")


# Opsi 2 halaman admin: tampilkan semua data
def tampilkan_data():
    bersih_layar()
    print("\n")
    print("\n === TAMPILKAN SEMUA DATA ===")
    if not koleksi_tenun:
        print("Data kosong")
        return
    table = prettytable.PrettyTable()
    table.field_names = ["Kode", "Motif", "Warna", "Kondisi", "Tahun"]
    for kode, motif, warna, kondisi, tahun in sorted(koleksi_tenun):
        table.add_row([kode, motif, warna, kondisi, tahun])
    print(table)


# Opsi 3 halaman admin: ubah data
def ubah_data():
    bersih_layar()
    print("\n")
    print("\n === MENGUBAH DATA ===")
    if not koleksi_tenun:
        print("Data kosong")
        return
    kode_target = input("Masukkan kode kain yang ingin diubah: ").strip().upper()
    kain_yang_ditemukan = next(
        (kain for kain in koleksi_tenun if kain[0].upper() == kode_target), None
    )
    if kain_yang_ditemukan is None:
        print("Kode tidak ditemukan")
        return
    motif_baru = input("Masukkan motif baru: ").strip()
    warna_baru = input("Masukkan warna baru: ").strip()
    kondisi_baru = input("Masukkan kondisi baru: ").strip()

    while True:
        tahun_input = input("Masukkan tahun baru: ").strip()
        if tahun_input.isdigit():
            tahun_baru = int(tahun_input)
            koleksi_tenun.remove(kain_yang_ditemukan)
            koleksi_tenun.add(
                (kode_target, motif_baru, warna_baru, kondisi_baru, tahun_baru)
            )
            print("Data berhasil diubah")
            break
        print("Tahun harus angka")


# Opsi 4 halaman admin: hapus data
def hapus_data():
    bersih_layar()
    print("\n")
    print("\n === MENGHAPUS DATA ===")
    if not koleksi_tenun:
        print("Data kosong")
        return

    kode_target = input("Masukkan kode kain yang ingin dihapus: ").strip().upper()
    kain_yang_ditemukan = next(
        (kain for kain in koleksi_tenun if kain[0].upper() == kode_target), None
    )

    if kain_yang_ditemukan is None:
        print("Kode tidak ditemukan")
        return
    koleksi_tenun.remove(kain_yang_ditemukan)
    print("Data berhasil dihapus")


# Opsi 5 halaman admin: keluar
def keluar():
    bersih_layar()
    print("\n")
    print("\n === KELUAR ===")
    print("Terima Kasih")
    sys.exit()


# Opsi 6 halaman admin: logout
def logout():
    print("\n")
    print("\n === LOGOUT ===")
    print("Logout berhasil")
    return main()


# Halaman admin
def menu_admin():
    bersih_layar()
    while True:
        print("\n")
        print("\n========= HALAMAN ADMIN =========")
        print("1. Masukkan Data Baru")
        print("2. Tampilkan Semua Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")
        print("6. Logout")
        pilihan = input("Pilih Menu (1-6): ").strip()
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            keluar()
        elif pilihan == "6":
            logout()
        else:
            print("Pilihan tidak valid")


# Halaman user
def menu_user():
    bersih_layar()
    print("\n")
    print("\n========= HALAMAN USER =========")
    while True:
        print("1. Tampilkan Koleksi Tenun")
        print("2. Logout")
        print("3. Keluar")

        pilihan = input("Pilih Menu (1-3): ").strip()
        if pilihan == "1":
            tampilkan_data()
            time.sleep(5)
            return menu_user()
        elif pilihan == "2":
            logout()
        elif pilihan == "3":
            keluar()
        else:
            print("Pilihan tidak valid")


# Halaman login
def main():
    bersih_layar()
    while True:
        print("\n" + "=" * 45)
        print("ARSIP KOLEKSI KAIN TENUN SAMARINDA")
        print("=" * 45)
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        pilihan = input("Pilih Menu (1-3): ").strip()

        # 1. LOGIN
        if pilihan == "1":
            bersih_layar()
            print("\n")
            print("============= LOGIN =============")
            username = input("Masukkan Username: ").strip().upper()
            password = pwinput.pwinput("Masukkan Password: ").strip().upper()

            if (
                username in data_user
                and data_user[username]["password"] == password
            ):
                role = data_user[username]["role"]
                if role == "admin":
                    menu_admin()
                elif role == "user":
                    menu_user()
            else:
                print("\nUsername atau password salah")
                time.sleep(3)
                return main()

        # 2. REGISTRASI
        elif pilihan == "2":
            bersih_layar()
            print("\n")
            print("============= REGISTRASI =============")
            username_baru = input("Masukkan username baru: ").strip().upper()
            password_baru = pwinput.pwinput("Masukkan password baru: ").strip()

            if username_baru in data_user:
                print("\nUsername sudah terdaftar")
            else:
                data_user[username_baru] = {
                    "password": password_baru,
                    "role": "user",
                }
                print("\nRegistrasi berhasil")
            time.sleep(3)

        # 3. KELUAR
        elif pilihan == "3":
            bersih_layar()
            print("\n")
            print("============= KELUAR =============")
            print("Terima kasih")
            sys.exit()

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
