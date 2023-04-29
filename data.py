import random
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
        if word != "":
            array = konso(array, word)
            matrix = konso(matrix, array)
        return matrix

def removelmt(arr, removed):
    len = length(arr)
    li = ["."]
    for i in range (len):
        if i != removed:
            li = konso(li, arr[i])
    return li

def minimal_nol(angka):
    if angka<0:
        return 0
    else:
        return angka
#----------------------------------------------------------------F01 - LOGIN -------------------------------------------------------------------------------
def login(users, logged_in, logged_user): 
    # tampilkan prompt login
    if logged_in:
        username = ""
        for i in range (length(users)):
            if users[i][2] == logged_user:
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
#----------------------------------------------------------------F02 - LOGOUT -------------------------------------------------------------------------------
def logout(logged_in, logged_user): 
    if logged_in == True:
        logged_in = False
        logged_user = ""
        print("Logout berhasil!")
    else:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return logged_in, logged_user
#----------------------------------------------------------------F03 - Summon Jin -------------------------------------------------------------------------------
def summonjin(logged_user, jin, user, idjin): 
    if logged_user == "bandung_bondowoso":
        if length(jin) != 100:
            print("Jenis jin yang dapat dipanggil:")
            print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print(" (2) Pembangun - Bertugas membangun candi\n")
            call = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            while call != 1 and call != 2:
                print(f"\nTidak ada jenis jin bernomor \"{call}\"!\n")
                call = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
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
                print("Membacakan mantra...\n")
                
                if call == 1:
                    jin = konso(jin, [call, idjin, usernameJin, password, -1, "."])
                else:
                    jin = konso(jin, [call, idjin, usernameJin, password, 0, "."])

                user = konso(user, [usernameJin, password, str(idjin), "."])

                print(f"Jin {usernameJin} berhasil dipanggil!")
                idjin+=1
        else:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Summon jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")
    return jin, user, idjin
#----------------------------------------------------------------F04 - Hilangkan Jin --------------------------------------------------------------------------
def hapusjin(jin, candi, logged_user, user):
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
                        if candi[j][1] == str(jin[i][1]):
                            candi = removelmt(candi, j)
                    for k in range (length(user)):
                        if user[k][2] == str(jin[i][1]):
                            user = removelmt(user, k)
                elif check == "N":
                    break
        if hapus == False:
            print("\nTidak ada jin dengan username tersebut.")
        jin = removelmt(jin, length(jin)-1)
    else:
        print("Hapus jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")
    return candi, jin, user
#----------------------------------------------------------------F05 - Ubah Tipe Jin -------------------------------------------------------------------------
def ubahjin(jin, logged_user): 
    if logged_user == "bandung_bondowoso":
        ubah = str(input("Masukkan username jin : "))
        ubahjin = False
        for i in range (length(jin)):
            if jin[i][2] == ubah:
                ubahjin = True
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
                    print("\nJin telah berhasil diubah.")
                elif check == "N":
                    break
        if ubahjin == False:
            print("\nTidak ada jin dengan username tersebut.")
    else:
        print("Ubah jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")
    return jin
#----------------------------------------------------------------F06 - Jin Pembangun -------------------------------------------------------------------------------
def bangun(candi, bahan_bangunan, logged_user, jin, idcandi):
    a = bahan_bangunan[0][2]
    b = bahan_bangunan[1][2]
    c = bahan_bangunan[2][2]
    if logged_user!="bandung_bondowoso" and logged_user!="roro_jonggrang":
        logged_user = int(logged_user)
        bangun = False
        for i in range (length(jin)):
            if jin[i][1]==logged_user:
                if jin[i][0] == 2:
                    bangun = True
                    pasir = random.randint(1,5)
                    batu = random.randint(1,5)
                    air = random.randint(1,5)
                    if pasir<=int(bahan_bangunan[0][2]) and batu<=int(bahan_bangunan[1][2]) and air<=int(bahan_bangunan[2][2]):
                        candi = konso(candi, [idcandi, logged_user, pasir, batu, air])
                        idcandi+=1
                        a = int(bahan_bangunan[0][2])
                        a -= pasir
                        a = str(a)
                        b = int(bahan_bangunan[1][2])
                        b -= batu
                        b = str(b)
                        c = int(bahan_bangunan[2][2])
                        c -= air
                        c = str(c)
                        print(f"Candi berhasil dibangun.\nSisa candi yang perlu dibangun: {100-length(candi)}.")
                    else:
                        print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!")
        if bangun == False:
            print("Membangun candi hanya dapat dilakukan oleh akun Jin Pembangun.")
    else:
        print("Membangun candi hanya dapat dilakukan oleh akun Jin Pembangun.")
    return a,b,c,candi,idcandi

