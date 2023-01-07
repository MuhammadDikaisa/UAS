from model.daftar_nilai import *
from view.view_nilai import *

print("======================================================================")
print("|                             PROGRAM                                |")
print("======================================================================")

while True:
    print("\n")
    menu = input("(L)Lihat, (T)Tambah, (H)Hapus, (U)Ubah, (C)Cari, (K)Keluar\nPilih menu : ")
    print("\n")
    
    if menu.lower() == 't':
        tambah_data()
    
    elif menu.lower() == 'c':
        cari_data()
        
    elif menu.lower() == 'l':
        lihat_data()
        
    elif menu.lower() == 'u':
        ubah_data()
        
    elif menu.lower == 'h':
        hapus_data()
        
    elif menu.lower == 'k':
        break
    
    else:
        print("Sepertinya ada yang salah, silahkan di cek kembali ya.")