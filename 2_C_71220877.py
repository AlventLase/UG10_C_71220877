bulan = int(input("Masukkan bulan (1-12): "))
ganjil = 1 or 3 or 5 or 7 or 8 or 10 or 12
feb = 2
genap = 4 or 6 or 9 or 11
ganj = 31
febr = 28
gena = 30

if bulan == feb:
    print("Jumlah hari",febr)
elif bulan == genap:
    print("Jumlah Hari",gena)
else:
    print("Jumlah Hari",ganj)
