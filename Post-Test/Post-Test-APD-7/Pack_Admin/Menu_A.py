def menu_admin():
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

def pil_tanaman(tanaman):
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
        
def menu_pil5(stok_PV):
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