# # # # # # # # # menampilkan list
# # # # # # # # praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# # # # # # # # print(praktikum)

# # # # # # # # menampilkan list
# # # # # # # praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# # # # # # # # memanggil satu elemen
# # # # # # # print(praktikum[-1])
# # # # # # # # memanggil elemen di dalam list
# # # # # # # print(praktikum[4][1])

# # # # # # kosong = []
# # # # # # kosong.append("Dapupu")
# # # # # # kosong.insert(0, "Mahasiswa") #menambahkan di index tertentu
# # # # # # print(kosong)

# # # # # # list awal
# # # # # studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # # # # print(studyclub)
# # # # # # Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# # # # # studyclub[2] = "AI"
# # # # # print(studyclub)
# # # # # #menambahkan elemen baru di akhir list
# # # # # studyclub.append("Cloud Computing")
# # # # # print(studyclub)
# # # # # # Menghapus elemen "Network" dari list
# # # # # del studyclub[3]
# # # # # print(studyclub)
# # # # # # Menghapus elemen "Data Science" dari list
# # # # # studyclub.remove("Data Science")
# # # # # print(studyclub)

# # # # # # list awal
# # # # # matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# # # # # print(matakuliah)
# # # # # # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# # # # # ambil_matkul = matakuliah.pop(2)
# # # # # print(matakuliah)
# # # # # print(ambil_matkul)

# # # # # matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# # # # # 'Orsikom','Basis Data']
# # # # # # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# # # # # print(matakuliah[0:7:3])

# # # # Membuat Nested List
# # # kelas = [
# # # ["Ridho", "Lian", "Nabil"],
# # # ["Daffa", "Dante", "Santoso"],
# # # ["Pernanda", "Riyadi", "Ahnaf"],
# # # ]
# # # kelas.insert(1, ["Dapupu", "Dito", "Deden"])
# # # print(kelas)
# # # kelas[2][1] = "Danu"
# # # print(kelas)
# # # print(kelas[3][0])
# # # kelas[1].append("Dimas")
# # # print(kelas)
# # # for i in kelas:
# # #     for nama in i:
# # #         print(nama)

# # # # # # List
# # # # # a = [1, 2, 3]
# # # # # b = [4, 5, 6]
# # # # # # menggabungkan kedua list dengan operator (+)
# # # # # c = a + b
# # # # # print(c)

# # # # # List
# # # # a = ["teknik", "informatika", "universitas", "Mulawarman", "Fakultas", "Teknik"]
# # # # # mengulang isi list dengan operator (*) sebanyak 3 kali
# # # # c = a*3
# # # # print(c)
# # # # # for i in a :
# # # # #     print(i)
# # # # for index, i in enumerate(a):
# # # #     print(f'Index ke {index} adalah {i}')

# # # menampilkan tuple
# # anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# # # memanggil satu elemen
# # print(anggota[1])
# # print(anggota[-1])
# # # memanggil elemen di dalam nested tuple
# # print(anggota[5][0])
# # anggota2 = list(anggota)
# # anggota2.insert(1, "Dapupu")
# # print(anggota2)
# # anggota2[4] = 4.00 
# # print(anggota2)

# # studi kasus
# keranjang_campur = ["Apel", "Brokoli", "jamur", "Daging", "Wortel", "Susu", "Pisang", "Bayam"]
# kernjang_buah = ["Apel", "Pisang", "Jeruk", "Mangga", "Semangka"]
# buah = []
# for i in keranjang_campur:
#     if i in kernjang_buah:
#         buah.append(i)
#         print(f"{i} dimasukkan ke dalam list buah")
# print(buah)