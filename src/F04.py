import F00,F01,B01

#fungsi yang mengecek apakah user yang dimaksud sudah ada dalam dataUser atau belum
def isTerdaftar(username):
	jumlahUsername = F00.banyakParam(F01.dataUser)
	idxUsername = 3
	iterator = 1 #mulai dari 1 karena kolom ke-0 adalah nama parameter
	isFound = False
	#ketika dataUser belum habis dan belum ditemukan username yang sama
	while((iterator != jumlahUsername) and (isFound == False)):
		if((username == F01.dataUser[iterator][idxUsername])): isFound = True
		iterator += 1   
	return isFound

def signup():
        #input data parameter yang diperlukan
        namaPemain = input('Masukkan nama pemain: ')
        tglPemain = input('Masukkan tanggal lahir pemain (DD/MM/YYYY): ')
        tinggiPemain = input('Masukkan tinggi badan pemain (cm): ')
        cekUsername = False
	#ketika masih ada username yang sama, user terus diminta menggantinya
        while(cekUsername == False):
                usernamePemain = input('Masukkan username pemain: ')
                if(isTerdaftar(usernamePemain) == True):
                        print('Username tersebut sudah terdaftar, silahkan gunakan username yang lain')
                else:
                        cekUsername = True
                        passwordPemain = input('Masukkan password pemain: ')
	#isi data diatas ke dataUser dengan password user di hash dengan module di B00
        F01.dataUser = F00.tambahArray(F01.dataUser,[namaPemain, tglPemain, tinggiPemain, usernamePemain, B01.hashMyPassword(passwordPemain), 'pemain', 0])
        print('')
        print('Selamat menjadi pemain, ' + namaPemain + '. Selamat bermain.')
        
