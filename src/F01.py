import csv
dataUser = dataWahana = dataPembelianTiket = dataPenggunaanTiket = dataRefundTiket = dataKritikSaran = dataKepemilikanTiket = []

#Konversi objek reader ke static array 2d        
def convertReader(dataReader):
        #asumsikan jumlah data maksimum adalah (10^5)-1
        dataParam = [[] for i in range(0,100000)]
        #iterasi isi objek dataReader
        mark = '-1' #disetiap file csv penanda selalu sama
        isAkhir = False 
        iterator = 0
        #ketika belum sampai pada mark
        while(isAkhir == False):
            tmpARow = next(dataReader)
            dataParam[iterator] = tmpARow
            if(tmpARow[0] == mark):
                isAkhir = True
            iterator += 1
        #kembalikan variabel dataParam yang merupakan array 2 dimensi
        return dataParam
    
#Read sekaligus convert ke array 2d         
def readCSV(namaFile):
        #read file dari directory yang sama dengan file ini
        dataCsv = open(namaFile, 'r')
        #baca semua isi dari dataCsv yang dibatasi oleh koma (,)
        reader = csv.reader(dataCsv, delimiter=',')
        return convertReader(reader) #mengembalikan objek reader
    
#Main Function
def loadFile():
        #Akses variabel global
        global dataUser 
        #karena setiap proses nama filenya berbeda-beda, sehingga kita harus mengulang-ulang input nama file
        namaFile = input('Masukkan nama File User: ')
        #convert objek reader ke array 2d
        dataUser = readCSV(namaFile)
        
        #prosesnya sama dengan diatas
        global dataWahana
        namaFile = input('Masukkan nama File Daftar Wahana: ')
        dataWahana = readCSV(namaFile)
        
        global dataPembelianTiket
        namaFile = input('Masukkan nama File Pembelian Tiket: ')
        dataPembelianTiket = readCSV(namaFile)
        
        global dataPenggunaanTiket
        namaFile = input('Masukkan nama File Penggunaan Tiket: ')
        dataPenggunaanTiket = readCSV(namaFile)
        
        global dataKepemilikanTiket
        namaFile = input('Masukkan nama File Kepemilikan Tiket: ')
        dataKepemilikanTiket = readCSV(namaFile)
        
        global dataRefundTiket
        namaFile = input('Masukkan nama File Refund Tiket: ')
        dataRefundTiket = readCSV(namaFile)
        
        global dataKritikSaran
        namaFile = input('Masukkan nama File Kritik dan Saran: ')
        dataKritikSaran = readCSV(namaFile)
        
        print('')
        print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")

        
