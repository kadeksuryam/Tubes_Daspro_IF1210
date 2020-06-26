import F00,F01,F02

def kritikDanSaran():
        idWahana = input("Masukkan ID Wahana: ")
        tanggalPelaporan = input("Masukkan tanggal pelaporan: ")
        kritik = input("Kritik/saran Anda: ")
        F01.dataKritikSaran = F00.tambahArray(F01.dataKritikSaran,[F02.usernameLogin,tanggalPelaporan,idWahana,kritik])
        print('')
        print("Kritik dan saran Anda kami terima.")
    


