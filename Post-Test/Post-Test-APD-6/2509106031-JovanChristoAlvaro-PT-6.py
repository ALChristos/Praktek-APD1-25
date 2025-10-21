import os

akun = {
    "akun admin" : ["Admin", "atmin123"],
    "akun member" : ["User", "sayangatmin"],
}

tanaman = [
    {"nama":"Mawar", 
     "jenis":"Bunga", 
     "kondisi":"Sehat",
     "usia":"4 Minggu", 
     "status":"Remaja", 
     "pupuk dan vitamin":"Sudah Diberi Pupuk dan Vitamin",
     "penyiraman":"Belum Disiram"
    },
    {"nama":"Melati",
     "jenis":"Bunga", 
     "kondisi":"Cekat", 
     "usia":"5 Bulan", 
     "status":"Tua", 
     "pupuk dan vitamin":"Sudah Diberi Pupuk dan Vitamin", 
     "penyiraman":"Sudah Disiram"
    },
    {"nama":"Bonsai", 
     "jenis":"Pohon", 
     "kondisi":"Sehat", 
     "usia":"3 Bulan", 
     "status":"Anakan", 
     "pupuk dan vitamin":"Belum Diberi Pupuk dan Vitamin", 
     "penyiraman":"Belum Disiram"
    },
    {"nama":"Beringin", 
     "jenis":"Pohon", 
     "kondisi":"Sehat", 
     "usia":"12 Tahun", 
     "status":"Tua", 
     "pupuk dan vitamin":"Belum Diberi Pupuk dan Vitamin", 
     "penyiraman":"Sudah Disiram"
    },
]
inventaris_U ={"hadiah": []}
laporan = {"laporan": []}
stok_PV = {"pupuk":13,
           "vitamin":8}
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
            print("="*58)
            print("\t============Menu Utama==============")
            print("="*58)
            print("1. Lihat Data Tanaman")
            print("2. Tambah Tanaman")
            print("3. Update Data Tanaman")
            print("4. Hapus Data Tanaman")
            print("5. Lihat dan Atur Stok/Pemberian Pupuk, Stok/Pemberian Vitamin, dan Pemberian Air")
            print("6. Lihat Laporan Laporan Masalah")
            print("7. Kembali ke Menu Login")
            print("="*58)
            pilihan = input("Pilih Menu (1-7) : ") 
            ada_angka = False
            for i in pilihan:
                if i in "1234567890":
                    ada_angka = True
                    break
            if not ada_angka or pilihan == "":
                print("INPUT HARUS BERUPA ANGKA DAN JANGAN KOSONG!!!")
                input("Tekan Enter Untuk Menginput Ulang")
                os.system("cls" if os.name == "nt" else "clear")
                continue
                      
            if pilihan == "1":
                print("="*58)
                print("===========Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i["nama"]}")
                    print(f"   Jenis Tanaman : {i["jenis"]}")
                    print(f"   Kondisi Tanaman : {i["kondisi"]}")
                    print(f"   Usia Tanaman : {i["usia"]}")
                    print(f"   Status Usia Tanaman : {i["status"]}")
                    print(f"   Pupuk dan Vitamin: {i["pupuk dan vitamin"]}")
                    print(f"   Status Penyiraman: {i["penyiraman"]}")
                    print("-"*58)
                    nomor += 1
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "2":
                ulang_pilihan = True
                while ulang_pilihan:
                    print("="*58)
                    print("==========Menambah Tanaman di Samarendah Garden==========")
                    print("="*58)
                    nama = input("Masukkan Nama Tanaman : ")
                    jenis = input("Masukkan Jenis Tanaman : ")
                    kondisi = input("Masukkan Kondisi Tanaman : ")
                    usia = input("Masukkan Usia Tanaman : ")
                    status = input("Masukkan Status Usia Tanaman : ")
                    pukvit = input("Masukan Status Pemupukan dan Vitamin : ")
                    penyiraman = input("Masukan Status Penyiraman : ")
                    ada_angka = False
                    for i in usia:
                     if i in "1234567890":
                        ada_angka = True
                        break
                    if not ada_angka:
                     print("USIA HARUS ADA ANGKANYA WOI!!!")
                     input("Tekan Enter Untuk Menginput Ulang")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     continue
                    elif usia == "":
                     print("USIA GAK BOLEH KOSONG WOI!!!")
                     input("Tekan Enter Untuk Menginput Ulang")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     continue
                    elif usia[0] not in "1234567890":
                     print("USIA HARUS PAKAI ANGKA WOI!!!")
                     input("Tekan Enter Untuk Menginput Ulang")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     continue

                    teks_valid = True
                    for i in nama + jenis + kondisi + status + pukvit + penyiraman:
                     if i in "1234567890":
                        teks_valid = False
                        break
                    if not teks_valid or nama == "" or jenis == "" or kondisi == "" or pukvit == "" or penyiraman == "":
                        print("NAMA, JENIS, KONDISI DAN STATUS DARI TANAMAN GAK BISA PAKAI ANGKA DAN GAK BISA KOSONG WOI!!!")
                        input("Tekan Enter Untuk Menginput Ulang")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    tanaman_baru = {"nama":nama,
                                    "jenis":jenis, 
                                    "kondisi":kondisi, 
                                    "usia":usia, 
                                    "status":status, 
                                    "pupuk dan vitamin":pukvit, 
                                    "penyiraman":penyiraman}
                    tanaman.append(tanaman_baru)
                    print(f"Tanaman {nama} Berhasil Ditambahkan!")
                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ulang_pilihan = False
           
            elif pilihan == "3":
             ulang_pilihan = True
             while ulang_pilihan:
                print("="*58)
                print("==========Mengupdate Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i["nama"]}")
                    print(f"   Jenis Tanaman : {i["jenis"]}")
                    print(f"   Kondisi Tanaman : {i["kondisi"]}")
                    print(f"   Usia Tanaman : {i["usia"]}")
                    print(f"   Status Usia Tanaman : {i["status"]}")
                    print(f"   Pupuk dan Vitamin: {i["pupuk dan vitamin"]}")
                    print(f"   Status Penyiraman: {i["penyiraman"]}")
                    print("-"*58)
                    nomor += 1
                pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Diupdate : "))
                if pilih_tanaman <= len(tanaman):
                    index = pilih_tanaman - 1
                    print(f"Anda Memilih Tanaman {tanaman[index]["nama"]}")
                    nama_baru = input("Masukkan Nama Tanaman Baru : ")
                    jenis_baru = input("Masukkan Jenis Tanaman Baru : ")
                    kondisi_baru = input("Masukkan Kondisi Tanaman Baru : ")
                    usia_baru = input("Masukkan Usia Tanaman Baru : ")
                    status_baru = input("Masukkan Status Usia Tanaman Baru : ")
                    pukvit_baru = input("Masukkan Status Pupuk dan Vitamin Tanaman Baru : ")
                    siram_baru = input("Masukkan Status Penyiraman Tanaman Baru : " )
                    ada_angka = False
                    for i in usia_baru:
                        if i in "1234567890":
                            ada_angka = True
                    if not ada_angka:
                     print("USIA HARUS ADA ANGKANYA WOI!!!")
                     input("Tekan Enter Untuk Menginput Ulang")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     continue
                    elif  usia_baru == "":
                     print("USIA GAK BOLEH KOSONG WOI!!!")
                     input("Tekan Enter Untuk Menginput Ulang")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     continue
                    elif usia_baru[0] not in "1234567890":
                     print("USIA HARUS PAKAI ANGKA WOI!!!")
                     input("Tekan Enter Untuk Menginput Ulang")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     continue

                    teks_valid = True
                    for i in nama_baru + jenis_baru + kondisi_baru + status_baru +  pukvit_baru + siram_baru:
                     if i not in "1234567890":
                      teks_valid = False
                      break
                    if not teks_valid or nama_baru == "" or jenis_baru == "" or kondisi_baru == "" or usia_baru == "" or status_baru == "" or pukvit_baru == "" or siram_baru:
                     print("NAMA, JENIS, KONDISI DAN STATUS DARI TANAMAN GAK BISA PAKAI ANGKA DAN GAK BISA KOSONG WOI!!!")
                     input("Tekan Enter Untuk Menginput Ulang")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     continue
                    if (nama_baru == "" and jenis_baru == "" and kondisi_baru == "" and usia_baru == "" and status_baru == "" and pukvit_baru == "" and siram_baru == ""):
                        print("Tidak ada perubahan yang dilakukan. Data tetap sama.")
                        input("Tekan Enter Untuk Kembali ke Menu Utama")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue  
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

            elif pilihan == "4":
              ulang_pilihan = True
              while ulang_pilihan:
                print("="*58)
                print("==========Menghapus Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i["nama"]}")
                    print(f"   Jenis Tanaman : {i["jenis"]}")
                    print(f"   Kondisi Tanaman : {i["kondisi"]}")
                    print(f"   Usia Tanaman : {i["usia"]}")
                    print(f"   Status Usia Tanaman : {i["status"]}")
                    print(f"   Pupuk dan Vitamin: {i["pupuk dan vitamin"]}")
                    print(f"   Status Penyiraman: {i["penyiraman"]}")
                    print("-"*58)
                    nomor += 1
                pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Dihapus : "))
                if pilih_tanaman <= len(tanaman):
                    index = pilih_tanaman - 1
                    konfirmasi = input(f"Apakah Anda Yakin Ingin Menghapus Tanaman {tanaman[index]["nama"]}? (y/n) : ")
                    if konfirmasi.lower() == 'y':
                        print(f"Tanaman Dengan Seri{tanaman.pop(index)}\n DI HAPUS!")
                        input("Tekan Enter Untuk Kembali ke Menu Utama")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        ulang_pilihan = False
                    else:
                     print("Pikirkan Lagi Baik-baik")
                     input("Tekan Enter Untuk Kembali ke Menu Utama")
                     os.system('cls' if os.name == 'nt' else 'clear')
                     ulang_pilihan = False

            elif pilihan == "5":
                ulang_pilihan = True
                while ulang_pilihan:
                 print("="*58)
                 print("==========Stok/Pemberian Pupuk, Stok/Pemberian Vitamin, dan Pemberian Air di Samarendah Garden==========")
                 print("="*58)
                 print("="*58)   
                 print("1. Tambah Stok Pupuk")
                 print("2. Tambah Stok Vitamin")
                 print("3. Beri Pupuk dan Vitamin ke Tanaman")
                 print("4. Beri Air ke Tanaman")
                 print("5. Kembali ke Menu Utama")
                 print(f"Stok Pupuk : {stok_PV["pupuk"]}")
                 print(f"Stok Vitamin : {stok_PV["vitamin"]}")
                 print("="*58)   
                 pilihan5 = input("Pilih Menu (1-5) : ")
                 if pilihan5 == "1":
                    tambah_pupuk = int(input("Masukkan Jumlah Pupuk yang Ingin Ditambahkan : "))
                    stok_PV["pupuk"] += tambah_pupuk
                    print(f"Stok Pupuk Berhasil Ditambahkan! Stok Pupuk Sekarang : {stok_PV["pupuk"]}")
                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                    os.system('cls' if os.name == 'nt' else 'clear')
                 elif pilihan5 == "2":
                    tambah_vitamin = int(input("Masukkan Jumlah Vitamin yang Ingin Ditambahkan : "))
                    stok_PV["vitamin"] += tambah_vitamin
                    print(f"Stok Vitamin Berhasil Ditambahkan! Stok Vitamin Sekarang : {stok_PV["vitamin"]}")
                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                    os.system('cls' if os.name == 'nt' else 'clear')
                 elif pilihan5 == "3":
                    if stok_PV["pupuk"] > 0 and stok_PV["vitamin"] > 0:
                        nomor = 1
                        for i in (tanaman):
                            print(f"{nomor}. Nama Tanaman : {i["nama"]}")
                            print(f"   Jenis Tanaman : {i["jenis"]}")
                            print(f"   Kondisi Tanaman : {i["kondisi"]}")
                            print(f"   Usia Tanaman : {i["usia"]}")
                            print(f"   Status Usia Tanaman : {i["status"]}")
                            print(f"   Pupuk dan Vitamin: {i["pupuk dan vitamin"]}")
                            print(f"   Status Penyiraman: {i["penyiraman"]}")
                            print("-"*58)
                            nomor += 1
                        pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Diberi Pupuk dan Vitamin : "))
                        if pilih_tanaman <= len(tanaman):
                            index = pilih_tanaman - 1 
                            if tanaman[index]["pupuk dan vitamin"] == "Sudah Diberi Pupuk dan Vitamin":
                                print(f"Tanaman {tanaman[index]['nama']} Sudah Pernah Diberi Pupuk dan Vitamin!")
                                input("Tekan Enter Untuk Kembali ke Menu Utama")
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                tanaman[index]["pupuk dan vitamin"] = "Sudah Diberi Pupuk dan Vitamin"
                                stok_PV["pupuk"] -= 1
                                stok_PV["vitamin"] -= 1
                                print(f"Tanaman {tanaman[index]["nama"]} Berhasil Diberi Pupuk dan Vitamin!")
                                input("Tekan Enter Untuk Kembali ke Menu Utama")
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print("Nomor Tanaman Tidak Valid!")
                            input("Tekan Enter Untuk Kembali ke Menu Utama")
                            os.system('cls' if os.name == 'nt' else 'clear')
                 elif pilihan5 == "4":
                    nomor = 1
                    for i in (tanaman):
                        print(f"{nomor}. Nama Tanaman : {i["nama"]}")
                        print(f"   Jenis Tanaman : {i["jenis"]}")
                        print(f"   Kondisi Tanaman : {i["kondisi"]}")
                        print(f"   Usia Tanaman : {i["usia"]}")
                        print(f"   Status Usia Tanaman : {i["status"]}")
                        print(f"   Pupuk dan Vitamin: {i["pupuk dan vitamin"]}")
                        print(f"   Status Penyiraman: {i["penyiraman"]}")
                        print("-"*58)
                        nomor += 1
                    pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Disiram : "))
                    if pilih_tanaman <= len(tanaman):
                        index = pilih_tanaman - 1 
                        if tanaman[index]["penyiraman"] == "Sudah Disiram":
                            print(f"Tanaman {tanaman[index]["nama"]} Sudah Pernah Disiram!")
                            input("Tekan Enter Untuk Kembali ke Menu Utama")
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            tanaman[index]["penyiraman"] = "Sudah Disiram"
                            print(f"Tanaman {tanaman[index]["nama"]} Berhasil Disiram!")
                            input("Tekan Enter Untuk Kembali ke Menu Utama")
                            os.system('cls' if os.name == 'nt' else 'clear')
                 else:
                    print("Kembali ke Menu Utama")
                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ulang_pilihan = False

            elif pilihan == "6":
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
            elif pilihan == "7":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("Pilihan Tidak Valid! Silahkan Pilih Menu yang Tersedia")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

    elif username == akun["akun member"][0] and password == akun["akun member"][1]:
        print("Anda Berhasil Log in Sebagai MEMBER! Selamat Datang Member :)")
        while True:
            print("="*58)
            print("\t============Menu Utama==============")
            print("="*58)
            print("1. Lihat Data Tanaman")
            print("2. Lapor Masalah pada Tanaman")
            print("3. Lihat Hadiah dari Admin")
            print("4. Kembali ke Menu Login")
            print("="*58)
            pilihan = input("Pilih Menu (1-4) : ")    
            ada_angka = False
            for i in pilihan:
                if i in "1234567890":
                    ada_angka = True
                    break
            if not ada_angka or pilihan == "":
                print("INPUT HARUS BERUPA ANGKA DAN JANGAN KOSONG!!!")
                input("Tekan Enter Untuk Menginput Ulang")
                os.system("cls" if os.name == "nt" else "clear")
                continue  
                
            if pilihan == "1":
                print("="*58)
                print("===========Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i["nama"]}")
                    print(f"   Jenis Tanaman : {i["jenis"]}")
                    print(f"   Kondisi Tanaman : {i["kondisi"]}")
                    print(f"   Usia Tanaman : {i["usia"]}")
                    print(f"   Status Usia Tanaman : {i["status"]}")
                    print(f"   Pupuk dan Vitamin: {i["pupuk dan vitamin"]}")
                    print(f"   Status Penyiraman: {i["penyiraman"]}")
                    print("-"*58)
                    nomor += 1
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "2":
                print("="*58)
                print("==========Melapor Masalah di Samarendah Garden==========")
                print("="*58)
                masalah = input("Masukkan Masalah yang Ingin Dilaporkan : ")
                teks_valid = False
                for i in masalah:
                    if i not in "1234567890":
                     teks_valid = True
                if not teks_valid:
                    print("NAH INI MASUKAN TEKS BUKAN ANGKA WOI!!!")
                    input("Tekan Enter Untuk Menginput Ulang")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                laporan["laporan"].append(masalah)
                print("Laporan Berhasil Dikirim! Terima Kasih Sudah Melapor :)")
                print("Admin Akan Segera Menindaklanjuti Laporan Anda")
                print("Sebagai Bentuk Kasih Sayang Admin Terhadap Member, Admin Akan Memberikan Hadiah")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "3":
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

            elif pilihan == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

    else:
     print("Akun Tidak Ada, Jangan Ngidul Le!!!")
     ulang = False






                        


                
                