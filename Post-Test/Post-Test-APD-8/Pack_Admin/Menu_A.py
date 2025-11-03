from prettytable import PrettyTable
import inquirer

def menu_admin():
    print("="*58)
    print("\t============Menu Utama==============")
    print("="*58)
    menu = [
        inquirer.List("menuA",
                      message = "Pilihlah Menu Yang Tersedia",
                      choices = ["1. Lihat Data Tanaman",
                                 "2. Tambah Tanaman",
                                 "3. Update Data Tanaman",
                                 "4. Hapus Data Tanaman",
                                 "5. Lihat dan Atur Stok/Pemberian Pupuk, Stok/Pemberian Vitamin, dan Pemberian Air",
                                 "6. Lihat Laporan Laporan Masalah",
                                 "7. Kembali ke Menu Login"])
    ]
    jawab = inquirer.prompt(menu)
    return jawab

def pil_tanaman(tanaman):
    tabel = PrettyTable()
    tabel.field_names = ["No"] + list(tanaman[0].keys())
    for i,o in enumerate(tanaman, start = 1):
        tabel.add_row([i] + list(o.values()))
    print(tabel)
        
def menu_pil5(stok_PV):
    print("="*58)
    print("===Stok/Pemberian Pupuk, Stok/Pemberian Vitamin, dan Pemberian Air di Samarendah Garden===")
    print("="*58)
    tabel = PrettyTable()
    tabel.field_names = ["No"] + list(stok_PV[0].keys())
    for i,o in enumerate(stok_PV, start = 1):
        tabel.add_row([i] + list(o.values()))
    print(tabel)
    print("="*58)   
    menu = [
        inquirer.List("menu5",
                      message = "Pilihlah Menu Yang Tersedia Dipilihan 5",
                      choices = ["1. Tambah Stok Pupuk",
                                 "2. Tambah Stok Vitamin",
                                 "3. Beri Pupuk dan Vitamin ke Tanaman",
                                 "4. Beri Air ke Tanaman",
                                 "5. Kembali ke Menu Utama"])
    ] 
    jawab = inquirer.prompt(menu)
    return jawab

    