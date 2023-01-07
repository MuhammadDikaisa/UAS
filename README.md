# Nama    : Muhammad Dikaisa I.A
# Nim     : 312210289
# Kelas   : TI.22.A.3

*<h2>Buatlah package dan modul dengan struktur seperti berikut :*

<img width="109" alt="1" src="https://user-images.githubusercontent.com/115516378/211126781-15b060c0-e42e-4d09-b86f-93c4c6d665a3.png">

*<h2>Didalam modul daftar_nilai.py terdapat beberapa fungsi sebagai berikut :*

*<h3>1. tambah_data*

```python
def tambah_data():
    global data
    ulangi = 'y'
    while ulangi =='y':
        nama = input_nama()
        nim = input_nim()
        nilai_tugas = input_ntugas()
        nilai_uts = input_nuts()
        nilai_uas = input_nuas()
        nilai_akhir = nakhir()
        data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]
        ulangi = (input('tambah data?(y/t) : '))

        if ulangi == 't':
            print('\nData berhasil di tambah!')
            return data
```       

*<h3>Output tambah_data :*


<img width="394" alt="3" src="https://user-images.githubusercontent.com/115516378/211127313-132ae0ad-c420-47aa-b037-a0ecafe39881.png">

*<h3> 2. ubah_data*

```python
def ubah_data():
    nama = input("Masukan nama untuk mengubah data: ")
    if nama in data.keys():
        print("\nMau mengubah apa?")
        sub_data = input("(Semua), (NIM), (Tugas), (UTS), (UAS) : ")
        if sub_data.lower() == "semua":
            print("==========================")
            print("Ubah data {}.".format(nama))
            print("==========================")
            data[nama][1] = input("Ubah NIM:")
            data[nama][2] = int(input("Ubah Nilai Tugas: "))
            data[nama][3] = int(input("Ubah Nilai UTS: "))
            data[nama][4] = int(input("Ubah Nilai UAS: "))
            data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100
            print("\nBerhasil ubah data!")

        elif sub_data.lower() == "nim":
            data[nama][1] = input("\nNIM:")
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "tugas":
            data[nama][2] = int(input("\nNilai Tugas: "))
            data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "uts":
            data[nama][3] = int(input("\nNilai UTS: "))
            data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "uas":
            data[nama][4] = int(input("\nNilai UAS: "))
            data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100
            print('\nData berhasil di ubah!')
        else:
            print("\nmenu tidak ditemukan.")

    else:
        print("'{}' tidak ditemukan.".format(nama))

```

*<h3>Output ubah_data :*

<img width="344" alt="4" src="https://user-images.githubusercontent.com/115516378/211127402-1ba387e5-e432-4c42-9617-d0364c764e67.png">


*<h3> 3. hapus_data*

```pyhton
def hapus_data():
    nama = input("Masukan nama untuk menghapus data : ")
    if nama in data.keys():
        del data[nama]
        print("\nData '{}' berhasil dihapus.".format(nama))
    else:
        print("'{}' tidak ditemukan.".format(nama))
```

*<h3>Output hapus_data*


<img width="382" alt="5" src="https://user-images.githubusercontent.com/115516378/211128081-e6a707ea-7449-4bb2-9986-f1c0ccacee5c.png">


*<h3> 4. cari_data*

```python
def cari_data():
    print("Mencari data: ")
    print("=================================================")
    nama = input("Masukan nama untuk mencari data: ")
    print('\nResult')
    print("==============================================================")
    print("|      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
    print("==============================================================")
    if nama in data.keys():
        print("| {0:14} | {1:9} | {2:5} | {3:5} | {4:5} | {5:5}"
            .format(nama, data[nama][1], data[nama][2], data[nama][3], data[nama][4], data[nama][5]))
        print('--------------------------------------------------------------')
    else:
        print("'{}' tidak ditemukan.".format(nama))
```

*<h3>Output cari_data*

<img width="373" alt="6" src="https://user-images.githubusercontent.com/115516378/211128173-f5895c5d-22bd-407d-a4d0-3f8daad83a61.png">

*<h2> Didalam Folder view terdapat modul input_nilai dan view_nilai sebagai berikut :*
*<h3>1. input_nilai :*
```python
# Menginput data
def input_nama():
    print("\nMasukkan data mahasiswa")
    print("...")
    global nama
    nama = input("\nNama: ")
    return nama


def input_nim():
    global nim
    nim = input("NIM: ")
    return nim


def input_ntugas():
    global nilai_tugas
    nilai_tugas = int(input("Masukkan nilai tugas: "))
    return nilai_tugas


def input_nuts():
    global nilai_uts
    nilai_uts = int(input("Masukkan nilai UTS: "))
    return nilai_uts


def input_nuas():
    global nilai_uas
    nilai_uas = int(input("Masukkan nilai UAS: "))
    return nilai_uas


# Nilai akhir
def nakhir():
    global nilai_akhir
    nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100
    return nilai_akhir
```

*<h3>Output dari modul input_nilai :*

<img width="373" alt="7" src="https://user-images.githubusercontent.com/115516378/211128462-4fdfa926-f73a-4018-a720-21fccc80c4a6.png">

*<h3>2. view_nilai :*

```pyhton
# Menampilkan data
from model.daftar_nilai import data

def lihat_data():
    print("Daftar Nilai:")
    print("===================================================================")
    print("| No |      Nama          |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
    print("===================================================================")
    if data.keys():
        no = 1
        for tabel in data.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                (no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
            print('-------------------------------------------------------------------')
            no += 1
    else:
        print("=========================TIDAK ADA DATA============================")
        print("===================================================================")
```

*<h3>Output dari modul view_nilai :*

<img width="415" alt="8" src="https://user-images.githubusercontent.com/115516378/211128579-50fe4f05-7927-4f07-9282-79c5fc8c5df6.png">

*<h2>Terakhir ada modul main.py*
*<h3>Di modul main.py inilah semua modul akan dikumpulkan, dan program akan dirun di modul main.py*

```python
from model.daftar_nilai import *
from view.view_nilai import *

#Mulai
print("===============================================================")
print("|                           Program                           |")
print("===============================================================")

while True:
    print("\n")
    menu = input("(L) Lihat, (T) Tambah, (H) Hapus, (U) Ubah, (C) Cari, (K) Keluar\nPilih menu: ")
    print("\n")

    # menu
    if menu.lower() == 't':
        tambah_data()

    elif menu.lower() == 'c':
        cari_data()

    elif menu.lower() == 'l':
        lihat_data()

    elif menu.lower() == 'u':
        ubah_data()

    elif menu.lower() == 'h':
        hapus_data()

    # Keluar
    elif menu.lower() == 'k':
        break

    else:
        print("Upss ada yang salah, silahkan cek kembali.")
```        

*<h3>Output dari modul ini*

<img width="391" alt="2" src="https://user-images.githubusercontent.com/115516378/211128741-fe08f76d-e827-4dcf-b531-22aa456ec663.png">