#----------------------------------------------------------------F07 - Jin pengumpul -------------------------------------------------------------------------------
def kumpul(logged_user, jin, bahan_bangunan):
    a = bahan_bangunan[0][2]
    b = bahan_bangunan[1][2]
    c = bahan_bangunan[2][2]
    if logged_user!="bandung_bondowoso" and logged_user!="roro_jonggrang":
        logged_user = int(logged_user)
        kumpul = False
        for i in range (length(jin)):
            if jin[i][1]==logged_user:
                if jin[i][0] == 1:
                    kumpul = True
                    pasir = random.randint(0,5)
                    batu = random.randint(0,5)
                    air = random.randint(0,5)
                    a = int(bahan_bangunan[0][2])
                    a += pasir
                    a = str(a)
                    b = int(bahan_bangunan[1][2])
                    b += batu
                    b = str(b)
                    c = int(bahan_bangunan[2][2])
                    c += air
                    c = str(c)
                    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
        if kumpul == False:
            print("Mengumpulkan bahan hanya dapat dilakukan oleh akun Jin Pengumpul.")
    else:
        print("Mengumpulkan bahan hanya dapat dilakukan oleh akun Jin Pengumpul.")
    return a,b,c

#----------------------------------------------------------------F08 - Batch Kumpul/Bangun -----------------------------------------------------------------------
def batchkumpul(logged_user, jin, bahan_bangunan):
    pasir = 0
    batu = 0
    air = 0
    sumjin = 0
    a = bahan_bangunan[0][2]
    b = bahan_bangunan[1][2]
    c = bahan_bangunan[2][2]
    if logged_user == "bandung_bondowoso":
        for i in range (length(jin)):
            if jin[i][0] == 1:
                sumjin+=1
                pasir+=random.randint(0,5)
                batu+=random.randint(0,5)
                air+=random.randint(0,5)
        if sumjin == 0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            print(f"Mengerahkan {sumjin} jin untuk mengumpulkan bahan.\nJin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")
            a = int(bahan_bangunan[0][2])
            a += pasir
            a = str(a)
            b = int(bahan_bangunan[1][2])
            b += batu
            b = str(b)
            c = int(bahan_bangunan[2][2])
            c += air
            c = str(c)
    else:
        print("Batch kumpul hanya dapat dilakukan oleh akun Bandung Bondowoso.")
    return a,b,c

def batchbangun(logged_user, jin, bahan_bangunan, idcandi):
    pasir = 0
    batu = 0
    air = 0
    candibaru = ["."]
    sumjin = 0
    if logged_user == "bandung_bondowoso":
        for i in range (length(jin)):
            if jin[i][0] == 2:
                sumjin+=1
        if sumjin == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            for i in range (sumjin):
                pasir+=random.randint(1,5)
                batu+=random.randint(1,5)
                air+=random.randint(1,5)
                candibaru = konso(candibaru,[pasir,batu,air,"."])
            if pasir<=int(bahan_bangunan[0][2]) and batu<=int(bahan_bangunan[1][2]) and air <=int(bahan_bangunan[2][2]):
                for i in range (length(jin)):
                    if jin[i][0] == 2:
                        a = 0
                        candi = konso(candi, [str(idcandi),str(jin[i][1]),str(candibaru[a][0]),str(candibaru[a][1]),str(candibaru[a][2]),"."])
                        candi+=1
                        idcandi+=1
            else:
                print(f"Mengerahkan {sumjin} jin untuk membangun candi dengan total bahan {bahan_bangunan[0][2]} pasir, {bahan_bangunan[1][2]} batu, dan {bahan_bangunan[2][2]} air.\nBangun gagal. Kurang {minimal_nol(pasir-int(bahan_bangunan[0][2]))} pasir, {minimal_nol(batu-int(bahan_bangunan[1][2]))} batu, dan {minimal_nol(air-int(bahan_bangunan[2][2]))} air.")
    else:
        print("Batch kumpul hanya dapat dilakukan oleh akun Bandung Bondowoso.")

#-----------------------------------------------------F09 - Ambil Laporan Jin--------------------------------------------------------------------------------
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

#------------------------------------------------------------F10 - Ambil Laporan Candi---------------------------------------------------------------------
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

