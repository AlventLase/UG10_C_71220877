daftar = str(input("Masukkan daftar pesanan: "))
print("Daftar pesanan [{}]".format(daftar))
a = str(input("Masukkan pesanan yang ingin ditambahkan: "))
if a in daftar:
    print("{} sudah berada dalam daftar pesanan.".format(a))
else:
    print("Hasil penambahan pada daftar pesanan: ")
    



