import F00,F01

def pencarianPemain():
    colUsername = 3
    colNama = 0
    colTinggi = 2
    colTanggal = 1
    username = input('Masukkan username: ')
    jumlahUser = F00.banyakParam(F01.dataUser) #Menghitung banyak data pada data user
    isFound = False
    idxDataUser = 1
    #Proses pencarian pemain
    while((isFound == False) and (idxDataUser < jumlahUser)):
        #Apabila username yang diinput telah terdaftar pada data
        if(F01.dataUser[idxDataUser][colUsername] == username):
            print('Nama Pemain: ', F01.dataUser[idxDataUser][colNama])
            print('Tinggi Pemain: ', F01.dataUser[idxDataUser][colTinggi] ,' cm')
            print('Tanggal lahir pemain: ',F01.dataUser[idxDataUser][colTanggal])
            isFound = True
        idxDataUser += 1
    #Jika username yang diinput tidak ada di data
    if(isFound == False):
        print('Username tidak ditemukan')
        
