import json
import os

pengunjung = {}


def cls(): os.system('clear' if os.name == 'posix' else 'cls')


def register_pengunjung(username, password, sebagai):
    if username not in pengunjung:
        pengunjung[username] = {'password': password,
                                'sebagai': sebagai, 'pinjaman': []}
        cls()
        print("Registrasi berhasil!")
        simpan_data_pengunjung()

    else:
        cls()
        print("Username sudah terdaftar.")


def login_pengunjung(username, password):
    if username in pengunjung and pengunjung[username]['password'] == password:
        cls()
        print("Login berhasil!")
        return True
    else:
        cls()
        print("Login gagal. Periksa kembali username dan password.")
        return False


def simpan_data_pengunjung():
    with open('data_pengunjung.json', 'w') as file:
        json.dump(pengunjung, file)


def load_data_pengunjung():
    if os.path.exists('data_pengunjung.json'):
        with open('data_pengunjung.json', 'r') as file:
            pengunjung.update(json.load(file))
