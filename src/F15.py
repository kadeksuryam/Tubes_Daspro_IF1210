import F00,F01

def cariTiket():
    username = input("Masukkan username: ")
    banyakDataKepemilikanTiket = F00.banyakParam(F01.dataKepemilikanTiket)
    banyakDataWahana = F00.banyakParam(F01.dataWahana)
    colUsername = 0
    colIdWahana = 1
    colBanyakTiket = 2
    colNamaWahana = 1
    #Proses mencari id wahana yang dimiliki oleh user
    for idxDataKepemilikanTiket in range(banyakDataKepemilikanTiket):
        if(username == F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colUsername]):
            tmpIdWahana = F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colIdWahana]
            #Proses mencari data nama wahana pada data wahana untuk digunakan sebagai output dari proses
            for idxDataWahana in range(banyakDataWahana):
                if(tmpIdWahana == F01.dataWahana[idxDataWahana][0]): # 0 adalah indeks dari kolom IdWahana pada file Data Wahana
                    print(F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colIdWahana]," | ",F01.dataWahana[idxDataWahana][colNamaWahana]," | ",F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colBanyakTiket])            
                                 
