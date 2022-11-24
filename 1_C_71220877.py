print("===== Pilih Menu =====")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
angpertama = int(input("Masukkan angka pertama: "))
angkedua = int(input("Masukkan angka kedua: "))
menu = input("Pilihan Anda: ")
if menu == ("1"):
    print(angpertama + angkedua)
elif menu == ("2"):
    print(angpertama - angkedua)
elif menu == ("3"):
    print(angpertama * angkedua)
else:
    print(angpertama / angkedua)
