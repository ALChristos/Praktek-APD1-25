import os

from Pack_Admin.Menu_A import pil_tanaman

def pil5_1(stok_PV):
    tambah_pupuk = input("Masukkan Jumlah Pupuk yang Ingin Ditambahkan : ")
    try:
        tambah_pupuk = int(tambah_pupuk)
        
        if tambah_pupuk:
            stok_PV[0]["pupuk"] += tambah_pupuk
            print(f"Stok Pupuk Berhasil Ditambahkan! Stok Pupuk Sekarang : {stok_PV[0]["pupuk"]}")
            input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
            os.system('cls' if os.name == 'nt' else 'clear')
            
    except ValueError:
        print("MASUKAN ANGKA!!!")
        input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
        os.system("cls" if os.name == "nt" else "clear")

def pil5_2(stok_PV):
    tambah_vitamin = input("Masukkan Jumlah Vitamin yang Ingin Ditambahkan : ")
    try:
        tambah_vitamin = int(tambah_vitamin)
        
        if tambah_vitamin:
            stok_PV[0]["vitamin"] += tambah_vitamin
            print(f"Stok Vitamin Berhasil Ditambahkan! Stok Vitamin Sekarang : {stok_PV[0]["vitamin"]}")
            input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
            os.system('cls' if os.name == 'nt' else 'clear')
        
    except ValueError:
        print("MASUKAN ANGKA!!!")
        input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
        os.system("cls" if os.name == "nt" else "clear")

def pil5_3(stok_PV, tanaman):
    if stok_PV[0]["pupuk"] > 0 and stok_PV[0]["vitamin"] > 0:
        pil_tanaman(tanaman) 
        pilih_tanaman = input("Pilih Nomor Tanaman yang Ingin Diberi Pupuk dan Vitamin : ")
        try: 
            pilih_tanaman = int(pilih_tanaman)
                
        except ValueError:
            print("MASUKAN ANGKA!!!")
            input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
            os.system("cls" if os.name == "nt" else "clear")             

    if pilih_tanaman <= len(tanaman):
        index = pilih_tanaman - 1 
        if tanaman[index]["pupuk dan vitamin"] == "Sudah Diberi Pupuk dan Vitamin":
            print(f"Tanaman {tanaman[index]['nama']} Sudah Pernah Diberi Pupuk dan Vitamin!")
            input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            tanaman[index]["pupuk dan vitamin"] = "Sudah Diberi Pupuk dan Vitamin"
            stok_PV[0]["pupuk"] -= 1
            stok_PV[0]["vitamin"] -= 1
            print(f"Tanaman {tanaman[index]["nama"]} Berhasil Diberi Pupuk dan Vitamin!")
            input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Nomor Tanaman Tidak Valid!")
        input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    lagi = input("Apakah Ingin Memberi Pupuk dan Vitamin Lagi?(Y/N)")
    if lagi.lower() == "y":
        os.system("cls" if os.name == "nt" else "clear")
        return pil5_3(stok_PV, tanaman)
    elif lagi.lower() == "n":
        os.system("cls" if os.name == "nt" else "clear")
        return
    else:
      print("PILIH Y/N JANGAN YANG LAIN!!!\n")
      os.system("cls" if os.name == "nt" else "clear")
      return pil5_3(stok_PV, tanaman)  
    
        
        
def pil5_4(tanaman):
    pil_tanaman(tanaman)
    pilih_tanaman = input("Pilih Nomor Tanaman yang Ingin Disiram : ")
    try:
        pilih_tanaman = int(pilih_tanaman)
    except ValueError:
        print("MASUKAN ANGKA!!!")
        input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
        os.system("cls" if os.name == "nt" else "clear")
    if pilih_tanaman <= len(tanaman):
        index = pilih_tanaman - 1 
        if tanaman[index]["penyiraman"] == "Sudah Disiram":
            print(f"Tanaman {tanaman[index]["nama"]} Sudah Pernah Disiram!")
            input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            tanaman[index]["penyiraman"] = "Sudah Disiram"
            print(f"Tanaman {tanaman[index]["nama"]} Berhasil Disiram!")
            input("Tekan Enter Untuk Kembali Ke Menu Pilihan 5")
            os.system('cls' if os.name == 'nt' else 'clear')
    
    lagi = input("Apakah Ingin Menyiram Tanaman Lagi?(Y/N)")
    if lagi.lower() == "y":
        os.system("cls" if os.name == "nt" else "clear")
        return pil5_4(tanaman)
    elif lagi.lower() == "n":
        os.system("cls" if os.name == "nt" else "clear")
        return
    else:
      print("PILIH Y/N JANGAN YANG LAIN!!!\n")
      os.system("cls" if os.name == "nt" else "clear")
      return pil5_4(tanaman)  
  

     