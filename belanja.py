harga = int(input("masukkan harga barang: "))
jumlah = int(input("masukkan jumlah barang: "))
diskon = int(input("masukkan diskon % : "))
total_diskon = harga * jumlah * diskon / 100
total = harga * jumlah - total_diskon

print (f"total keseluruhan adalah {total}")