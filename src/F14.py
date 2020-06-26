import F00,F01

def riwayat_wahana():
        Jumlah = F00.banyakParam(F01.dataPenggunaanTiket)
        tmpData1 = F00.sliceArray(F01.dataPenggunaanTiket,2,Jumlah)
        ID_Wahana = input("Masukkan ID Wahana: ")
        colIdWahana = 2
        colTanggal = 1
        colUsername = 0
        colBanyakTiket = 3
        tmpJumlah=0
        print("Riwayat: ")
        #Menghitung total berapa banyak yang ID_Wahananya sama, akan digunakan sebagai ruang array tmpData2
        for idxDataWahana in range(0,Jumlah-1):
            if (ID_Wahana == tmpData1[idxDataWahana][colIdWahana]):
                tmpJumlah += 1
        tmpData2 = [["" for j in range(3)]for k in range(tmpJumlah)]
        idxTmpData2 = 0 #Inisialisasi indeks tmpData2
        #Membuat tmpData2 yang berisi data yang memiliki ID_Wahana yang dicari
        for idxTmpData1 in range(0,Jumlah-1):
            if (ID_Wahana == tmpData1[idxTmpData1][colIdWahana]):
                isSelected = False
                while(isSelected == False):
                    tmpData2[idxTmpData2] = tmpData1[idxTmpData1]
                    idxTmpData2 += 1
                    isSelected = True
        for idxRiwayat in range(0,tmpJumlah):
             print(tmpData2[idxRiwayat][colTanggal],"|",tmpData2[idxRiwayat][colUsername],"|",tmpData2[idxRiwayat][colBanyakTiket])
        






