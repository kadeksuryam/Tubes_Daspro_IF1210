import csv,F00,F01,F03

dataTiketHilang = [] #inisialisasi dataTiketHilang

def saveTiketCSV():
        #save dataTiketHilang ke file tiketHilang.csv
	with open("tiketHilang.csv", "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(dataTiketHilang)

def laporanTiketHilang():
	global dataTiketHilang   #Akses variabel global
	#Baca file tiketHilang.csv
	dataTiketHilang =  F01.readCSV("tiketHilang.csv")
	banyakTiketHilang = F00.banyakParam(dataTiketHilang)

	#diasumsikan data yang dimasukkan valid
	username = input('Masukkan username: ')
	tanggalKehilangan = input('Tanggal kehilangan tiket: ')
	idWahana = input('ID wahana: ')
	jumlahHilang = input('Jumlah tiket yang dihilangkan: ')
	dataTiketHilang[banyakTiketHilang] = [username, tanggalKehilangan, idWahana, jumlahHilang, '-1']
	dataTiketHilang[banyakTiketHilang+1] = ['-1']
	#delete tiket
	F00.removeTiket(username, idWahana, jumlahHilang)

	#simpan data kehilangan ke file csv
	saveTiketCSV()
	print('\nLaporan kehilangan tiket Anda telah direkam.')
