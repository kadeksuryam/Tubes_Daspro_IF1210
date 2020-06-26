import F00,F01,B01

#username yang akan login saat ini
usernameLogin = "" 
#state apakah user sudah login atau belum
isLogin = False 

def login():
	global usernameLogin
	#Input username dan password dan deklarasi konstanta terkait
	usernameLogin = input('Masukkan username: ')
	passwordLogin = input('Masukkan password: ')
	jumlahUser = F00.banyakParam(F01.dataUser) 
	global isLogin
    #index dimulai dari 1, karena index ke 0 adalah nama parameter
	idxUser = 1
    
	#iterasi isi dataUser
	#ketika belum login dan dataUser belum dijelajahi semua
	while(idxUser != jumlahUser and isLogin == False): 
		#inisialisasi konstanta index kolom terkait
		idxColUsername = 3
		idxColStatus = 5
		idxColPassword = 4
		idxColNamaPemain = 0    
		#ketika ditemukan username yang dimaksud
		#verifikasi password menggunakkan module di B01, karena password pada dasarnya di hash
		isUsernameSesuai = (F01.dataUser[idxUser][idxColUsername] == usernameLogin)
		isPasswordSesuai = (B01.verifikasiPassword(F01.dataUser[idxUser][idxColPassword], passwordLogin))
		if(isUsernameSesuai and isPasswordSesuai):
			if(F01.dataUser[idxUser][idxColStatus] == 'admin'):
				print('Anda login sebagai admin')
			else:
                                print('Selamat bersenang-senang, ' + F01.dataUser[idxUser][idxColNamaPemain])
			isLogin = True
		idxUser += 1
                            
    #pemain belum terdaftar atau data yang diinput salah
	if(isLogin == False):
		print('Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silahkan coba lagi!')
		login()

