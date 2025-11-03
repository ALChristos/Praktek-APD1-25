import inquirer

def menu_member():
    print("="*58)
    print("\t============Menu Utama==============")
    print("="*58)
    menu = [
        inquirer.List("menuM",
                      message = "Pilihlah Menu Yang Tersedia",
                      choices = ["1. Lihat Data Tanaman",
                                 "2. Lapor Masalah pada Tanaman",
                                 "3. Lihat Hadiah dari Admin",
                                 "4. Kembali ke Menu Login"])
    ]
    jawab = inquirer.prompt(menu)
    return jawab