def input_nama():
    print("\nMasukan data Mahasiswa : ")
    print(". . .")
    global nama
    nama= input("\nNama : ")
    return nama

def input_nim():
    global nim 
    nim = input("\nNim : ")
    return nim

def input_ntugas():
    global nilai_tugas
    nilai_tugas = int(input("Masukan nilai Tugas : "))
    return nilai_tugas

def input_nuts():
    global nilai_uts
    nilai_uts = int(input("Masukan nilai Uts : "))
    return nilai_uts

def input_nuas():
    global nilai_uas 
    nilai_uas = int(input("Masukan nilau Uas : "))
    return nilai_uas

def nakhir():
    global nilai_akhir
    nilai_akhir = (nilai_tugas) * 30/100 + (nilai_uts) * 35/100 + (nilai_uas) * 35/100
    return nilai_akhir