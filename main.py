import konversi
import os 

os.system("cls")
# os.system("clear")
print("konversi suhu")
print("1.celcius ke fahrenheit")
print("2.fahrenheit ke celcius")

pilih = int(input("pilih: "))
if (pilih == 1):
    celcius = float(input("masukkan suhu celcius: "))
    suhu = konversi.c_to_f(celcius)
    print(f"suhu dalam fahrenheit {suhu} ")

elif (pilih == 2):
    fahrenheit = float(input("masukkkan suhu fahrenheit: "))
    suhu = konversi.f_to_c(fahrenheit)
    print(f"suhu dalam celcius {suhu} ")