#------------------------------------------------------------------F11 Hancurkan Candi-----------------------------------------------------------------------
def hancurkancandi(logged_user, candi):
    if logged_user == "roro_jonggrang":
        id = int(input("Masukkan ID candi: "))
        cek_id = False
        for i in range (length(candi)):
            if candi[i][0] == str(id):
                cek_id = True
                check = str(input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? "))
                if check == "Y":
                    print("\nCandi telah berhasil dihancurkan.")
                    candi = removelmt(candi,i)
                else:
                    break
        if cek_id == False:
            print("\nTidak ada candi dengan ID tersebut.")
    return candi

#------------------------------------------------------------------F12 - Ayam berkokok-----------------------------------------------------------------------
def ayamberkokok(candi) :
    print ("Kukuruyuk.. Kukuruyuk..")
    jumlah_candi = length(candi)
    if jumlah_candi < 100 :
        print ("*Bandung Bondowoso angry noise*")
        print ("Roro Jonggrang dikutuk menjadi candi")
        exit()
        # Keluar Program
    else : #jumlah candi > 100
        print ("yah, Bandung Bondowoso memenangkan permainan!")
        exit()
        # Keluar Program

#-----------------------------------------------------------------F13 - Load--------------------------------------------------------------------------------
import os
def load(source):
    if os.path.exists(source):
        users = csvtomatrix(f"{source}/user.csv")
        candi = csvtomatrix(f"{source}/candi.csv")
        bahan_bangunan = csvtomatrix(f"{source}/bahan_bangunan.csv")
        if length(bahan_bangunan)==0:
            bahan_bangunan = konso(bahan_bangunan, ["pasir","serbuk","0","."])
            bahan_bangunan = konso(bahan_bangunan, ["batu","keras","0","."])
            bahan_bangunan = konso(bahan_bangunan, ["air","cair","0","."])
    else:
        print(f"Folder \"{source}\" tidak ditemukan.")
        exit()
#-----------------------------------------------------------------F14 - Save-------------------------------------------------------------------------------
def save(user, candi, bahan_bangunan):
    nama_folder = str(input("\nMasukkan nama folder:"))
    folder_save = ".\save"
    path_folder = os.path.join(folder_save, nama_folder)
    print("\nSaving...\n")
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)
        print(f"Membuat folder {path_folder}...")
    
    nama_file = "user.csv"
    path_file = os.path.join(path_folder, nama_file)

    with open(path_file, mode='w', newline='') as file:
        header = "username;password;role\n"
        file.write(header)
        newline = True
        for i in range (length(user)):
            for j in range(length(user[i])):
                if newline == True:
                    n = user[i][j]
                    file.write(str(n))
                    newline = False
                else:
                    file.write(";")
                    n = user[i][j]
                    file.write(str(n))
            file.write("\n")
            newline = True

    nama_file = "candi.csv"
    path_file = os.path.join(path_folder, nama_file)

    with open(path_file, mode='w', newline='') as file:
        header = "id;pembuat;pasir;batu;air\n"
        file.write(header)
        newline = True
        for i in range (length(candi)):
            for j in range(length(candi[i])):
                if newline == True:
                    n = candi[i][j]
                    file.write(str(n))
                    newline = False
                else:
                    file.write(";")
                    n = candi[i][j]
                    file.write(str(n))
            file.write("\n")
            newline = True
    
    nama_file = "bahan_bangunan.csv"
    path_file = os.path.join(path_folder, nama_file)

    with open(path_file, mode='w', newline='') as file:
        header = "nama;deskripsi;jumlah\n"
        file.write(header)
        newline = True
        for i in range (length(bahan_bangunan)):
            for j in range(length(bahan_bangunan[i])):
                if newline == True:
                    n = bahan_bangunan[i][j]
                    file.write(str(n))
                    newline = False
                else:
                    file.write(";")
                    n = bahan_bangunan[i][j]
                    file.write(str(n))
            file.write("\n")
            newline = True

    print(f"Berhasil menyimpan data di folder {path_folder}!")
#-------------------------------------------------------------------F15 - Help ----------------------------------------------------------------------------
def help(logged_in, logged_user, jin):
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
        else:
            for i in range(length(jin)):
                if int(logged_user) == jin[i][1]:
                    if jin[1][0] == 2:
                        print("1. logout")
                        print("   Untuk keluar dari akun yang digunakan sekarang")
                        print("2. bangun")
                        print("   Untuk membangun candi")
                        print("3. save")
                        print("   Untuk menyimpan data ke dalam suatu file")
                        print("4. exit")
                        print("   Untuk keluar dari program dan kembali ke terminal")
                    if jin[1][0] == 1:
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
#-----------------------------------------------------------------F16 - Exit-------------------------------------------------------------------------------
def close(user,candi,bahan_bangunan):
    answer = "x"
    while answer != "y" and answer != "Y" and answer != "n" and answer != "N":
        answer = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)"))
    if answer == "y" or answer == "Y":
        save(user,candi,bahan_bangunan)
        exit()
    else:
        exit()
