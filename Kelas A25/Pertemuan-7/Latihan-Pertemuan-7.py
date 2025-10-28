# # # # # def salam():
# # # # #     print ('Halo, Ridho')
    
# # # # # def kali():
# # # # #     x = 5*5
# # # # #     print(x)
    
# # # # # kali()
# # # # # salam()

# # # # # def s(p,l):
# # # # #     a = p*l
# # # # #     return a
# # # # # print(s(10,60))

# # def segitiga(a,t):
# #     luas = 0.5*a*t
# #     return luas
# # c = int(input("alas = "))
# # b = int(input("tinggi = "))
# # print(segitiga(c,b))

# # # # Nama = "Hambali"
# # # # Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# # # # def info():
# # # #  Nama = "Informatika"
# # # #  Mata_Kuliah = "Logika Informatika"
# # # #  print("Prodi:", Nama)
# # # #  print("Mata Kuliah:", Mata_Kuliah)

# # # # # mengakses variabel global
# # # # print("Prodi:", Nama)
# # # # print("Mata Kuliah:", Mata_Kuliah)
# # # # # memanggil fungsi info
# # # # info()


# # # # def faktorial(n):
# # # #     if n == 1 or n == 0:
# # # #      return 1
# # # #     else:
# # # #      return n * faktorial(n - 1)

# # # # hasil = faktorial(5)
# # # # print(f"Hasil dari 5! adalah: {hasil}")

# # # film = []


# # # def show_data():
# # #     if len(film) <= 0:
# # #         print("Belum Ada data")
# # #     else:
# # #         print("ID | Judul Film")
# # #         for indeks in range(len(film)):
# # #             print(indeks + 1, "|", film[indeks])

# # # # Fungsi untuk menambah data
# # # def insert_data():
# # #     film_baru = input("Judul Film: ")
# # #     film.append(film_baru)
# # #     print("Film berhasil ditambahkan!")


# # # # Fungsi untuk mengedit data
# # # def edit_data():
# # #     show_data()
# # #     indeks = int(input("Inputkan ID film: "))
# # #     if indeks >= len(film) or indeks < 1:
# # #         print("ID salah")
# # #     else:
# # #         judul_baru = input("Judul baru: ")
# # #         film[indeks] = judul_baru
# # #         print("Film berhasil diupdate!")


# # # # Fungsi untuk menghapus data
# # # def delete_data():
# # #     show_data()
# # #     indeks = int(input("Inputkan ID film: "))
# # #     if indeks >= len(film) or indeks < 1:
# # #         print("ID salah")
# # #     else:
# # #         film.remove(film[indeks])
# # #         print("Film berhasil dihapus!")


# # # # fungsi untuk menampilkan menu
# # # def show_menu():
# # #     print ("\n")
# # #     print ("----------- MENU---------- ")
# # #     print ("[1] Show Data")
# # #     print ("[2] Insert Data")
# # #     print ("[3] Edit Data")
# # #     print ("[4] Delete Data")
# # #     print ("[5] Exit")
# # #     menu = input("PILIH MENU> ")
# # #     print ("\n")

# # #     if menu == "1":
# # #         show_data()
# # #     elif menu == "2":
# # #         insert_data()
# # #     elif menu == "3":
# # #         edit_data()
# # #     elif menu == "4":
# # #         delete_data()
# # #     elif menu == "5":
# # #         exit()
# # #     else:
# # #         print ("Salah pilih!")

# # # if __name__ == "__main__":
# # #         while (True):
# # #             show_menu()
            

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')    
    
# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')
# finally :
#     print('Blok Try Selesai')  
    
# try:
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as e:
#     print(e)

# try:
#     nama = input("nama : ")
#     if nama == "":
#         raise ValueError("nama tidak boleh kosong")
# except ValueError as a:
#     print(a)
    
try:
    pw = input("pw : ")
    if len(pw) < 8:
     raise ValueError("pw tak boleh kurang dari 8 digit")
except ValueError as a:
    print(a)
    
    
    

    
    