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


# Inisialisasi data penting
data = data.load(f"{args.folderName}")
users = data[0]
candi = data[1]
bahan_bangunan = data[2]
print(users, candi, bahan_bangunan)

logged_in = False
logged_user = ""
jin = ["."]
idjin = 1
print("Selamat datang di program “Manajerial Candi”")
print("Silahkan masukkan username Anda")

# Array [Kode Jin, ID Jin, Nama Jin, Password, Jumlah Candi yg dibuat (khusus kode 2 atau kode 1 dikasi -1 aja)]
while True:
  masukan = input(">>> ")
  if masukan == "login" or masukan == "logout":
    hasil = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin)
    logged_in = hasil[0]
    logged_user = hasil[1]
  elif masukan == "summonjin":
    datajin = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin)
    jin = datajin[0]
    users = datajin[1]
    idjin = datajin[2]
    print(datajin)
  elif masukan == "hapusjin":
    jindancandi = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin)
    jin = jindancandi[1]
    candi = jindancandi[0]
  elif masukan == "ubahjin":
     jin = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin)
  elif masukan == "bangun":
     hasil = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin)
  elif masukan == "kumpul":
     hasil = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin)
  else:
    commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin)
