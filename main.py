# Program Utama

# File: main.py
import commands
import data
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('folderName', type=str, nargs='?')
    args = parser.parse_args()

    if not args.folderName:
        print("Tidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()


# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
data = data.load(f"{args.folderName}")
users = data[0]
candi = data[1]
bahan_bangunan = data[2]
logged_in = False
logged_user = ""
print(users)
print(candi)
print(bahan_bangunan)
print("Selamat datang di program “Manajerial Candi”")
print("Silahkan masukkan username Anda")

# Array [Kode Jin, ID Jin, Nama Jin, Password, Jumlah Candi yg dibuat (khusus kode 2 atau kode 1 dikasi -1 aja)]
jin = [[1, 1, "Asep", "Agus", -1, "."], [2, 2, "Ayam", "Unggas", 1, "."], [2, 3, "Jin", "Hal0", 10, "."], [2, 4, "Jon", "Alo", 7, "."], "."]
# dummy jin
while True:
  masukan = input(">>> ")
  if masukan == "login" or masukan == "logout":
    hasil = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user)
    logged_in = hasil[0]
    logged_user = hasil[1]
  else:
    commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user)
