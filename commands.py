import data
# RUN
def run(input, user, candi, jin, bahan_bangunan, logged_in, logged_user, idjin, idcandi):
    if input == "login":
        hasil = data.login(user, logged_in, logged_user)
        return hasil
    elif input == "logout":
        hasil = data.logout(logged_in, logged_user)
        return hasil
    elif input == "summonjin":
        datajin = data.summonjin(logged_user, jin, user, idjin)
        return datajin
    elif input == "hapusjin":
        candijinuser = data.hapusjin(jin, candi, logged_user, user)
        return candijinuser
    elif input == "ubahjin":
        jin = data.ubahjin(jin, logged_user)
        return jin
    elif input == "bangun":
        hasil = data.bangun(candi, bahan_bangunan, logged_user, jin, idcandi)
        return hasil
    elif input == "kumpul":
        hasil = data.kumpul(logged_user, jin, bahan_bangunan)
        return hasil
    elif input == "batchkumpul":
        hasil = data.batchkumpul(logged_user, jin, bahan_bangunan)
        return hasil
    elif input == "batchbangun":
        hasil = data.batchbangun(logged_user, jin, bahan_bangunan, idcandi)
        return hasil
    elif input == "laporanjin":
        data.laporanjin(logged_user, jin, bahan_bangunan)
    elif input == "laporancandi":
        data.laporancandi(logged_user, candi)
    elif input == "hancurkancandi":
        hasilcandi = data.hancurkancandi(logged_user, candi)
        return hasilcandi
    elif input == "ayamberkokok":
        data.ayamberkokok(candi)
    elif input == "save":
        data.save(user, candi, bahan_bangunan)
    elif input == "help":
        data.help(logged_in,logged_user, jin)
    elif input == "exit":
        data.close(user,candi,bahan_bangunan)
    else:
        return 0