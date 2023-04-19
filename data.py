# Data Penting
def length(a):
    sum = 0 
    while a[sum] != ".": # menggunakan titik untuk marking
        sum+=1
    return sum

def konso(a, b): # fungsi append
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
   
# F01 & F02 - BUAT JADI FUNCTION
def login(users, logged_in, logged_user):
    # tampilkan prompt login
    if logged_in:
        username = ""
        for i in range (length(users)):
            if users[i][2] == users:
                username = users[i][0]
        print(username)
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
def logout(logged_in, logged_user):
    logged_in = False
    logged_user = ""
    print("Logout berhasil!")
    return logged_in, logged_user

def help():
    print("Daftar command yang dapat dipanggil:")
    print("logout: Keluar dari sistem.")
    print("help: Tampilkan daftar command yang dapat dipanggil.")
    


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
       pasir+=candi[i][2]
       batu+=candi[i][3]
       air+=candi[i][4]
    print("> Total Pasir yang digunakan:", pasir)
    print("> Total Batu yang digunakan:", batu)
    print("> Total Air yang digunakan:", air)
    if length(candi)>0:
        hargacandi = [0 for i in range (length(candi))]
        for i in range (length(candi)):
           hargacandi[i]= 10000*candi[i][2] + 15000*candi[i][3] + 7500*candi[i][4]
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
import argparse
def load(source):
    if os.path.exists(source):
        users = csvtomatrix(f"{source}/user.csv")
        candi = csvtomatrix(f"{source}/candi.csv")
        bahan_bangunan = csvtomatrix(f"{source}/bahan_bangunan.csv")
        return users, candi, bahan_bangunan
    else:
        print(f"Folder \"{source}\" tidak ditemukan.")
        exit()