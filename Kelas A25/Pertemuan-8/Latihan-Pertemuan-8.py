# # # import math
# # # # from math import sqrt
# # # import math as m

# # # # # # # # num = int("42") # 42
# # # # # # # # name = str(123) # "123"
# # # # # # # # data = list("abc") # ['a', 'b', 'c']
# # # # # # # # print(data)
# # # # # # # # data = dict(a=1, b=2) # {'a': 1, 'b': 2}
# # # # # # # # print(data)
# # # # # # # # print(type(num)) # <class 'int'>

# # # # # # # a = divmod(10,3)
# # # # # # # print(a)#(hasil bagi,sisa bagi)

# # # # # # abs(-9) # 9
# # # # # # max([1, 3, 7]) # 7
# # # # # list1 = [1,5,100,6,7]
# # # # # print(max(list1))
# # # # # print(min(list1))
# # # # # # min([1, 3, 7]) # 1
# # # # # # round(3.14159,2) # 3.14
# # # # # # sum([1, 2, 3]) # 6

# # # # for i, v in enumerate(['a','b','c']):
# # # #     print(i, v) # 0 a , 1 b
    
# # # # a = [1,5,6,30,95,120,5,3,3]
# # # # print(sorted(a))

# # # # x = 42
# # # # def fungsi():
# # # #     x = 10
# # # #     y = 20
# # # #     z = 30
# # # #     print(globals()['x']) # mendapatkan isi dari variabel x (global)
# # # #     print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
# # # #     print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# # # # fungsi()

# # # print(int(m.sqrt(16)))
# # # print(m.factorial(4))

# # import random
# # # print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4

# # # pilih_acak = ["pisang", "rambutan", "manggis"]
# # # acak = "apcb"
# # # print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# # # print(random.choice(acak)) # memilih 1 karakter acak pada string
# # # # memasukkan satu persatu nilai dari kumpulan_angka
# # # # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# # kumpulan_angka = "1234567890"
# # hasil = ""
# # for i in range(4):
# #     hasil += random.choice(kumpulan_angka)
# # print(hasil)

# # acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# # random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang berubah
# # print(acak_kartu)

# from datetime import datetime
# print(datetime.now())




#library eksternal prettytable: https://pypi.org/project/prettytable/





import inquirer

pertanyaan = [
inquirer.List('size',
message="What size do you need?",
choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
),
]
# mendapatkan jawaban
answer = inquirer.prompt(pertanyaan)
print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
print(answer['size']) #
