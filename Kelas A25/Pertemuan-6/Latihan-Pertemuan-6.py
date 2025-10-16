# # # # # # # buah = {"apel", "jeruk", "mangga", "apel"}
# # # # # # # buah = (["apel", "jeruk", "mangga", "apel"])
# # # # # # # for i in buah:
# # # # # # #     print(i, end='')

# # # # # # angka_ganjil = {1, 3, 5, 7, 9}
# # # # # # for angka in angka_ganjil:
# # # # # #     print (angka)

# # # # # Daftar_buku = {
# # # # # "Buku1" : "Bumi Manusia",
# # # # # "Buku2" : "Laut Bercerita"
# # # # # }
# # # # # print(Daftar_buku)
# # # # # print(Daftar_buku["Buku1"])

# # # # Biodata = {
# # # #     "Nama" : "Ananda Daffa Harahap",
# # # #     "NIM" : 2409106050,
# # # #     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# # # #     "Mahasiswa_Aktif" : True,
# # # #     "Social Media" : {
# # # #         "Instagram" : "daffahrhap" 
# # # #     }
# # # # }
# # # # # for i in Biodata.values():
# # # # #     print(i)

# # # # # for a, b in Biodata.items():
# # # # #     print(f"{a} : {b}")
    
# # # # print(f"nama saya adalah {Biodata["Nama"]}")
# # # # print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# # # # print(f"nama saya adalah {Biodata.get("Nama")}\n")

# # # # print(Biodata.get("Nama"))
# # # # print(Biodata.get("Alamat"))
# # # # print(Biodata.get("Alamat", "Key tersebut tidak ada"))

# # # # Nilai = {
# # # # "Matematika": 80,
# # # # "B. Indonesia": 90,
# # # # "B. Inggris": 81,
# # # # "Kimia": 78,
# # # # "Fisika": 80
# # # # }
# # # # # for i in Nilai:
# # # # #     print(i)
# # # # #     print("") # pemisah
# # # # # # Menggunakan items()
# # # # # for i, j in Nilai.items():
# # # # #     print(f"Nilai {i} anda adalah {j}")

# # # # Nilai.update({"Sejarah":70})
# # # # print(Nilai)

# # # Film = {
# # # "Avenger Endgame" : "Action",
# # # "Sherlock Holmes" : "Mystery",
# # # "The Conjuring" : "Horror"
# # # }

# # # Film['The Conjuring'] = "Comedy"
# # # Film.update({"Jumanji":"Action"})
# # # print(Film)

# # Musik = {
# #     "The Chainsmoker": ["All we Know", "The Paris"],
# #     "Alan Walker": ["Alone", "Lily"],
# #     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
# #     'Paramore' : ["Misery Business", "Ain't It Fun", 
# #                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# # }

# # print(Musik['The Chainsmoker'][0])
# # print(Musik['Neffex'][1][0])
# # print(Musik['Paramore'][2][1][0])

# # angka = set()
# # a= {10,11,12}
# # b= {11,12,15}
# # c= a | b
# # print(c)
# # c= a or b
# # print(c)
# # c= a & b
# # print(c)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# print(Nilai)
