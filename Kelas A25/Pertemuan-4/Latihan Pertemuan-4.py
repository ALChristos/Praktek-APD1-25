# # # # # # # # # # ulangi = 10
# # # # # # # # # # for i in range (ulangi):
# # # # # # # # # #  print(f'Perulangan ke {i}')

# # # # # # # # # simpan = [1, 'Dapupu', 4.00, True]
# # # # # # # # # for i in simpan:
# # # # # # # # #     print(i)

# # # # for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
# # # #     for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
# # # #         print(f'{i} x {j} = {i * j}')
# # # #         print('')

# # # # # # # jawab = 'ya'
# # # # # # # hitung = 0
# # # # # # # while(jawab == 'ya'):
# # # # # # #     hitung += 1
# # # # # # #     jawab = input("Ulang lagi? ")
# # # # # # #     print(f"Total perulangan: {hitung}")

# # # # # # cuaca='hujan'
# # # # # # while cuaca == 'hujan' or cuaca == 'Hujan':
# # # # # #     print("jangan keluar rumah")
# # # # # #     cuaca = input("Masih hujan? ")
# # # # # # print("Sudah tidak hujan, silakan keluar rumah")

# # # # angka = 10
# # # # while angka >= 1:
# # # #     print(angka)
# # # #     angka -= 2
# # # # print("Wakwaw...!!!")

# # # # angka = [2, 5, 8, 12, 15, 7, 20]
# # # # print("Mencari angka pertama yang lebih besar dari 10...")
# # # # for a in angka:
# # # #     print(f"Sekarang memeriksa angka: {a}")
# # # #     if a > 10:
# # # #         print(f"Angka {a} lebih besar dari 10, Perulangan berhenti.")
# # # #         break
# # # # print("Program selesai.")

# # # for i in range(1, 101):
# # #     if i % 2 != 0:
# # #         continue
# # #     print(f"Angka genap ditemukan: {i}")
# # # print("\nProgram selesai.")

# # # for i in range(1, 101):
# # #     if i % 2 == 0:
# # #         continue
# # #     print(f"Angka ganjil ditemukan: {i}")
# # # print("\nProgram selesai.")

# # # kuadart = [i**2 for i in range(1, 11)]
# # # print(kuadart)
# # # genap = [i for i in range(1, 101) if i % 2 == 0]
# # # print(genap)
# # # ganjil = [i for i in range(1, 101) if i % 2 != 0]
# # # print(ganjil)

# # # Studi kasus Fani dan Fatih
# # # Studi kasus segitiga
# # tinggi = int(input("Masukkan tinggi segitiga: "))
# # print("\nSegitiga Sama Kaki:")
# # for i in range(1, tinggi + 1):
# #     print(' ' * (tinggi - i), end='')
# #     print('*' * (2 * i - 1))
# # print("\nSegitiga Sama Kaki Terbalik:")
# # for i in range(tinggi, 0, -1):
# #     print(' ' * (tinggi - i), end='')
# #     print('*' * (2 * i - 1))

# # Input tinggi segitiga
# tinggi = int(input("Masukkan tinggi segitiga: "))
# print("Segitiga Sama Kaki:")
# for i in range(tinggi):
#     print(' ' * (tinggi - i - 1) + '*' * (2 * i + 1))

