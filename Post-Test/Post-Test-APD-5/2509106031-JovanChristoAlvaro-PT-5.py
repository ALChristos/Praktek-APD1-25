import os

akun = [
    ["Admin", "atmin1234"],
    ["User", "member67"],
]
tanaman = [
    ["Mawar", "Bunga", "Sehat", "4 Minggu", "Remaja", "Sudah Diberi Pupuk dan Vitamin", "Belum Disiram"],
    ["Melati", "Bunga", "Cekat", "5 Bulan", "Tua", "Sudah Diberi Pupuk dan Vitamin", "Sudah Disiram"],
    ["Bonsai", "Pohon", "Sehat", "3 Bulan", "Anakan", "Belum Diberi Pupuk dan Vitamin", "Belum Disiram"],
    ["Beringin", "Pohon", "Sehat", "12 Tahun", "Tua", "Belum Diberi Pupuk dan Vitamin", "Sudah Disiram"],
]
inventaris_U =[]
laporan = []
stok_PV = [13,8]
ulang = True
  

while ulang:
    print("="*58)
    print("=======SELAMAT DATANG DI APLIKASI SAMARENDAH GARDEN=======")
    print("\t===Silahkan Login Terlebih Dahulu===")
    print("="*58)
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    if username == akun[0][0] and password == akun[0][1]:
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
            if pilihan == "1":
                print("="*58)
                print("===========Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i[0]}")
                    print(f"   Jenis Tanaman : {i[1]}")
                    print(f"   Kondisi Tanaman : {i[2]}")
                    print(f"   Lama Perawatan : {i[3]}")
                    print(f"   Usia Tanaman : {i[4]}")
                    print("-"*58)
                    nomor += 1
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "2":
                print("="*58)
                print("==========Menambah Tanaman di Samarendah Garden==========")
                print("="*58)
                nama = input("Masukkan Nama Tanaman : ")
                jenis = input("Masukkan Jenis Tanaman : ")
                kondisi = input("Masukkan Kondisi Tanaman : ")
                usia = input("Masukkan Usia Tanaman : ")
                status = input("Masukkan Status Usia Tanaman : ")
                tanaman_baru = [nama, jenis, kondisi, usia, status]
                tanaman.append(tanaman_baru)
                print(f"Tanaman {nama} Berhasil Ditambahkan!")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "3":
                print("="*58)
                print("==========Mengupdate Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i[0]}")
                    print(f"   Jenis Tanaman : {i[1]}")
                    print(f"   Kondisi Tanaman : {i[2]}")
                    print(f"   Lama Perawatan : {i[3]}")
                    print(f"   Usia Tanaman : {i[4]}")
                    print("-"*58)
                    nomor += 1
                pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Diupdate : "))
                if pilih_tanaman <= len(tanaman):
                    index = pilih_tanaman - 1
                    print(f"Anda Memilih Tanaman {tanaman[index][0]}")
                    tanaman[index][0]= input("Masukkan Nama Tanaman Baru (tekan enter kalau tidak ingin mengubah) : ")
                    tanaman[index][1] = input("Masukkan Jenis Tanaman Baru (tekan enter kalau tidak ingin mengubah) : ")
                    tanaman[index][2] = input("Masukkan Kondisi Tanaman Baru (tekan enter kalau tidak ingin mengubah) : ")
                    tanaman[index][3] = input("Masukkan Usia Tanaman Baru (tekan enter kalau tidak ingin mengubah) : ")
                    tanaman[index][4] = input("Masukkan Status Usia Tanaman Baru (tekan enter kalau tidak ingin mengubah) : ")
                    print(f"Data Tanaman {tanaman[index][0]} Berhasil Diupdate!")
                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("Nomor Tanaman Tidak Valid!")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "4":
                print("="*58)
                print("==========Menghapus Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i[0]}")
                    print(f"   Jenis Tanaman : {i[1]}")
                    print(f"   Kondisi Tanaman : {i[2]}")
                    print(f"   Lama Perawatan : {i[3]}")
                    print(f"   Usia Tanaman : {i[4]}")
                    print("-"*58)
                    nomor += 1
                pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Dihapus : "))
                if pilih_tanaman <= len(tanaman):
                    index = pilih_tanaman - 1
                    konfirmasi = input(f"Apakah Anda Yakin Ingin Menghapus Tanaman {tanaman[index][0]}? (y/n) : ")
                    if konfirmasi.lower() == 'y':
                        print(f"Tanaman Dengan Seri{tanaman.pop(index)}\n DI HAPUS!")
                        input("Tekan Enter Untuk Kembali ke Menu Utama")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print("Pikirkan Lagi Baik-baik")
                        input("Tekan Enter Untuk Kembali ke Menu Utama")
                        os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "5":
                print("="*58)
                print("==========Stok/Pemberian Pupuk, Stok/Pemberian Vitamin, dan Pemberian Air di Samarendah Garden==========")
                print("="*58)
                print(f"Stok Pupuk : {stok_PV[0]}")
                print(f"Stok Vitamin : {stok_PV[1]}")
                while True:
                    print("1. Tambah Stok Pupuk")
                    print("2. Tambah Stok Vitamin")
                    print("3. Beri Pupuk dan Vitamin ke Tanaman")
                    print("4. Beri Air ke Tanaman")
                    print("5. Kembali ke Menu Utama")
                    pilihan5 = input("Pilih Menu (1-5) : ")
                    if pilihan5 == "1":
                        tambah_pupuk = int(input("Masukkan Jumlah Pupuk yang Ingin Ditambahkan : "))
                        stok_PV[0] += tambah_pupuk
                        print(f"Stok Pupuk Berhasil Ditambahkan! Stok Pupuk Sekarang : {stok_PV[0]}")
                        input("Tekan Enter Untuk Kembali ke Menu Utama")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif pilihan5 == "2":
                        tambah_vitamin = int(input("Masukkan Jumlah Vitamin yang Ingin Ditambahkan : "))
                        stok_PV[1] += tambah_vitamin
                        print(f"Stok Vitamin Berhasil Ditambahkan! Stok Vitamin Sekarang : {stok_PV[1]}")
                        input("Tekan Enter Untuk Kembali ke Menu Utama")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif pilihan5 == "3":
                        if stok_PV[0] > 0 and stok_PV[1] > 0:
                            pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Diberi Pupuk dan Vitamin : "))
                            if pilih_tanaman <= len(tanaman):
                                index = pilih_tanaman - 1 
                                if tanaman[index][5] == "Sudah Diberi Pupuk dan Vitamin":
                                    print(f"Tanaman {tanaman[index][0]} Sudah Pernah Diberi Pupuk dan Vitamin!")
                                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                else:
                                    tanaman[index][5] = "Sudah Diberi Pupuk dan Vitamin"
                                    stok_PV[0] -= 1
                                    stok_PV[1] -= 1
                                    print(f"Tanaman {tanaman[index][0]} Berhasil Diberi Pupuk dan Vitamin!")
                                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print("Nomor Tanaman Tidak Valid!")
                                input("Tekan Enter Untuk Kembali ke Menu Utama")
                                os.system('cls' if os.name == 'nt' else 'clear')
                    elif pilihan5 == "4":
                        pilih_tanaman = int(input("Pilih Nomor Tanaman yang Ingin Disiram : "))
                        if pilih_tanaman <= len(tanaman):
                            index = pilih_tanaman - 1 
                            if tanaman[index][6] == "Sudah Disiram":
                                print(f"Tanaman {tanaman[index][0]} Sudah Pernah Disiram!")
                                input("Tekan Enter Untuk Kembali ke Menu Utama")
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                tanaman[index][6] = "Sudah Disiram"
                                print(f"Tanaman {tanaman[index][0]} Berhasil Disiram!")
                                input("Tekan Enter Untuk Kembali ke Menu Utama")
                                os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print("Kembali ke Menu Utama")
                        input("Tekan Enter Untuk Kembali ke Menu Utama")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

            elif pilihan == "6":
                print("="*58)
                print("==========Laporan Masalah di Samarendah Garden==========")
                print("="*58)
                if len(laporan) == 0:
                    print("Belum Ada Laporan Masalah")
                else:
                    nomor = 1
                    for i in laporan:
                        print(f"{nomor}. {i}")
                        nomor += 1
                        print("-"*58)
                    penyelesaian = int(input(" Masalah Mana yang Sudah Diatasi?(Masukan Nomornya) : "))
                    if penyelesaian <= len(laporan):
                        index = penyelesaian - 1
                        print(f"Masalah Dengan Seri {laporan.pop(index)}\n DI ATASI!")
                        hadiah = input("Berikan Hadiah Kepada Member yang Melapor: ")
                        inventaris_U.append(hadiah)
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

    elif username == akun[1][0] and password == akun[1][1]:
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
            if pilihan == "1":
                print("="*58)
                print("===========Data Tanaman di Samarendah Garden==========")
                print("="*58)
                nomor = 1
                for i in (tanaman):
                    print(f"{nomor}. Nama Tanaman : {i[0]}")
                    print(f"   Jenis Tanaman : {i[1]}")
                    print(f"   Kondisi Tanaman : {i[2]}")
                    print(f"   Lama Perawatan : {i[3]}")
                    print(f"   Usia Tanaman : {i[4]}")
                    print("-"*58)
                    nomor += 1
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "2":
                print("="*58)
                print("==========Melapor Masalah di Samarendah Garden==========")
                print("="*58)
                masalah = input("Masukkan Masalah yang Ingin Dilaporkan : ")
                laporan.append(masalah)
                print("Laporan Berhasil Dikirim! Terima Kasih Sudah Melapor :)")
                print("Admin Akan Segera Menindaklanjuti Laporan Anda")
                print("Sebagai Bentuk Kasih Sayang Admin Terhadap Member, Admin Akan Memberikan Hadiah")
                input("Tekan Enter Untuk Kembali ke Menu Utama")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif pilihan == "3":
                print("="*58)
                print("==========Hadiah dari Admin Samarendah Garden==========")
                print("="*58)
                if len(inventaris_U) == 0:
                    print("Belum Ada Hadiah dari Admin")
                    input("Tekan Enter Untuk Kembali ke Menu Utama")
                    os.system('cls' if os.name == 'nt' else 'clear')

                else:
                    nomor = 1
                    for i in inventaris_U:
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





                    
                

                        


                
                