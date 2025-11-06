import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

# plt.figure(figsize=(12, 6)) #Horizontal, Vertikal
# plt.xlabel('kasih nama Sumbu X') #Sumbu X
# plt.ylabel('kasih nama Sumbu Y') #Sumbu Y
# plt.title("Ini judul loh") 

#GRAFIK GARIS
# x = [1, 2, 3, 4, 5] 
# y = [10, 35, 20, 70, 60]
# plt.figure(figsize=(8, 4)) 
# # plt.plot() 
# plt.plot(x, y) 
# # Detail element 
# plt.title("Contoh Grafik") 
# plt.xlabel("Sumbu X") 
# plt.ylabel("Sumbu Y") 
# plt.grid(True) 
# plt.show()



#GRAFIK GARIS
# x = [1, 2, 3, 4, 5] 
# y = [10, 35, 20, 70, 60] 
# y2 = [12, 43, 56, 23, 67] 
# plt.figure(figsize=(8, 4)) 
# # plt.plot() untuk masing-masing garis 
# plt.plot(x, y, marker="o", color="blue", label="Matematika") 
# plt.plot(x, y2, color="red", marker="h", linestyle="--", label="Fisika") 
# # Detail elemen untuk memambahkan teks 
# plt.title("Contoh Grafik") 
# plt.xlabel("Sumbu X") 
# plt.ylabel("Sumbu Y") 
# plt.grid(True) 
# # Nambahin keterangan, tapi jangan lupa tambahkan label 
# plt.legend() 
# plt.show() 
# plt.savefig("Real Penggunaan") #Menyimpan Gambar 



#GRAFIK BAR
# kategori = ['Python', 'Assembly', 'Java', 'C++'] 
# jumlah_pengguna = [100, 10, 50, 70] 
# plt.figure(figsize=(8, 5)) 
# # plt.bar() untuk menampilkan bar ke atas 
# plt.bar(kategori, jumlah_pengguna) 
# plt.xlabel("Nama Bahasa Pemrograman") 
# plt.ylabel("Banyak Pengguna") 
# plt.title("Perbandingan popularitas Bahasa Pemrograman") 
# # axis = y --- untuk mengubur garis vertikal; 
# # alpha --- untuk mengatur opacity garis 
# plt.grid(axis="y", alpha=0.5, linestyle="--") 
# plt.show()



views = [320, 450, 400, 390, 410, 470, 500, 490, 480, 510, 
530, 600, 620, 590, 550, 570, 610, 640, 700, 5000, 1000, 2000, 800, 
700, 750] 
plt.figure(figsize=(7, 4)) 
plt.boxplot(views, vert=False) 
plt.xlabel('Number of Views') 
plt.ylabel('Instagram') 
plt.ylabel('Number of Costumers') 
plt.grid(axis='y', alpha=0.5) 
views_series = pd.Series(views) 
views_clean = views_series[views_series < 1000] 
plt.show()