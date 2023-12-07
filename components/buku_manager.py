import json
import os

from datetime import datetime, timedelta

from .user_manager import pengunjung

buku = []


def cls(): os.system('clear' if os.name == 'posix' else 'cls')


def tambah_buku(judul, pengarang, kategori):
    buku.append({'judul': judul, 'pengarang': pengarang,
                'kategori': kategori, 'status': 'tersedia'})
    cls()
    print('Buku berhasil di tambah')


def cari_buku(kriteria, nilai):
    hasil_pencarian = [b for b in buku if b[kriteria].lower() == nilai.lower()]
    return hasil_pencarian


def pinjam_buku(username, judul):

    tanggal_sekarang = datetime.now()
    tanggal_peminjaman = tanggal_sekarang.strftime("%d/%m/%Y")
    deadline = (
        tanggal_sekarang + timedelta(days=14)).strftime("%d/%m/%Y")

    for buku_item in buku:
        if buku_item['judul'] == judul and buku_item['status'] == 'tersedia':
            if 'sanksi_sampai' in pengunjung[username]:
                if pengunjung[username]['sanksi_sampai'] > tanggal_peminjaman:
                    cls()
                    print(f'Anda tidak diizinkan meminjam buku sampai {pengunjung[username]["sanksi_sampai"]}. ')
                else:
                    buku_item['status'] = 'dipinjam'
                    pengunjung[username]['pinjaman'].append(
                        {'judul': judul, 'pengarang': buku_item['pengarang'], 'tgl_peminjaman': tanggal_peminjaman, 'deadline': deadline})
                    del pengunjung[username]['sanksi_sampai']
                    cls()
                    print("Peminjaman berhasil!")                    
            else:
                buku_item['status'] = 'dipinjam'
                pengunjung[username]['pinjaman'].append(
                    {'judul': judul, 'pengarang': buku_item['pengarang'], 'tgl_peminjaman': tanggal_peminjaman, 'deadline': deadline})
                cls()
                print("Peminjaman berhasil!")
            return
    cls()
    print("Buku tidak tersedia atau sudah dipinjam.")


def kembalikan_buku(username, judul):

    tanggal_sekarang = datetime.now()
    tanggal_pengembalian = tanggal_sekarang.strftime("%d/%m/%Y")

    for buku_item in buku:
        if buku_item['judul'] == judul and buku_item['status'] == 'dipinjam':
            buku_item['status'] = 'tersedia'
            for pinjaman in pengunjung[username]['pinjaman']:
                if pinjaman['judul'] == judul:
                    
                    deadline = pinjaman['deadline']
                    terlambat = tanggal_pengembalian > deadline

                    a = datetime.strptime(deadline, "%d/%m/%Y")
                    b = datetime.strptime(tanggal_pengembalian, "%d/%m/%Y")
                    selisih_hari = (b - a).days

                    sanksi_sampai = (tanggal_sekarang + timedelta(days= selisih_hari)).strftime("%d/%m/%Y")
                    # c = datetime.strptime(sanksi_sampai, "%d/%m/%Y")
                    # selisih_sanksi = (c - b).days

                    # pengunjung[username]['pinjaman'].remove(pinjaman)
                    # cls()

                    if terlambat:
                        # denda = selisih_hari * 1000
                        pengunjung[username]['pinjaman'].remove(pinjaman)
                        pengunjung[username].update({'sanksi_sampai': sanksi_sampai})
                        cls()
                        print(f'Pengembalian berhasil dengan keterlambatan. Anda dilarang meminjam buku selama {selisih_hari} hari')
                        # print(sanksi_sampai)
                    else:
                        pengunjung[username]['pinjaman'].remove(pinjaman)
                        cls()
                        print("Pengembalian berhasil!")

                    return
    cls()
    print("Buku tidak dapat dikembalikan. Periksa kembali judul atau status buku.")


def tampilkan_buku_kategori(kategori):
    buku_kategori = [b for b in buku if b['kategori'].lower()
                     == kategori.lower()]
    return buku_kategori


def simpan_data_buku():
    with open('data_buku.json', 'w') as file:
        json.dump(buku, file)


def load_data_buku():
    if os.path.exists('data_buku.json'):
        with open('data_buku.json', 'r') as file:
            buku.extend(json.load(file))
