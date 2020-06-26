def binToInt(binary):
    #konversi binary ke integer
    hasil = 0
    panjangBinary = len(binary)
    for i in range(0, panjangBinary):
        if(binary[i] == 1):
            #karena bit dibaca dari kanan ke kiri sehingga saat ke i, pangkatnya harus panjangBinary-i-1
            #hasil dari 2^(panjangBinary-i-1) sama saja dengan mengshiftkan bilangan 1 ke kiri sebanyak panjangBinary-i-1
            hasil += (1 << (panjangBinary-i-1))
    return hasil


def intToBin(angka):
    #konversi integer ke binary
    tmpHasil = []
    hasil = [] #array of bit
    while(angka != 0):
        if(angka%2 == 0): hasil += [0]
        else: hasil += [1]
        angka //= 2 #dibulatkan ke bawah
    #kumpulan bit tersebut dibalik, karena nilai bit harus membesar dari kanan ke kiri
    for i in range(len(hasil)-1, -1, -1):
        tmpHasil += [hasil[i]]
    return tmpHasil

def toBits(pesan):
    #konversi string ke kumpulan bit
    hasil = [] #array of bit
    for c in pesan:
        bits = intToBin(ord(c)) #ord(c) mengembalikan nilai ASCII huruf c
        hasil += [0] #paling kiri dari kumpulan bit haruslah 0
        for bit in bits: #copy isi dari bit dari bits
            hasil += [bit] 
    return hasil


#setiap elemennya berisi 32 bit pertama dari fractional part akar2 bil prima 2-19 (dalam hexadecimal)
nilaiInitHash = [0x6a09e667, 0xbb67ae85,
                    0x3c6ef372, 0xa54ff53a,
                    0x510e527f, 0x9b05688c,
                    0x1f83d9ab, 0x5be0cd19]

#setiap elemennya berisi 32 bit pertama dari fractional part akar3, 64 bilangan prima pertama (dalam hexadecimal)
nilaiK = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

#print(binToInt([1,0,1]))
