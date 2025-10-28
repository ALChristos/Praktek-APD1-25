import os

from Pack_Admin.Menu_A import pil_tanaman, menu_pil5
from Pack_Admin.Pilihan5_A import * 

def pil1_admin(tanaman):
    print("="*58)
    print("===========Data Tanaman di Samarendah Garden==========")
    print("="*58)
    pil_tanaman(tanaman)
    input("Tekan Enter Untuk Kembali ke Menu Utama")
    os.system('cls' if os.name == 'nt' else 'clear')


def pil2_admin(tanaman):
    ulang_pilihan = True
    while ulang_pilihan:
        print("="*58)
        print("==========Menambah Tanaman di Samarendah Garden==========")
        print("="*58)
        try:
            nama = input("Masukkan Nama Tanaman : ")
            usia = input("Masukkan Usia Tanaman : ")
            jenis = input("Masukkan Jenis Tanaman : ")
            kondisi = input("Masukkan Kondisi Tanaman : ")
            status = input("Masukkan Status Usia Tanaman : ")
            pukvit = input("Masukan Status Pemupukan dan Vitamin : ")
            penyiraman = input("Masukan Status Penyiraman : ")
            if nama == "" or usia == "" or jenis == "" or kondisi == "" or status == "" or pukvit == "" or penyiraman == "":
                raise ValueError("NAMA, USIA, JENIS, KONDISI DAN STATUS DARI TANAMAN GAK BISA KOSONG WOI!!!\n")
            elif len(usia) > 0 and usia[0] not in "1234567890":
                 raise ValueError("USIA HARUS ADA ANGKANYA!!!\n")
            
            for i in nama + jenis + kondisi + status + pukvit + penyiraman:
                if i in "1234567890":
                    raise ValueError("NAMA, JENIS, KONDISI DAN STATUS DARI TANAMAN GAK BISA PAKAI ANGKA WOI!!!\n")
                    
            tanaman_baru = {"nama": nama,
                            "jenis": jenis,
                            "kondisi": kondisi,
                            "usia": usia,
                            "status": status,
                            "pupuk dan vitamin": pukvit,
                            "penyiraman": penyiraman}
            tanaman.append(tanaman_baru)
            print(f"Tanaman {nama} Berhasil Ditambahkan!")

        except ValueError as e:
            print(f"Error : {e}\n")
            input("Tekan Enter Untuk Menginput Ulang\n")
            os.system("cls" if os.name == "nt" else "clear")
            
        lagi = input("Apakah Ingin Menambah Tanaman Yang Lain?(Y/N)")  
        if lagi.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            return pil2_admin(tanaman)
        elif lagi.lower() == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            ulang_pilihan = False
            return
        else:
            print("PILIH Y/N JANGAN YANG LAIN!!!\n")
            return pil2_admin(tanaman)

           
def pil3_admin(tanaman):
    ulang_pilihan = True
    while ulang_pilihan:
        print("="*58)
        print("==========Mengupdate Data Tanaman di Samarendah Garden==========")
        print("="*58)
        pil_tanaman(tanaman)
        pilih_tanaman = input("Pilih Nomor Tanaman yang Ingin Diupdate : ")
        try:
            pilih_tanaman = int(pilih_tanaman)
        except ValueError:
            print("MASUKAN ANGKA!!!\n")
            input("Tekan Enter Untuk Menginput Ulang")
            os.system("cls" if os.name == "nt" else "clear")
            continue
        try:   
            if pilih_tanaman <= len(tanaman):
                index = pilih_tanaman - 1
                print(f"Anda Memilih Tanaman {tanaman[index]["nama"]}")
                nama_baru = input("Masukkan Nama Tanaman Baru : ")
                jenis_baru = input("Masukkan Jenis Tanaman Baru : ")
                kondisi_baru = input("Masukkan Kondisi Tanaman Baru : ")
                usia_baru = input("Masukkan Usia Tanaman Baru : ")
                status_baru = input("Masukkan Status Usia Tanaman Baru : ")
                pukvit_baru = input("Masukkan Status Pupuk dan Vitamin Tanaman Baru : ")
                siram_baru = input("Masukkan Status Penyiraman Tanaman Baru : ")
                if len(usia_baru) > 0 and usia_baru[0] not in "1234567890":
                    raise ValueError("USIA HARUS ADA ANGKANYA!!!\n")
                elif (nama_baru == "" or jenis_baru == "" or kondisi_baru == "" or usia_baru == "" or status_baru == "" or pukvit_baru == "" or siram_baru == ""):
                   raise ValueError("NAMA, USIA, JENIS, KONDISI DAN STATUS DARI TANAMAN GAK BISA KOSONG WOI!!!\n")
               
                for i in nama_baru + jenis_baru + kondisi_baru + status_baru + pukvit_baru + siram_baru:
                    if i in "1234567890":
                        raise ValueError("NAMA, JENIS, KONDISI DAN STATUS DARI TANAMAN GAK BISA PAKAI ANGKA WOI!!!\n")
                        
                if nama_baru:
                    tanaman[index]["nama"] = nama_baru
                if jenis_baru:
                    tanaman[index]["jenis"] = jenis_baru
                if kondisi_baru:
                    tanaman[index]["kondisi"] = kondisi_baru
                if usia_baru:
                    tanaman[index]["usia"] = usia_baru
                if status_baru:
                    tanaman[index]["status"] = status_baru
                if pukvit_baru:
                    tanaman[index]["pupuk dan vitamin"] = pukvit_baru
                if siram_baru:
                    tanaman[index]["penyiraman"] = siram_baru
                print(f"Data Tanaman {tanaman[index]["nama"]} Berhasil Diupdate!")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Nomor Tanaman Tidak Valid!")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')
                ulang_pilihan = False
                            
        except ValueError as e:
            print(f"Error : {e}\n")
            input("Tekan Enter Untuk Menginput Ulang")
            os.system("cls" if os.name == "nt" else "clear")
            
        lagi = input("Apakah Ingin Mengupdate Tanaman Yang Lain?(Y/N)")  
        if lagi.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            return pil3_admin(tanaman)
        elif lagi.lower() == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            ulang_pilihan = False
            return
        else:
            print("PILIH Y/N JANGAN YANG LAIN!!!\n")
            return pil3_admin(tanaman)
            


