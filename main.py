from components.buku_manager import *
from components.user_manager import *

from prettytable import PrettyTable


def cls(): os.system('clear' if os.name == 'posix' else 'cls')


def menu():
    load_data_pengunjung()
    load_data_buku()

    while True:
        print("\n===== SELAMAT DATANG DI PERPUSTAKAAN KAMI =====")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            cls()
            print('==== Silahkan Register ====')
            username = input("Username: ")
            while len(username) < 3:
                username = input(
                    "Username harus memiliki setidaknya 3 karakter. Masukkan lagi username: ")
            password = input("Password: ")
            while len(password) < 3:
                password = input(
                    "password harus memiliki setidaknya 3 karakter. Masukkan lagi password: ")
            sebagai = input('Sebagai? (mahasiswa/tenaga kependidikan/dosen): ')
            while sebagai.lower() != 'mahasiswa' and sebagai.lower() != 'tenaga kependidikan' and sebagai.lower() != 'dosen':
                sebagai = input(
                    'Sebagai? (mahasiswa/tenaga kependidikan/dosen): ')
            register_pengunjung(username, password, sebagai.lower())

        elif pilihan == '2':
            cls()
            print('==== Silahkan Login ====')
            username = input("Username: ")
            password = input("Password: ")
            if login_pengunjung(username, password):
                while True:
                    print("\n===== MENU PERPUSTAKAAN =====")
                    print("1. Tambah Buku")
                    print("2. Cari Buku")
                    print("3. Pinjam Buku")
                    print("4. Kembalikan Buku")
                    print("5. Tampilkan Buku per Kategori")
                    print("6. Simpan Perubahan Dan Logout")

                    pilihan_pengunjung = input("Pilih menu (1-6): ")

                    if pilihan_pengunjung == '1':
                        if username == 'admin' and password == '123':
                            cls()
                            print('==== Menambah Buku ====')
                            judul = input("Judul Buku: ")
                            while len(judul) < 1:
                                judul = input(
                                    'Judul tidak boleh kosong! Masukkan lagi Judul: ')
                            pengarang = input("Pengarang Buku: ")
                            while len(pengarang) < 1:
                                pengarang = input(
                                    'Pengarang tidak boleh kosong! Masukkan lagi Pengarang: ')
                            kategori = input("Kategori Buku: ")
                            while len(kategori) < 1:
                                kategori = input(
                                    'Kategori tidak boleh kosong! Masukkan lagi Kategori: ')
                            tambah_buku(judul.lower(),
                                        pengarang.lower(), kategori.lower())

                        else:
                            cls()
                            print('Maaf anda bukan admin')

                    elif pilihan_pengunjung == '2':
                        kriteria = input(
                            "Cari berdasarkan? (judul/pengarang): ")
                        while kriteria.lower() != 'judul' and kriteria.lower() != 'pengarang':
                            kriteria = input(
                                "Cari berdasarkan? (judul/pengarang): ")

                        cls()
                        print("==== Cari Buku ====")

                        if kriteria.lower() == 'judul':
                            nilai = input("Masukkan judul: ")
                        elif kriteria.lower() == 'pengarang':
                            nilai = input("Masukkan pengarang: ")

                        hasil_pencarian = cari_buku(
                            kriteria.lower(), nilai.lower())
                        if hasil_pencarian:
                            cls()
                            tabel = PrettyTable(
                                ['Judul', 'Pengarang', 'Kategori', 'Status'])
                            print("Hasil Pencarian:")
                            for buku_item in hasil_pencarian:
                                # print(f"Judul: {buku_item['judul']}, Pengarang: {buku_item['pengarang']}, Kategori: {buku_item['kategori']}, Status: {buku_item['status']}")
                                tabel.add_row(
                                    [buku_item['judul'], buku_item['pengarang'], buku_item['kategori'], buku_item['status']])
                            print(tabel)
                        else:
                            cls()
                            print("Buku tidak ditemukan.")

                    elif pilihan_pengunjung == '3':
                        cls()
                        print("==== Pinjam Buku ====")
                        judul_pinjam = input("Judul Buku yang akan dipinjam: ")
                        pinjam_buku(username, judul_pinjam.lower())

                    elif pilihan_pengunjung == '4':
                        cls()
                        print('==== Kembalikan Buku ====')
                        judul_kembali = input(
                            "Judul Buku yang akan dikembalikan: ")
                        kembalikan_buku(username, judul_kembali.lower())

                    elif pilihan_pengunjung == '5':
                        cls()
                        print('==== Menampilkan Buku Berdasarkan Kategori ====')
                        kategori_tampil = input(
                            "Pilih kategori (fiksi/nonfiksi): ")

                        while kategori_tampil.lower() != 'fiksi' and kategori_tampil.lower() != 'nonfiksi':
                            kategori_tampil = input(
                                "Pilih kategori (fiksi/nonfiksi): ")

                        buku_kategori = tampilkan_buku_kategori(
                            kategori_tampil.lower())
                        if buku_kategori:
                            cls()
                            tabel = PrettyTable(
                                ['Judul', 'Pengarang', 'Status'])
                            print(f"Buku pada kategori {kategori_tampil}:")
                            for buku_item in buku_kategori:
                                # print(f"Judul: {buku_item['judul']}, Pengarang: {buku_item['pengarang']}, Status: {buku_item['status']}")
                                tabel.add_row(
                                    [buku_item['judul'], buku_item['pengarang'], buku_item['status']])
                            print(tabel)
                        else:
                            cls()
                            print("Tidak ada buku pada kategori tersebut.")

                    elif pilihan_pengunjung == '6':
                        simpan_data_buku()
                        simpan_data_pengunjung()
                        cls()
                        print("Logout berhasil!")
                        break

                    else:
                        cls()
                        print("Pilihan tidak valid. Silakan pilih kembali.")

        elif pilihan == '3':
            simpan_data_buku()
            simpan_data_pengunjung()
            cls()
            print("Terima kasih! Sampai jumpa lagi.")
            break

        else:
            cls()
            print("Pilihan tidak valid. Silakan pilih kembali.")


menu()
