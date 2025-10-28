import os

from Pack_Admin.Menu_A import *
from Pack_Admin.Pilihan_A import *
from Pack_Member.Menu_M import *
from Pack_Member.Pilihan_M import *

akun = {
    "akun admin": ["Admin", "atmin123"],
    "akun member": ["User", "sayangatmin"],
}

tanaman = [
    {"nama": "Mawar",
     "jenis": "Bunga",
     "kondisi": "Sehat",
     "usia": "4 Minggu",
     "status": "Remaja",
     "pupuk dan vitamin": "Sudah Diberi Pupuk dan Vitamin",
     "penyiraman": "Belum Disiram"
    },
    {"nama": "Melati",
     "jenis": "Bunga",
     "kondisi": "Cekat",
     "usia": "5 Bulan",
     "status": "Tua",
     "pupuk dan vitamin": "Sudah Diberi Pupuk dan Vitamin",
     "penyiraman": "Sudah Disiram"
    },
    {"nama": "Bonsai",
     "jenis": "Pohon",
     "kondisi": "Sehat",
     "usia": "3 Bulan",
     "status": "Anakan",
     "pupuk dan vitamin": "Belum Diberi Pupuk dan Vitamin",
     "penyiraman": "Belum Disiram"
    },
    {"nama": "Beringin",
     "jenis": "Pohon",
     "kondisi": "Sehat",
     "usia": "12 Tahun",
     "status": "Tua",
     "pupuk dan vitamin": "Belum Diberi Pupuk dan Vitamin",
     "penyiraman": "Sudah Disiram"
    },
]
inventaris_U = {"hadiah": []}
laporan = {"laporan": []}
stok_PV = {"pupuk": 13,
           "vitamin": 8}
ulang = True


while ulang:
    print("="*58)
    print("=======SELAMAT DATANG DI APLIKASI SAMARENDAH GARDEN=======")
    print("\t===Silahkan Login Terlebih Dahulu===")
    print("="*58)
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    if username == akun["akun admin"][0] and password == akun["akun admin"][1]:
        print("Anda Berhasil Log in Sebagai ATMIN! Selamat Datang Min :)")
        while True:
            menu_admin()
            pilihan = input("Pilih Menu (1-7) : ")
            try:
             pilihan = int(pilihan)
            except ValueError:
             print("Pilihan harus berupa Angka dan Tidak boleh kosong!!!")
             input("Tekan Enter Untuk Menginput Ulang")
             os.system("cls" if os.name == "nt" else "clear")

            if pilihan == 1:
             pil1_admin(tanaman)

            elif pilihan == 2:
             pil2_admin(tanaman)
           
            elif pilihan == 3:
             pil3_admin(tanaman)

            elif pilihan == 4:
             pil4_admin(tanaman)
              
            elif pilihan == 5:
             pil5_admin(tanaman, stok_PV)

            elif pilihan == 6:
             pil6_admin(laporan, inventaris_U)
            elif pilihan == 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("Pilihan Tidak Valid! Silahkan Pilih Menu yang Tersedia")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

    elif username == akun["akun member"][0] and password == akun["akun member"][1]:
        print("Anda Berhasil Log in Sebagai MEMBER! Selamat Datang Member :)")
        while True:
            menu_member()
            pilihan = input("Pilih Menu (1-4) : ")
            try:
                pilihan = int(pilihan)   
            except ValueError:
                print("Pilihan harus berupa Angka dan Tidak boleh kosong!!!")
                input("Tekan Enter Untuk Menginput Ulang")
                os.system("cls" if os.name == "nt" else "clear")
               
            if pilihan == 1:
             pil1_member(tanaman)
                
            elif pilihan == 2:
             pil2_member(laporan)

            elif pilihan == 3:
             pil3_member(inventaris_U)  

            elif pilihan == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                break

    else:
     print("Akun Tidak Ada, Jangan Ngidul Le!!!")
     ulang = False






                        


                
                