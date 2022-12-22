#halaman 16 modul praktikum algoritma pemrograman
#create by RIDHO ARYA FIRMANSYAH_2270231027

#latihan konversi satuan temperature

#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah",celcius, "Celcius")
# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")
# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")
# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")