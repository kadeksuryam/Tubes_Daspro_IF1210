import F00,F01

def goldenAccount():
	#inisialisasi konstanta    
	biayaUpgrade = 50000    
	print('Dengan mengupgrade ke golden Account anda akan dikenakan biaya sebesar ' + str(biayaUpgrade))
	username = input('Masukkan username yang ingin di-upgrade: ')
	jumlahUser = F00.banyakParam(F01.dataUser)
	isTerproses = False
	idxColUser = 3
	idxColSaldo = 6    
	idxColStatus = 5
	idxDataUser = 1
    #Cari user dari dataUser dari paling belakang
	while((idxDataUser < jumlahUser) and (isTerproses == False)):
		isUsernameFound = (username == F01.dataUser[idxDataUser][idxColUser])
		isSaldoCukup = (int(F01.dataUser[idxDataUser][idxColSaldo]) >= biayaUpgrade)
		#jika username ditemukan dan saldonya mencukupi        
		if(isUsernameFound and isSaldoCukup):
			isTerproses = True
			F01.dataUser[idxDataUser][idxColStatus] = 'golden account'  #ubah status di dataUser menjadi golden account
			#kurangkan saldo user            
			F01.dataUser[idxDataUser][idxColSaldo] =  str(int(F01.dataUser[idxDataUser][idxColSaldo])-biayaUpgrade)           
			print('')
			print('Akun Anda telah diupgrade')
		idxDataUser += 1
    #jika tidak ditemukan user yang dimaksud
	if(isTerproses == False):
		print('Username yang dimaksud tidak terdaftar , silahkan coba lagi!')
	

