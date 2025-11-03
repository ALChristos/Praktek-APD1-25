import os
import inquirer
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
inventaris_U = [{"hadiah": []}]
laporan = [{"laporan": []}]
stok_PV = [{"pupuk": 13,
           "vitamin": 8}]
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
            jawab = menu_admin()
           
            if jawab["menuA"][0] == "1":
             pil1_admin(tanaman)

            elif jawab["menuA"][0] == "2":
             pil2_admin(tanaman)
           
            elif jawab["menuA"][0] == "3":
             pil3_admin(tanaman)

            elif jawab["menuA"][0] == "4":
             pil4_admin(tanaman)
              
            elif jawab["menuA"][0] == "5":
             pil5_admin(tanaman, stok_PV)

            elif jawab["menuA"][0] == "6":
             pil6_admin(laporan, inventaris_U)
             
            elif jawab["menuA"][0] == "7":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

    elif username == akun["akun member"][0] and password == akun["akun member"][1]:
        print("Anda Berhasil Log in Sebagai MEMBER! Selamat Datang Member :)")
        while True:
            jawab = menu_member()
               
            if jawab["menuM"][0] == "1":
             pil1_member(tanaman)
                
            elif jawab["menuM"][0] == "2":
             pil2_member(laporan)

            elif jawab["menuM"][0] == "3":
             pil3_member(inventaris_U)  

            elif jawab["menuM"][0] == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

    else:
     print("Akun Tidak Ada, Jangan Ngidul Le!!!")
     ulang = False






                        


                
                