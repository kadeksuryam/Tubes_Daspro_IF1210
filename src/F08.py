import F00,F01,F02
	
def pakaiTiket():
    idWahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jumlahTiket = input("Jumlah tiket yang digunakan: ")
    username = F02.usernameLogin
    jumlahDataKepemilikanTiket = F00.banyakParam(F01.dataKepemilikanTiket)
    isTerproses = False
    colUsername = 0
    colIdWahana = 1
    colJumlahTiket = 2
    idxDataKepemilikanTiket = 0
    while((idxDataKepemilikanTiket < jumlahDataKepemilikanTiket) and (isTerproses == False)):
        if(username == F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colUsername] and idWahana == F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colIdWahana]) and (int(jumlahTiket) <= int(F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colJumlahTiket])):
            isTerproses = True
        idxDataKepemilikanTiket += 1
    #Apabila id wahana yang diinput salah, maka akan dikeluarkan output tidak valid
    if(isTerproses == True):
        #Melakukan prosedur remove tiket sesuai dengan jumlah tiket yang dimiliki
        F00.removeTiket(username,idWahana,jumlahTiket)
        F01.dataPenggunaanTiket = F00.tambahArray(F01.dataPenggunaanTiket,[username,tanggal,idWahana,jumlahTiket])
        print("Terima kasih telah bermain.")
    else: #(isTerproses == False):
        print("Tiket Anda tidak valid dalam sistem kami")