def pil4_admin(tanaman):
    ulang_pilihan = True
    while ulang_pilihan:
        print("="*58)
        print("==========Menghapus Data Tanaman di Samarendah Garden==========")
        print("="*58)
        pil_tanaman(tanaman)
        pilih_tanaman = input("Pilih Nomor Tanaman yang Ingin Dihapus : ")
        try:
            pilih_tanaman = int(pilih_tanaman)
        except ValueError:
            print("MASUKAN ANGKA!!!")
            input("Tekan Enter Untuk Menginput Ulang")
            os.system("cls" if os.name == "nt" else "clear")
            continue
        
        if pilih_tanaman <= len(tanaman):
            index = pilih_tanaman - 1
            try:
                konfirmasi = input(f"Apakah Anda Yakin Ingin Menghapus Tanaman {tanaman[index]["nama"]}? (y/n) : ")
                for i in konfirmasi:
                    if i not in "ynYN":
                        raise ValueError("PILIH Y/N JANGAN YANG LAIN!!!\n")   
                if konfirmasi.lower() == 'y':
                    print(f"Tanaman Dengan Seri{tanaman.pop(index)}\n DI HAPUS!\n")
                    input("Tekan Enter")
                else:
                    print("Pikirkan Lagi Baik-baik\n")
                    input("Tekan Enter")
                   
            except ValueError as e:
                print(f"Error : {e}\n")
                input("Tekan Enter Untuk Menginput Ulang")
                os.system("cls" if os.name == "nt" else "clear")
                continue
        else:
            print("Tidak Ada Tanaman Yang Tersisa/Nomor Tanaman Tidak Tersedia")   
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')
            ulang_pilihan = False
            
        lagi = input("Apakah Ingin Menghapus Tanaman Yang Lain?(Y/N)")  
        if lagi.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            return pil4_admin(tanaman)
        elif lagi.lower() == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            ulang_pilihan = False
            return
        else:
            print("PILIH Y/N JANGAN YANG LAIN!!!\n")
            return pil4_admin(tanaman)
                
                          
def pil5_admin(tanaman,stok_PV):
     ulang_pilihan = True
     while ulang_pilihan:
        menu_pil5(stok_PV)
        pilihan5 = input("Pilih Menu (1-5) : ")
        try:
            pilihan5 = int(pilihan5)
        except ValueError:
            print("MASUKAN ANGKA!!!")
            input("Tekan Enter Untuk Menginput Ulang")
            os.system("cls" if os.name == "nt" else "clear")
            continue
        if pilihan5 == 1:
            pil5_1(stok_PV)
            
        elif pilihan5 == 2:
            pil5_2(stok_PV)
                  
        elif pilihan5 == 3:
            pil5_3(stok_PV, tanaman) 
               
        elif pilihan5 == 4:
            pil5_4(tanaman)       
        else:
            print("Kembali ke Menu Utama")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')
            ulang_pilihan = False
            

def pil6_admin(laporan, inventaris_U):
    print("="*58)
    print("==========Laporan Masalah di Samarendah Garden==========")
    print("="*58)
    if len(laporan["laporan"]) == 0:
        print("Belum Ada Laporan Masalah")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        nomor = 1
        for i in laporan.values():
            print(f"{nomor}. {i}")
            nomor += 1
            print("-"*58)
        penyelesaian = int(input(" Masalah Mana yang Sudah Diatasi?(Masukan Nomornya) : "))
        if penyelesaian <= len(laporan["laporan"]):
            index = penyelesaian - 1
            print(f"Masalah Dengan Seri {laporan["laporan"].pop(index)}\n DI ATASI!")
            hadiah = input("Berikan Hadiah Kepada Member yang Melapor: ")
            inventaris_U["hadiah"].append(hadiah)
            print(f"Hadiah {hadiah} Berhasil Diberikan Kepada Member yang Melapor!")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Nomor Laporan Tidak Valid!")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')
    

