import F00,F01,F02

def refund():
        id_wahana = input("Masukkan ID wahana: ")
        nTiket = input("Jumlah tiket yang di-refund: ")
        tanggalRefund = input("Masukkan tanggal hari ini: ")
        jumlahDataUser = F00.banyakParam(F01.dataUser)
        jumlahDataKepemilikanTiket = F00.banyakParam(F01.dataKepemilikanTiket)
        jumlahDataWahana = F00.banyakParam(F01.dataWahana)
        colHargaWahana = 2
        colIdWahana = 1
        colTiket = 2
        colSaldo = 6
        colUsername = 0
        isFound=False
        idxDataKepemilikanTiket = 1
        #Mencari harga tiket wahana yang diinput
        for idxDataWahana in range(1,jumlahDataWahana):
                if(id_wahana==F01.dataWahana[idxDataWahana][0]):
                        hargaWahana = int(F01.dataWahana[idxDataWahana][colHargaWahana]) 
        while(idxDataKepemilikanTiket < jumlahDataKepemilikanTiket):
                if(F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colUsername]==F02.usernameLogin and id_wahana==F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colIdWahana] and (int(nTiket) <= int(F01.dataKepemilikanTiket[idxDataKepemilikanTiket][colTiket]))):
                        for idxDataUser in range(1,jumlahDataUser):
                                if(F02.usernameLogin == F01.dataUser[idxDataUser][3]):
                                        tmpSaldoUser = int(F01.dataUser[idxDataUser][colSaldo]) #Saldo sementara untuk diproses
                                        F01.dataUser[idxDataUser][6] = str(int((tmpSaldoUser + int(nTiket)*0.75*hargaWahana))) #Saldo setelah ditambah uang refund
                                        isFound=True
                idxDataKepemilikanTiket += 1
        if (isFound==True): #Jika memang user memiliki tiket terkait
                F00.removeTiket(F02.usernameLogin,id_wahana,nTiket) #Melakukan fungsi remove tiket sesuai jumlah tiket yang direfund
                F01.dataRefundTiket = F00.tambahArray(F01.dataRefundTiket,[F02.usernameLogin,tanggalRefund,id_wahana,nTiket])
                print('')
                print("Uang refund sudah kami berikan pada akun Anda.")
        else: #User tidak memiliki tiket terkait atau berbohong
                print("Anda tidak memiliki tiket terkait")


            
                
                


