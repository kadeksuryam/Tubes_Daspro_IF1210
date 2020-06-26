import F00,F01

def tambahWahana():
    print("Masukkan Informasi Wahana yang ditambahkan: ")
    idWahana = input("Masukkan ID Wahana: ")
    namaWahana = input("Masukkan Nama Wahana: ")
    hargaTiket = input("Masukkan Harga Tiket: ")
    batasUmur = input("Batasan umur: ")
    batasTinggi = input("Batasan tinggi badan: ")
    F01.dataWahana = F00.tambahArray(F01.dataWahana,[idWahana,namaWahana,hargaTiket,batasUmur,batasTinggi])
    print('')
    print("Info wahana telah ditambahkan !")


