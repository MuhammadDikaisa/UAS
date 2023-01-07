from view.input_nilai import *
data = {}
def tambah_data():
    global data
    ulangi = 'y'
    while ulangi == 'y':
        nama = input_nama()
        nim = input_nim()
        nilai_tugas = input_ntugas()
        nilai_uts = input_nuts()
        nilai_uas = input_nuas()
        nilai_akhir = nakhir()
        data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir, nilai_akhir]
        ulangi = input("Tambahkan data? (y/t)")
        
        if ulangi == 't':
            print("/nData berhasil ditambahkan!")
            return data

def ubah_data():
    nama = input("Masukan nama untuk mengubah data : ")
    if nama in data.keys():
        print("\nMau mengubah apa?")
        sub_data = input("(Semua), (NIM), (Tugas), (UTS), (UAS) : ")
        if sub_data.lower() == "semua":
            print("==========================")
            print("Ubah data {}.".format(nama))
            print("==========================")
            data[nama][1] = input("Ubah NIM     :")
            data[nama][2] = int(input("Ubah Nilai Tugas     :"))
            data[nama][3] = int(input("Ubah Nilai UTS     :"))
            data[nama][4] = int(input("Ubah Nilai UAS     :"))
            data[nama][5] = data[nama][2] * 30/100 + data[nama][3] * 35/100 + data[nama][4] * 35/100
            print("\nBerhasil Ubah data!")
            
        elif sub_data.lower() == "nim":
            data[nama][1] = input("\nNim : ")
            print("\nData berhasil diubah!")
        elif sub_data.lower() == "tugas":
            data[nama][2] = int(input("\nNilai Tugas : "))
            data[nama][5] = data[nama][2] * 30/100 + data[nama][3] * 35/100 + data[nama][4] * 35/100
            print("\nData berhasil diubah!")
        elif sub_data.lower() == "uts":
            data[nama][1] = int(input("\nNilai uts : "))
            data[nama][5] = data[nama][2] * 30/100 + data[nama][3] * 35/100 + data[nama][4] * 35/100
            print("\nData berhasil diubah!")
        elif sub_data.lower() == "uas":
            data[nama][1] = input("\nNilai Uas : ")
            data[nama][5] = data[nama][2] * 30/100 + data[nama][3] * 35/100 + data[nama][4] * 35/100
            print("\nData berhasil diubah!")
        else:
            print("\nMenu tidak ditemukan")
            
    else:
        print("'{}' tidak ditemukan".format(nama))

def hapus_data():
    nama = input("Masukan nama untuk menghapus data : ")
    if nama in data.keys():
        del data[nama]
        print("\nData '{}' berhasil dihapus.".format(nama))
    else:
        print("'{}' tidak ditemukan.".format(nama))
        
def cari_data():
    print("Mencari data : ")
    print("===============================================")
    nama = input("Masukan nama untuk mencari data : ")
    print('\nResult')
    print("===============================================")
    print("|        Nama        |   NIM   | Tugas | UTS | UAS|  Akhir  |")
    if nama in data.keys():
        print("| {0:14} | {1:9} | {2:5} | {3:5} | {4:5} | {5:5}".format(nama, data[nama][1], data[nama][2], data[nama][3], data[nama][4], data[nama][5]))
        print("===============================================")
    else:
        print("'{}' tidak ditemukan.".format(nama))