import F00,F01

def bestWahana():
	#sort dataPembelian menurut ID
	banyakPembelian = F00.banyakParam(F01.dataPembelianTiket)
	idxIdWahana = 2
	idxJmlTiket = 3
	tmpDataPembelian = F00.sortParam(F01.dataPembelianTiket, idxIdWahana+1, 2, banyakPembelian, True)
	#buat prefix sum
	totalPembelian = [[] for i in range(0, 100000)]
	totalPembelian[0] = ['Id_wahana','Jumlah_tiket','-1']
	totalPembelian[1] = [tmpDataPembelian[0][idxIdWahana], tmpDataPembelian[0][idxJmlTiket], '-1']
	iterator = 2
	for i in range(1, banyakPembelian-1):
		if(tmpDataPembelian[i][2] == totalPembelian[iterator-1][0]):
			totalPembelian[iterator-1][1] = str(int(totalPembelian[iterator-1][1])+int(tmpDataPembelian[i][3]))
		else:
			totalPembelian[iterator] = [tmpDataPembelian[i][idxIdWahana], tmpDataPembelian[i][idxJmlTiket], '-1']
			iterator += 1
    
	#print(totalPembelian[0])
	totalPembelian[iterator] = ['-1']   
	colBanyakPembelian = 2
	banyakIdWahana = F00.banyakParam(totalPembelian)
	#sort menurut banyaknya pembelian tiket
	totalPembelian = F00.sortParam(totalPembelian, colBanyakPembelian, 2, banyakIdWahana, False)    

	#output 3 besar
	for i in range(0, 3):
		#searching ID wahana, untuk mendapatkan nama wahana
		banyakWahana = F00.banyakParam(F01.dataWahana)
		j = 1
		isFound = False
		#selama idwahana pada totalPembelian belum ditemukan
		while(j != banyakWahana and isFound == False):
			if(totalPembelian[i][0] == F01.dataWahana[j][0]):
				isFound = True
				print(str(i+1) + ' | ' + totalPembelian[i][0] + ' | ' + F01.dataWahana[j][1] + ' |' + totalPembelian[i][1])
			j += 1
	
