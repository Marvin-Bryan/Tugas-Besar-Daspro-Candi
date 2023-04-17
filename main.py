# Program Utama

# File: main.py
import commands
import data

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

users = data.load("files/user.csv")
candi = data.load("files/candi.csv")
bahan_bangunan = data.load("files/bahan_bangunan.csv")

print(users, candi, bahan_bangunan)
user = "bandung_bondowoso" # dummy user, kalo mo coba yg lain masukin aja langsung
# Array [Kode Jin, ID Jin, Nama Jin, Password, Jumlah Candi yg dibuat (khusus kode 2 atau kode 1 dikasi -1 aja)]
jin = [[1, 1, "Asep", "Agus", -1], [2, 2, "Ayam", "Unggas", 1], [2, 3, "Jin", "Hal0", 10], [2, 4, "Jon", "Alo", 7]]
# dummy jin
while True:
  masukan = input(">>> ")
  commands.run(masukan, user, candi, jin, bahan_bangunan)
