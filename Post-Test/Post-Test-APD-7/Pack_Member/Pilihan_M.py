import os

from Pack_Admin.Menu_A import pil_tanaman


def pil1_member(tanaman):
    print("="*58)
    print("===========Data Tanaman di Samarendah Garden==========")
    print("="*58)
    pil_tanaman(tanaman)
    input("Tekan Enter Untuk Kembali ke Menu Utama")
    os.system('cls' if os.name == 'nt' else 'clear')


def pil2_member(laporan):
    print("="*58)
    print("==========Melapor Masalah di Samarendah Garden==========")
    print("="*58)
    try:
        masalah = input("Masukkan Masalah yang Ingin Dilaporkan : ")

        if masalah[0] in "1234567890" or masalah == "":
            raise ValueError("KALAU NGASIH TAU MASALAH YANG JELAS LE!!!\n")

        laporan["laporan"].append(masalah)
        print("Laporan Berhasil Dikirim! Terima Kasih Sudah Melapor :)")
        print("Admin Akan Segera Menindaklanjuti Laporan Anda")
        print("Sebagai Bentuk Kasih Sayang Admin Terhadap Member, Admin Akan Memberikan Hadiah")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    except ValueError as e:
        print(e)
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
def pil3_member(inventaris_U):
    print("="*58)
    print("==========Hadiah dari Admin Samarendah Garden==========")
    print("="*58)
    if len(inventaris_U["hadiah"]) == 0:
        print("Belum Ada Hadiah dari Admin")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        nomor = 1
        for i in inventaris_U.values():
            print(f"{nomor}. {i}")
            nomor += 1
            print("-"*58)
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear') 
