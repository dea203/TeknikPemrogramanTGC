def hitung_total(harga, jumlah, diskon = 0):
    total_diskon = harga * jumlah * diskon / 100
    total = harga * jumlah - total_diskon
    return total 

harga = int(input("masukkan harga barang: "))
jumlah = int(input("masukkan jumlah barang: "))
diskon = int(input("masukkan diskon % : "))
total = hitung_total(harga, jumlah)

print (f"total keseluruhan adalah {total}")