import csv,F01

def saveFile():
        #input nama file yang dimaksud
	namaFile = input('Masukkan nama File User: ')
	with open(namaFile, "w", newline="") as f: #baca file dan proses
		writer = csv.writer(f)     
		writer.writerows((F01.dataUser)) #tulis data dari parameter yang dimaksud ke file
	
	#prosesnya sama dengan diatas    
	namaFile = input('Masukkan nama File Daftar Wahana: ')
	with open(namaFile, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(F01.dataWahana)
	
	namaFile = input('Masukkan nama File Pembelian Tiket: ')
	with open(namaFile, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(F01.dataPembelianTiket)
	
	namaFile = input('Masukkan nama File Penggunaan Tiket: ')
	with open(namaFile, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(F01.dataPenggunaanTiket)
	
	namaFile = input('Masukkan nama File Kepemilikan Tiket: ')
	with open(namaFile, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(F01.dataKepemilikanTiket)
	
	namaFile = input('Masukkan nama File Refund Tiket: ')
	with open(namaFile, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(F01.dataRefundTiket)
	
	namaFile = input('Masukkan nama File Kritik dan Saran: ')
	with open(namaFile, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(F01.dataKritikSaran)
	
	print('\nData berhasil disimpan!')
