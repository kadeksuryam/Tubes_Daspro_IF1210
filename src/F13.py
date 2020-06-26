import F00,F01

def topup():
    Jumlah = F00.banyakParam(F01.dataUser)
    kolomUsername = 3
    kolomSaldo = 6
    tmpDataTopUp = F00.sliceArray(F01.dataUser,2,Jumlah)
    username = input("Masukkan username: ")
    topup = input("Masukkan saldo yang di-top up: ")
    for idxDataUser in range(0,Jumlah-1):
        saldo = tmpDataTopUp[idxDataUser][kolomSaldo]
        if (username == tmpDataTopUp[idxDataUser][kolomUsername]):
            total = int(saldo) + int(topup)
            tmpDataTopUp[idxDataUser][kolomSaldo] = str(total)
    print("Top up berhasil. Saldo "+username+" bertambah menjadi", total)
    
