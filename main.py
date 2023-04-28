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

logged_in = False
logged_user = ""
jin = ["."]
idjin = 1
idcandi = 1
print("Selamat datang di program “Manajerial Candi”")
print("Silahkan masukkan username Anda")
# Array [Kode Jin, ID Jin, Nama Jin, Password, Jumlah Candi yg dibuat (khusus kode 2 atau kode 1 dikasi -1 aja)]
while True:
  masukan = input(">>> ")
  if masukan == "login" or masukan == "logout":
    hasil = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
    logged_in = hasil[0]
    logged_user = hasil[1]
  elif masukan == "summonjin":
    datajin = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
    jin = datajin[0]
    users = datajin[1]
    idjin = datajin[2]
  elif masukan == "hapusjin":
    jindancandi = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
    jin = jindancandi[1]
    candi = jindancandi[0]
    users = jindancandi[2]
  elif masukan == "ubahjin":
     jin = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
  elif masukan == "bangun":
     hasil = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
     bahan_bangunan[0][2] = hasil[0]
     bahan_bangunan[1][2] = hasil[1]
     bahan_bangunan[2][2] = hasil[2]
     candi = hasil[3]
     idcandi = hasil[4]
  elif masukan == "kumpul" or masukan == "batchkumpul":
     hasil = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
     bahan_bangunan[0][2] = hasil[0]
     bahan_bangunan[1][2] = hasil[1]
     bahan_bangunan[2][2] = hasil[2]
  elif masukan == "hancurkancandi":
     candi = commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
  else:
    commands.run(masukan, users, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi)
