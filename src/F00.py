import F01

#Fungsi pengambilan beberapa elemen dari Array
def sliceArray(dataParam, awal, akhir):
    #inisialisasi variabel penampungan sementara
    tmpData = [[] for i in range(awal-1, akhir)]
    idxData = 0
    #iterasi elemen mulai dari index awal-1 sampai akhir-1
    for i in range(awal-1, akhir):
        #isi data sementara
        tmpData[idxData] = dataParam[i]
        idxData += 1
    return tmpData

#Pengganti fungsi append
def tambahArray(data,eltambah):
    mark = '-1'
    indeks = banyakParam(data)
    data[indeks+1] = [mark]
    data[indeks] = eltambah
    return data

#Mencari role user sebagai identitas
def cariRoleUser(username):
    for i in range(banyakParam(F01.dataUser)):
        if(F01.dataUser[i][3] == username):
            roleUser = F01.dataUser[i][5]
    return roleUser

#Banyaknya kolom pada suatu array 1d
def banyakCol(aRowData):
    markCol = '-1'
    isAkhir = False
    jmlCol = 0
    #ketika belum sampai pada mark
    while(isAkhir == False):
        if(aRowData[jmlCol] == markCol):
            isAkhir = True
        jmlCol += 1
    return (jmlCol-1)
    
#Banyaknya data/banyaknya baris pada data/array 2d
def banyakParam(dataParam): 
    jmlData = 0
    markRow = '-1' #disetiap file csv penanda selalu sama
    isAkhir = False
    colAwal = 0
    #ketika belum sampai pada mark
    while(isAkhir == False):
        if(dataParam[jmlData][colAwal] == markRow):
            isAkhir = True
        jmlData += 1
    #return banyak data tanpa mark
    return (jmlData-1)

def sortParam(dataParam, keySort, awal, akhir, ascending): 
	maxCol = banyakCol(dataParam[0]) #jumlah kolom pada parameter terkait
	tmpDataParam = sliceArray(dataParam, awal, akhir) #bagian data yang ingin di sort
	colParam = keySort-1   #kolom yang menjadi acuan sorting (karena 2d)
	jumlahParam = akhir-awal+1 #jumlah data pada parameter terkait
    
    #Lakukan Selection Sort
	for i in range(0, jumlahParam-1):
		idxMxMn = i
		for j in range(i+1, jumlahParam):
			if(ascending == True): #data akan terurut menaik
				#bandingkan data ke j dengan j+1 yang bergantung pada colParam
				if(tmpDataParam[j][colParam] < tmpDataParam[idxMxMn][colParam]):
					idxMxMn = j
			else: #data akan terurut menurun
				if(int(tmpDataParam[j][colParam]) > int(tmpDataParam[idxMxMn][colParam])):
					idxMxMn = j
		for k in range(0, maxCol):
            #lakukan 'Swapping'/penukaran elemen setiap kolomnya
			tmp = tmpDataParam[i][k]
			tmpDataParam[i][k] = tmpDataParam[idxMxMn][k]
			tmpDataParam[idxMxMn][k] = tmp
	return tmpDataParam
       
def removeTiket(username, idWahana, jumlahRemove):
    #inisialisasi konstanta terkait
	idxColUsername = 0
	idxColWahana = 1
	idxColBanyakTiket = 2
	jumlahTiket = banyakParam(F01.dataKepemilikanTiket)
	jumlahSekarang = 1
    
	#data tiket sementara, maximum sampai 10^5-1
	tmpKepemilikanTiket = [[] for i in range(0, 100000)]
	tmpKepemilikanTiket[0] = F01.dataKepemilikanTiket[0]
	#iterasi data Tiket
	for idxTiket in range(1, jumlahTiket):
		#jika ditemukan tiket dengan username dan idWahana yang benar
		isUsernameSesuai = F01.dataKepemilikanTiket[idxTiket][idxColUsername] == username
		isIdWahanaSesuai = F01.dataKepemilikanTiket[idxTiket][idxColWahana] == idWahana
		if(isUsernameSesuai and isIdWahanaSesuai):
			isTiketUserHabis = ((int(F01.dataKepemilikanTiket[idxTiket][idxColBanyakTiket])-int(jumlahRemove)) > 0)
			#tambah tiket ke array jika masih > 0, selain itu abaikan 
			if(isTiketUserHabis == True):
				tiketSekarang = str(int(F01.dataKepemilikanTiket[idxTiket][idxColBanyakTiket])-int(jumlahRemove))
				F01.dataKepemilikanTiket[idxTiket][idxColBanyakTiket] = tiketSekarang
				tmpKepemilikanTiket[jumlahSekarang] = F01.dataKepemilikanTiket[idxTiket]
				jumlahSekarang += 1
		else:
			tmpKepemilikanTiket[jumlahSekarang] = F01.dataKepemilikanTiket[idxTiket]
			jumlahSekarang += 1

	#isi mark di akhir array tmpKepemilikanTiket
	mark = ['-1']
	tmpKepemilikanTiket[jumlahSekarang] = mark
    
	#samakan dataKepemilikanTiket di F01 dengan tmpKepemilikanTiket
	for i in range(0, jumlahTiket+1):
		#sesuaikan urutan data        
		if(i <= jumlahSekarang):
			F01.dataKepemilikanTiket[i] = tmpKepemilikanTiket[i]
		else:
			F01.dataKepemilikanTiket[i] = [] 
