import bonus
# Data Penting
def length(a): # fungsi len
    sum = 0 
    while a[sum] != ".": # menggunakan titik untuk marking
        sum+=1
    return sum

def konso(a, b): # fungsi append array & number
    len = length(a)+2
    li = [0 for i in range (len)]
    for i in range (length(a)):
        li[i] = a[i]
    li[len-2] = b
    li[len-1] = "."
    return li

def bubble_sort(arr): # fungsi sorting array
    n = length(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_matrix(mat, x): # fungsi sorting matriks dengan input indeks array
    n = length(mat)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if mat[j][x] > mat[j+1][x] :
                mat[j], mat[j+1] = mat[j+1], mat[j]

def array_slicing(start, end, array): # fungsi slicing
    sliced = ""
    for i in range(start, end):
        sliced = konso(sliced, array[i])
    return sliced

def join(array): # gabungkan array ke text
    string = ""
    for i in range (length(array)):
       string += array[i]
    return string

def csvtomatrix(source):
        # CSV TO MATRIX
        # r : read, r+ : read & write
        file = open(f"{source}", "r+")
        file = file.read()
        
        matrix = ["."]
        array = ["."]
        word = ""
        start = False
        for i in range (len(file)):
            if start == False:
                if file[i]=="\n":
                    start = True
            else:
                if file[i] == "\n":
                    array = konso (array, word)
                    word = ""
                    matrix = konso(matrix, array)
                    array = ["."]
                elif file[i] == ";":
                    array = konso(array, word)
                    word = ""
                else:
                    word+=file[i]
        return matrix

def removelmt(arr, removed):
    len = length(arr)
    li = ["."]
    for i in range (len):
        if i != removed:
            li = konso(li, arr[i])
    return li

def login(users, logged_in, logged_user): #F01
    # tampilkan prompt login
    if logged_in:
        username = ""
        for i in range (length(users)):
            if users[i][2] == users:
                username = users[i][0]
        print("Login gagal!")
        print("Anda telah login dengan username", username, end=", ")
        print("silahkan lakukan \"logout\" sebelum melakukan login kembali.")
    else:
        username = input("Username: ")
        password = input("Password: ")
        # periksa apakah pengguna masih login saat mencoba login kembali
        found = False
        # periksa apakah username dan password cocok\
        for i in range (length(users)):
            if users[i][0] == username:
                found = True
                if users[i][1] == password:
                    logged_in = True
                    logged_user = users[i][2]
                    print(f"\nSelamat datang, {username}!")
                    print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                else:
                    print("\nPassword salah!")
        if found == False:
            print("\nUsername tidak terdaftar!")
    return logged_in, logged_user
        
        # periksa command yang dimasukkan

def logout(logged_in, logged_user): #F02
    logged_in = False
    logged_user = ""
    print("Logout berhasil!")
    return logged_in, logged_user

def summonjin(logged_user, jin, user): #F03
    if logged_user == "bandung_bondowoso":
        if length(jin) != 100:
            print("Jenis jin yang dapat dipanggil:")
            print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print(" (2) Pembangun - Bertugas membangun candi\n")
            call = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            if call == 1 or call == 2:
                if call == 1:
                    print("\nMemilih jin \"Pengumpul\".\n")
                if call == 2:
                    print("\nMemilih jin \"Pembangun\".\n")
                usernamesama = True
                while usernamesama == True:
                    usernameJin = str(input("Masukkan username jin: "))
                    usernamesama = False
                    for i in range (length(jin)):
                        if jin[i][2] == usernameJin:
                            print(f"\nUsername \"{usernameJin}\" sudah diambil!")
                            usernamesama = True
                if usernamesama == False:
                    passwordnya = False
                    while passwordnya == False:
                        password = str(input("Masukkan password jin: "))
                        if len(password)<5 or len(password)>25:
                            print("\nPassword panjangnya harus 5-25 karakter!\n")
                        else:
                            passwordnya = True
                    print("\nMengumpulkan sesajen...")
                    print("Menyerahkan sesajen...")
                    print("Membacakan mantra...")
                    
                    if call == 1:
                        jin = konso(jin, [call, length(jin)+1, usernameJin, password, -1])
                    else:
                        jin = konso(jin, [call, length(jin)+1, usernameJin, password, 0])
                    user = konso(user, [usernameJin, password, length(jin)+1])
                    print(f"Jin {usernameJin} berhasil dipanggil!")
            else:
                print(f"Tidak ada jenis jin bernomor \"{call}\"!")
        else:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Summon jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")
    return jin, user

def hapusjin(jin, candi, logged_user, user): #F04
    if logged_user == "bandung_bondowoso":
        jin = konso(jin, [0,0,""])
        jinDihapus = str(input("Masukkan username jin : "))
        hapus = False
        for i in range (length(jin)-1):
            if jin[i][2] == jinDihapus:
                hapus = True
                check = str(input(f"Apakah anda yakin ingin menghapus jin dengan username {jinDihapus} (Y/N)? "))
                if check == "Y":
                    jin = removelmt(jin, i)
                    print("\nJin telah berhasil dihapus dari alam gaib.")
                    for j in range (length(candi)):
                        if candi[j][1] == str(i+1):
                            candi = removelmt(candi, j)
                    for k in range (length(user)):
                        if user[k][2] == str(i+1):
                            user = removelmt(user, k)
                elif check == "N":
                    break
        if hapus == False:
            print("\nTidak ada jin dengan username tersebut.")
        jin = removelmt(jin, length(jin)-1)
    else:
        print("Hapus jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")
    return candi, jin

def ubahjin(jin, logged_user): #F05
    if logged_user == "bandung_bondowoso":
        ubah = str(input("Masukkan username jin : "))
        ubah = False
        for i in range (length(jin)):
            ubah = True
            if jin[i][2] == ubah:
                if jin[i][0] == 1:
                    a = "Pengumpul"
                    b = "Pembangun"
                else:
                    a = "Pembangun"
                    b = "Pengumpul"
                check = str(input(f"Jin ini bertipe \"{a}\". Yakin ingin mengubah ke tipe \"{b}\" (Y/N)? "))
                if check == "Y":
                    if a == "Pengumpul":
                        jin[i][0] = 2
                    else:
                        jin[i][0] = 1
                elif check == "N":
                    break
            if ubah == False:
                print("\nTidak ada jin dengan username tersebut.")
    else:
        print("Ubah jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")

def bangun(candi, bahan_bangunan, logged_user):
    if logged_user == "jin_pembangun":
        pasir = bonus.random()
        batu = bonus.random()
        air = bonus.random()
        if pasir<=int(bahan_bangunan[0][2]) and batu<=int(bahan_bangunan[1][2]) and air<=int(bahan_bangunan[2][2]):
            candi = konso(candi, [length(candi), logged_user, pasir, batu, air])

#F09 - Ambil Laporan Jin
def laporanjin(user, jin, bahan_bangunan):
  if user == "bandung_bondowoso":
    print()
    print("> Total Jin:", length(jin))
    sum = 0
    for i in range (length(jin)):
        if jin[i][0] == 1:
           sum+=1
    print("> Total Jin Pengumpul:", sum)
    print("> Total Jin Pembangun:", length(jin)-sum)
    bubble_sort_matrix(jin, 4)
    aturjin = ["."]
    for i in range (length(jin)):
       if jin[i][4] != -1:
          aturjin = konso(aturjin, jin[i])
    if length(aturjin)-1>0:
        print("> Jin Terajin:", aturjin[length(aturjin)-1][2])
        print("> Jin Termalas:", aturjin[0][2])
    else:
        print("> Jin Terajin:")
        print("> Jin Termalas:")
    print("> Jumlah Pasir:", bahan_bangunan[0][2])
    print("> Jumlah Air:", bahan_bangunan[1][2])
    print("> Jumlah Batu:", bahan_bangunan[2][2])
  else:
    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

#F10 - Ambil Laporan Candi
def laporancandi(user, candi):
  if user == "bandung_bondowoso":
    print()
    print("> Total Candi:", length(candi))
    pasir = 0
    batu = 0
    air = 0
    for i in range (length(candi)):
       pasir+=int(candi[i][2])
       batu+=int(candi[i][3])
       air+=int(candi[i][4])
    print("> Total Pasir yang digunakan:", pasir)
    print("> Total Batu yang digunakan:", batu)
    print("> Total Air yang digunakan:", air)
    if length(candi)>0:
        hargacandi = [0 for i in range (length(candi))]
        for i in range (length(candi)):
           hargacandi[i]= 10000*pasir + 15000*batu + 7500*air
        min = 0 
        max = 0
        for i in range (length(candi)):
            if hargacandi[i]<hargacandi[min]:
               min = i
            if hargacandi[i]>hargacandi[max]:
               max = i
        # Ubah format harga candi
        def formatrupiah(uang):
            uang = str(uang)
            if length(uang)==5:
               return join(array_slicing(0, 2, uang)) + "." + join(array_slicing(2, 5, uang))
            else:
               return join(array_slicing(0,3,uang)) + "." + join(array_slicing(3,6,uang))
        print("> ID Candi Termahal:", candi[max][0], "(Rp "+formatrupiah(hargacandi[max])+")")
        print("> ID Candi Termurah:", candi[min][0], "(Rp "+formatrupiah(hargacandi[min])+")")
    else:
        print("> ID Candi Termahal: -")
        print("> ID Candi Termurah: -")
  else:
    print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")

# F11 Hancurkan Candi

# F12 - Ayam berkokok
def ayamberkokok() :
    print ("Kukuruyuk.. Kukuruyuk..")
    jumlah_candi = int(input("Jumlah Candi : "))
    if jumlah_candi <= 100 :
        print ("*Bandung Bondowoso angry noise*")
        print ("Roro Jonggrang dikutuk menjadi candi")
        # Keluar Program
    else : #jumlah candi > 100
        print ("yah, Bandung Bowoso memenangkan permainan!")
        # Keluar Program

# F13 - Load
import os
def load(source):
    if os.path.exists(source):
        users = csvtomatrix(f"{source}/user.csv")
        candi = csvtomatrix(f"{source}/candi.csv")
        bahan_bangunan = csvtomatrix(f"{source}/bahan_bangunan.csv")
        return users, candi, bahan_bangunan
    else:
        print(f"Folder \"{source}\" tidak ditemukan.")
        exit()

#F15
def help(logged_in, logged_user):
    print("=========== HELP ===========")
    if logged_in :
        if logged_user == "bandung_bondowoso" :
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. summonjin")
            print("   Untuk memanggil jin")
            print("3. hapusjin")
            print("   Untuk menghapus jin")
            print("4. ubahjin")
            print("   Untuk mengubah tipe jin")
            print("5. batchbangun")
            print("   Untuk membangun candi dengan semua Jin Pembangun")
            print("6. batchkumpul")
            print("   Untuk mengumpulkan bahan bangunan dengan semua Jin Pengumpul")
            print("7. laporanjin")
            print("   Untuk mengeluarkan laporan mengenai jin dan kinerja jin")
            print("8. laporancandi")
            print("   Untuk mengeluarkan laporan mengenai progres pembangunan candi")
            print("9. save")
            print("   Untuk menyimpan data ke dalam suatu file")
            print("10. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
        elif logged_user == "roro_jonggrang" :
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. hancurkancandi")
            print("   Untuk menghancurkan candi")
            print("3. ayamberkokok")
            print("   Untuk memeriksa jumlah candi yang telah dibangun")
            print("4. save")
            print("   Untuk menyimpan data ke dalam suatu file")
            print("5. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
        elif logged_user == "jin_pembangun":
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun")
            print("   Untuk membangun candi")
            print("3. save")
            print("   Untuk menyimpan data ke dalam suatu file")
            print("4. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
        elif logged_user == "jin_pengumpul":
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul")
            print("   Untuk mengumpulkan resource candi")
            print("3. save")
            print("   Untuk menyimpan data ke dalam suatu file")
            print("4. exit")
            print("   Untuk keluar dari program dan kembali ke terminal")
    else:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")