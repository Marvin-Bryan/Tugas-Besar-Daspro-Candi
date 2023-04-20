import data
# RUN
def run(input, user, candi, jin, bahan_bangunan, logged_in, logged_user):
    if input == "login":
        hasil = data.login(user, logged_in, logged_user)
        return hasil
    elif input == "logout":
        hasil = data.logout(logged_in, logged_user)
        return hasil
    elif input == "summonjin":
        jin = data.summonjin(logged_user, jin)
        return jin
    elif input == "hapusjin":
        jindancandi = data.hapusjin(jin, candi)
        return jindancandi
    elif input == "ubahjin":
        data.ubahjin(jin)
    elif input == "bangun":
        data.bangun()
    elif input == "kumpul":
        data.kumpul()
    elif input == "batchkumpul":
        data.batchkumpul()
    elif input == "batchbangun":
        data.batchbangun()
    elif input == "laporanjin":
        data.laporanjin(logged_user, jin, bahan_bangunan)
    elif input == "laporancandi":
        data.laporancandi(logged_user, candi)
    elif input == "hancurkancandi":
        data.hancurkancandi()
    elif input == "ayamberkokok":
        data.ayamberkokok()
    elif input == "save":
        data.save()
    elif input == "help":
        data.help(logged_in, logged_user)
    elif input == "exit":
        exit()
    else:
        return 0