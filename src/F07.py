import F00,F01,F02

def cekSaldo(saldoUser,hargaTiket,jumlahTiket):
    return saldoUser < hargaTiket*jumlahTiket

def cekGoldenAccount(roleUser):
    return roleUser == "golden account"

def cekUmur(tLahir,tSekarang):
    jumHariMin = 17*365 #Sebagai syarat 17 tahun, diubah menjadi hari
    jumHariLahir = int(tLahir[0:2]) + int(tLahir[3:5])*28 + int(tLahir[6:10])*365 #Menghitung jumlah total hari dari data tanggal lahir
    jumHariNow = int(tSekarang[0:2]) + int(tSekarang[3:5])*28 + int(tSekarang[6:10])*365 #Menghitung jumlah total hari dari data tanggal sekarang
    return ((jumHariNow-jumHariLahir) >= jumHariMin) #Pengecekan apakah umur 17 tahun atau tidak 

def beliTiket():
    idWahana = input('Masukkan ID Wahana: ')
    tSekarang = input('Masukkan tanggal hari ini: ')
    jumlahTiket = int(input('Jumlah tiket yang dibeli: '))
    jumlahWahana = F00.banyakParam(F01.dataWahana)
    jumlahDataUser = F00.banyakParam(F01.dataUser)
    isTerproses = False #Sebagai penanda bahwa suatu proses telah diproses
    isKetemu = False #Sebagai penanda dalam pencarian data user, akan digunakan untuk mengubah saldo user setelah transaksi
    baris = 0
    #Mencari data-data user yang akan dijadikan sumber untuk proses selanjutnya
    while (baris < jumlahDataUser and isKetemu == False):
        baris += 1
        if(F01.dataUser[baris][3]==F02.usernameLogin):
            isKetemu = True
            tLahirUser = F01.dataUser[baris][1] #Mengambil data tangga; dari file dataUser csv
            saldoUser = int(F01.dataUser[baris][6]) #Mengambil data saldo user
            tinggiUser = int(F01.dataUser[baris][2]) #Mengambil data tinggi user
            roleUser = F01.dataUser[baris][5] #Mengambil status user 
    #Proses pembelian tiket
    for idxDataWahana in range(1, jumlahWahana):
        if(idWahana == F01.dataWahana[idxDataWahana][0]): #Menyocokkan id wahana yang diinput dengan yang ada di data
            hargaTiket = int(F01.dataWahana[idxDataWahana][2]) #Mengambil harga tiket dari file wahana 
            #Mengklasifikasi syarat dari wahana
            if((cekUmur(tLahirUser,tSekarang) == False) and (F01.dataWahana[idxDataWahana][3] == 'anak-anak' or F01.dataWahana[idxDataWahana][3] == 'semua umur')):
                #Jika tinggi user tidak memenuhi syarat
                if(F01.dataWahana[idxDataWahana][4] == ">=170" and tinggiUser < 170):
                    isTerproses = True
                    print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
                    print('Silakan menggunakan wahana lain yang tersedia.')
                else: #(F01.dataWahana[i][4] == "tanpa batasan"):
                    #Memeriksa apakah user memiliki golden account, jika iya maka akan diskon 50%
                    if (cekGoldenAccount(roleUser) == True):
                        hargaTiket = hargaTiket*0.5
                        #Memeriksa apakah user memiliki saldo yang cukup untuk membeli tiket
                        if(cekSaldo(saldoUser,hargaTiket,jumlahTiket) == True):
                            isTerproses = True
                            print('Saldo Anda tidak cukup')
                            print('Silakan mengisi saldo anda')
                        else:
                            isTerproses = True
                            print('Selamat bersenang-senang di '+F01.dataWahana[idxDataWahana][1]+'.')
                            F01.dataUser[baris][6] = str(int(saldoUser) - int(hargaTiket*jumlahTiket))
                            F01.dataPembelianTiket = F00.tambahArray(F01.dataPembelianTiket,[F02.usernameLogin,tSekarang,idWahana,str(jumlahTiket)])
                            F01.dataKepemilikanTiket = F00.tambahArray(F01.dataKepemilikanTiket,[F02.usernameLogin,idWahana,str(jumlahTiket)])
                    #Jika user tidak memiliki golden tiket
                    else:
                        #Memeriksa apakah user memiliki saldo yang cukup untuk membeli tiket
                        if(cekSaldo(saldoUser,hargaTiket,jumlahTiket) == True):
                            isTerproses = True
                            print('Saldo Anda tidak cukup')
                            print('Silakan mengisi saldo anda')
                        else:
                            isTerproses = True
                            print('Selamat bersenang-senang di '+F01.dataWahana[idxDataWahana][1]+'.')
                            F01.dataUser[baris][6] = str(int(saldoUser) - int(hargaTiket*jumlahTiket))
                            F01.dataPembelianTiket = F00.tambahArray(F01.dataPembelianTiket,[F02.usernameLogin,tSekarang,idWahana,str(jumlahTiket)])
                            F01.dataKepemilikanTiket = F00.tambahArray(F01.dataKepemilikanTiket,[F02.usernameLogin,idWahana,str(jumlahTiket)])
            elif((cekUmur(tLahirUser,tSekarang) == True) and (F01.dataWahana[idxDataWahana][3] == 'dewasa' or F01.dataWahana[idxDataWahana][3] == 'semua umur')):
                if(F01.dataWahana[idxDataWahana][4] == '>=170' and tinggiUser < 170):
                    isTerproses = True
                    print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
                    print('Silakan menggunakan wahana lain yang tersedia.')
                else: #(F01.dataWahana[i][4] == 'tanpa batasan'):
                    #Memeriksa apakah user memiliki golden account, jika iya maka akan diskon 50%
                    if (cekGoldenAccount(roleUser) == True):
                        hargaTiket = hargaTiket*0.5
                        #Memeriksa apakah user memiliki saldo yang cukup untuk membeli tiket
                        if(cekSaldo(saldoUser,hargaTiket,jumlahTiket) == True):
                            isTerproses = True
                            print('Saldo Anda tidak cukup')
                            print('Silakan mengisi saldo anda')
                        else:
                            isTerproses = True
                            print('Selamat bersenang-senang di '+F01.dataWahana[idxDataWahana][1]+'.')
                            F01.dataUser[baris][6] = str(int(saldoUser) - int(hargaTiket*jumlahTiket))
                            F01.dataPembelianTiket = F00.tambahArray(F01.dataPembelianTiket,[F02.usernameLogin,tSekarang,idWahana,str(jumlahTiket)])
                            F01.dataKepemilikanTiket = F00.tambahArray(F01.dataKepemilikanTiket,[F02.usernameLogin,idWahana,str(jumlahTiket)])
                    #Jika user tidak memiliki golden tiket
                    else:
                        #Memeriksa apakah user memiliki saldo yang cukup untuk membeli tiket
                        if(cekSaldo(saldoUser,hargaTiket,jumlahTiket) == True):
                            isTerproses = True
                            print('Saldo Anda tidak cukup')
                            print('Silakan mengisi saldo anda')
                        else:
                            isTerproses = True
                            print('Selamat bersenang-senang di '+F01.dataWahana[idxDataWahana][1]+'.')
                            F01.dataUser[baris][6] = str(int(saldoUser) - int(hargaTiket*jumlahTiket))
                            F01.dataPembelianTiket = F00.tambahArray(F01.dataPembelianTiket,[F02.usernameLogin,tSekarang,idWahana,str(jumlahTiket)])
                            F01.dataKepemilikanTiket = F00.tambahArray(F01.dataKepemilikanTiket,[F02.usernameLogin,idWahana,str(jumlahTiket)])
            elif(F01.dataWahana[idxDataWahana][3] == 'semua umur'):
                if(F01.dataWahana[idxDataWahana][4] == '>=170' and tinggiUser < 170):
                    isTerproses = True
                    print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
                    print('Silakan menggunakan wahana lain yang tersedia.')
                else: #(F01.dataWahana[i][4] == 'tanpa batasan'):
                    #Memeriksa apakah user memiliki golden account, jika iya maka akan diskon 50%
                    if(cekGoldenAccount(roleUser) == True):
                        hargaTiket = hargaTiket*0.5
                        #Memeriksa apakah user memiliki saldo yang cukup untuk membeli tiket
                        if(cekSaldo(saldoUser,hargaTiket,jumlahTiket) == True):
                            isTerproses = True
                            print('Saldo Anda tidak cukup')
                            print('Silakan mengisi saldo anda')
                        else:
                            isTerproses = True
                            print('Selamat bersenang-senang di '+F01.dataWahana[idxDataWahana][1]+'.')
                            F01.dataUser[baris][6] = str(int(saldoUser) - int(hargaTiket*jumlahTiket))
                            F01.dataPembelianTiket = F00.tambahArray(F01.dataPembelianTiket,[F02.usernameLogin,tSekarang,idWahana,str(jumlahTiket)])
                            F01.dataKepemilikanTiket = F00.tambahArray(F01.dataKepemilikanTiket,[F02.usernameLogin,idWahana,str(jumlahTiket)])
                    #Jika user tidak memiliki golden tiket
                    else:
                        #Memeriksa apakah user memiliki saldo yang cukup untuk membeli tiket
                        if(cekSaldo(saldoUser,hargaTiket,jumlahTiket) == True):
                            isTerproses = True
                            print('Saldo Anda tidak cukup')
                            print('Silakan mengisi saldo anda')
                        else:
                            isTerproses = True
                            print('Selamat bersenang-senang di '+F01.dataWahana[idxDataWahana][1]+'.')
                            F01.dataUser[baris][6] = str(int(saldoUser) - int(hargaTiket*jumlahTiket))
                            F01.dataPembelianTiket = F00.tambahArray(F01.dataPembelianTiket,[F02.usernameLogin,tSekarang,idWahana,str(jumlahTiket)])
                            F01.dataKepemilikanTiket = F00.tambahArray(F01.dataKepemilikanTiket,[F02.usernameLogin,idWahana,str(jumlahTiket)])
    #Jika id wahana yang diinput salah
    if(isTerproses == False):
        print('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
        print('Silakan menggunakan wahana lain yang tersedia.')
    

