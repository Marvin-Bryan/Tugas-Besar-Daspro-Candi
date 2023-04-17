import data
# RUN
def run(input, user, candi, jin, bahan_bangunan):
    if input == "login":
        data.login()
    elif input == "logout":
        data.logout()
    elif input == "summonjin":
        data.summonjin()
    elif input == "hapusjin":
        data.hapusjin()
    elif input == "ubahjin":
        data.ubahjin()
    elif input == "bangun":
        data.bangun()
    elif input == "kumpul":
        data.kumpul()
    elif input == "batchkumpul":
        data.batchkumpul()
    elif input == "batchbangun":
        data.batchbangun()
    elif input == "laporanjin":
        data.laporanjin(user, jin, bahan_bangunan)
    elif input == "laporancandi":
        data.laporancandi(user, candi)
    elif input == "hancurkancandi":
        data.hancurkancandi()
    elif input == "ayamberkokok":
        data.ayamberkokok()
    elif input == "save":
        data.save()
    elif input == "help":
        data.help()
    elif input == "exit":
        data.exit()
    else:
        return 0
