import os #import os untuk membersihkan layar, dan os.system nya ada di baris 87
          #agar dapat menampilkan pesan di terminal terlebih dahulu sebelum membersihkan layar

nama = "Jovan"
nim = "031"
perulangan = 0
max_perulangan = 5

while perulangan < max_perulangan:
    print("====="*14)
    print("=======SELAMAT DATANG DI RENTAL MOBIL CABANG PATI CINTA DAMAI=========")
    print("====="*14)
    username = input("Masukkan username anda: ")
    password = input("Masukkan password anda: ")
    if username == nama and password == nim:
        print("====="*14)
        print("\t================ANDA BERHASIL LOGIN!=================")
        print("====="*14)
        print("\t========RENTAL MOBIL CABANG PATI CINTA DAMAI=========")
        print("====="*14)
        print("\t====Silahkan masukan biodata anda terlebih dahulu====")
        print("====="*14)
        nama = input("Masukan nama anda : ")
        usia = int(input("Masukan usia anda : "))
        sim = input("Apakah anda memiliki SIM? (ada/tidak) : ")
        deposit = int(input("Masukan jumlah deposit anda : Rp. "))
        pengalaman = int(input("Masukan pengalaman anda dalam mengemudi (dalam tahun) : "))
        print("====="*14)
        print("\t====================BIODATA ANDA====================")
        print("====="*14)
        if usia < 21:
            usia_kurang = ("Anda di TOLAK!!!, Karena usia anda tidak mencukupi")
            print(f"Nama anda: {nama}")
            print(f"Usia anda: {usia} tahun")
            print(f"Status SIM anda: {sim}")
            print(f"Jumlah deposit anda: Rp. {deposit}")
            print(f"Pengalaman anda dalam mengemudi: {pengalaman} tahun")
            print(f"Status rental: {usia_kurang}")
        elif usia >= 21 and sim == "tidak":
            sim_tidak = ("Anda di TOLAK!!!, Karena anda tidak memiliki SIM")
            print(f"Nama anda: {nama}")
            print(f"Usia anda: {usia} tahun")
            print(f"Status SIM anda: {sim}")
            print(f"Jumlah deposit anda: Rp. {deposit}")
            print(f"Pengalaman anda dalam mengemudi: {pengalaman} tahun")
            print(f"Status rental: {sim_tidak}")
        elif usia >= 21 and sim == "ada" and deposit < 500000:
            deposit_kurang = ("Anda di TOLAK!!!, Karena deposit anda kurang dari Rp. 500.000")
            print(f"Nama anda: {nama}")
            print(f"Usia anda: {usia} tahun")
            print(f"Status SIM anda: {sim}")
            print(f"Jumlah deposit anda: Rp. {deposit}")
            print(f"Pengalaman anda dalam mengemudi: {pengalaman} tahun")
            print(f"Status rental: {deposit_kurang}")
        elif usia >= 21 and sim == "ada" and deposit >= 500000 and pengalaman < 4:
            pengalaman_kurang = ("Anda di SETUJUI!!!, Namun untuk mobil standar saja")
            print(f"Nama anda: {nama}")
            print(f"Usia anda: {usia} tahun")
            print(f"Status SIM anda: {sim}")
            print(f"Jumlah deposit anda: Rp. {deposit}")
            print(f"Pengalaman anda dalam mengemudi: {pengalaman} tahun")
            print(f"Status rental: {pengalaman_kurang}")
        else:
            pengalaman_cukup = ("Anda di SETUJUI!!!, Untuk semua jenis mobil")
            print(f"Nama anda: {nama}")
            print(f"Usia anda: {usia} tahun")
            print(f"Status SIM anda: {sim}")
            print(f"Jumlah deposit anda: Rp. {deposit}")
            print(f"Pengalaman anda dalam mengemudi: {pengalaman} tahun")
            print(f"Status rental: {pengalaman_cukup}")
            print("====="*14)
            print("====="*14)
            break
    elif username != nama or password != nim:
        perulangan += 1
        print("====="*14)
        print("Username atau password anda salah!")
        print(f"Anda memiliki kesempatan {max_perulangan - perulangan} kali lagi")
        coba_lagi = input("Apakah anda ingin mencoba lagi? (y/n):")
        print("====="*14)
        if perulangan == max_perulangan:
            print("====="*14)
            print("ANDA GAGAL LOGIN!!!")
            print("ANDA INI MAU MEMBOBOL DATA USER YA!!")
            print("====="*14)
        elif coba_lagi.lower() == "y":
            os.system ("cls")
        else:
            print("====="*14)
            print("TERIMA KASIH TELAH MENGUNJUNGI RENTAL MOBIL CABANG PATI CINTA DAMAI")
            print("====="*14)
            break
        
