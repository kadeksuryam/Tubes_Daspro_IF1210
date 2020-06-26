import F00,F01

def pencarianWahana():
    colIdWahana = 0
    colNamaWahana = 1
    colHarga = 2
    colUmur = 3
    colTinggi = 4
    isFound = False
    print('Jenis batasan umur:')
    print('1. Anak-anak (<17 tahun)')
    print('2. Dewasa (>=17 tahun)')
    print('3. Semua umur')
    print('')
    print('Jenis batasan tinggi badan')
    print('1. Lebih dari 170 cm')
    print('2. Tanpa batasan')
    print('')
    print('Masukkan batasan dengan nomor pilihan')
    print('')
    batasanUmur = int(input('Batasan umur pemain: '))
    #Validasi input user
    while(batasanUmur != 1 and batasanUmur != 2 and batasanUmur != 3):
        print('Batasan umur tidak valid!')
        batasanUmur = int(input('Batasan umur pemain: '))
    batasanTinggi = int(input('Batasan tinggi badan: '))
    while(batasanTinggi != 1 and batasanTinggi != 2):
        print('Batasan tinggi badan tidak valid!')
        batasanTinggi = int(input('Batasan tinggi badan: '))
    daftarWahana = F00.banyakParam(F01.dataWahana)
    #Proses pencarian wahana
    for idxDataWahana in range(1, daftarWahana):
        #Jika wahana adalah untuk anak - anak
        if(F01.dataWahana[idxDataWahana][colUmur] == 'anak-anak' and batasanUmur == 1):
            #Jika batas tinggi wahana lebih dari 170 cm
            if(batasanTinggi == 1 and F01.dataWahana[idxDataWahana][colTinggi] == '>=170'):
                isFound = True
                print(F01.dataWahana[idxDataWahana][colIdWahana],' | ',F01.dataWahana[idxDataWahana][colNamaWahana],' | ',F01.dataWahana[idxDataWahana][colHarga])
            #Jika wahana tidak memiliki batas tinggi
            elif(batasanTinggi == 2 and F01.dataWahana[idxDataWahana][colTinggi] == 'tanpa batasan'):
                isFound = True
                print(F01.dataWahana[idxDataWahana][colIdWahana],' | ',F01.dataWahana[idxDataWahana][colNamaWahana],' | ',F01.dataWahana[idxDataWahana][colHarga])
        #Jika wahana adalah untuk dewasa
        elif(F01.dataWahana[idxDataWahana][colUmur] == 'dewasa' and batasanUmur == 2):
            #Jika batas tinggi wahana lebih dari 170 cm
            if(batasanTinggi == 1 and F01.dataWahana[idxDataWahana][colTinggi] == '>=170'):
                isFound = True
                print(F01.dataWahana[idxDataWahana][colIdWahana],' | ',F01.dataWahana[idxDataWahana][colNamaWahana],' | ',F01.dataWahana[idxDataWahana][colHarga])
            #Jika wahana tidak memiliki batas tinggi
            elif(batasanTinggi == 2 and F01.dataWahana[idxDataWahana][colTinggi] == 'tanpa batasan'):
                isFound = True
                print(F01.dataWahana[idxDataWahana][colIdWahana],' | ',F01.dataWahana[idxDataWahana][colNamaWahana],' | ',F01.dataWahana[idxDataWahana][colHarga])
        #Jika wahana untuk semua umur
        elif(F01.dataWahana[idxDataWahana][colUmur] == 'semua umur' and batasanUmur == 3):
            #Jika batas tinggi wahana lebih dari 170 cm
            if(batasanTinggi == 1 and F01.dataWahana[idxDataWahana][colTinggi] == '>=170'):
                isFound = True
                print(F01.dataWahana[idxDataWahana][colIdWahana],' | ',F01.dataWahana[idxDataWahana][colNamaWahana],' | ',F01.dataWahana[idxDataWahana][colHarga])
            #Jika wahana tidak memiliki batas tinggi
            elif(batasanTinggi == 2 and F01.dataWahana[idxDataWahana][colTinggi] == 'tanpa batasan'):
                isFound = True
                print(F01.dataWahana[idxDataWahana][colIdWahana],' | ',F01.dataWahana[idxDataWahana][colNamaWahana],' | ',F01.dataWahana[idxDataWahana][colHarga])
    #Jika tidak ada wahana yang cocok dengan input user
    if(isFound == False):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu")
