# # # # # # # angka=10
# # # # # # # if angka > 5:
# # # # # # #     print("lebih besar dari 5")


# # # # # # nilai = 80
# # # # # # if nilai >= 75:
# # # # # #     print("lulus")
# # # # # # else:
# # # # # #     print("tidak lulus")

# # # # # # input nilai
# # # # # umur = int(input("Masukkan umur Anda: "))
# # # # # # misalnya, umur = 16
# # # # # # Percabangan
# # # # # if umur <= 13:
# # # # #     kategori = "Anak-anak"
# # # # # elif umur <= 18:
# # # # #     kategori = "Remaja"
# # # # # elif umur <= 40:
# # # # #     kategori = "Dewasa"
# # # # # else:
# # # # #     kategori = "Tua"
# # # # # # Menampilkan umur dan kategori
# # # # # print("Umur:", umur, "Kategori:", kategori)


# # # # nilai = int(input("Masukkan nilai Anda: "))
# # # # if nilai >= 90:
# # # #     dapat = "A"
# # # # elif nilai >= 80:
# # # #     dapat = "B"
# # # # elif nilai >= 70:
# # # #     dapat = "C"
# # # # elif nilai >= 60:
# # # #     dapat = "D"
# # # # else:  
# # # #     dapat = "E"


# # # # nilai = 70
# # # # if nilai = 60:
# # # # status = "Lulus"
# # # # else:
# # # # status = "Tidak Lulus"
# # # # print(status)
# # # # # output
# # # # Lulus


# # # Menggunakan Ternary Operator
# # nilai = 50
# # status = "Lulus" if nilai == 70 status = "remed" elif nilai == 50 else "Tidak Lulus"
# # print(status)


# # # Wahana rollercoaster tornado dufan
# # tinggi_badan= int(input("Masukkan tinggi badan (cm): "))
# # if tinggi_badan >= 145:
# #     print("Boleh naik wahana rollercoaster tornado dufan")
# # else:
# #     print("Tidak boleh naik wahana rollercoaster tornado dufan")


# # # Toko pakaian grand opening
# # harga_pakaian= int(input("Masukkan harga pakaian: "))
# # if harga_pakaian > 100000:
# #     diskon= harga_pakaian * 0.20
# #     total_bayar= harga_pakaian - diskon
# #     print(f"Total bayar setelah diskon 20% adalah:{total_bayar}")
# # elif harga_pakaian > 50000:
# #     diskon= harga_pakaian * 0.10
# #     total_bayar= harga_pakaian - diskon
# #     print(f"Total bayar setelah diskon 10% adalah:{total_bayar}")
# # else:
# #     print(f"Total bayar adalah:{harga_pakaian}")


# # # Tenary operator
# # harga_pakaian= int(input("Masukkan harga pakaian: "))
# # total_bayar= harga_pakaian - (harga_pakaian * 0.20) if harga_pakaian > 100000 else harga_pakaian - (harga_pakaian * 0.10) if harga_pakaian > 50000 else harga_pakaian
# # print(f"Total bayar adalah:{total_bayar}")



# nilai = int(input("Masukan Nilai: "))
# kelas = input("Masukan kelas: ")

# if nilai > 80 and (kelas == "A" or kelas == "a"):
#     print("IPK 4")
# elif nilai > 80 and (kelas == "B" or kelas == "b"):
#     print("IPK 3")
# else:
#      print("IPK 2")