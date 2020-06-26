def ror(x, jumlahRotate): #Right rotate bit
    return (x >> jumlahRotate) | (x << (32-jumlahRotate)) & 0xFFFFFFFF

def rShift(x, jumlahShift): #right shift bit/penambahan 0 di sisi kiri bit
    return x >> jumlahShift

#rumus yang didefinisikan pada sha 256
def ch(x, y, z): return (x & y) ^ (~x & z)

def maj(x,y,z): return (x & y) ^ (x & z) ^ (y & z)

def sig_0(x):
    s2 = ror(x,2)
    s13 = ror(x,13)
    s22 = ror(x,22)
    
    return s2 ^ s13^ s22

def sig_1(x):
    s6 = ror(x,6)
    s11 = ror(x,11)
    s25 = ror(x, 25)
    
    return s6 ^ s11 ^ s25

def sub_0(x):
    s7 = ror(x, 7)
    s18 = ror(x,18)
    r3 = rShift(x, 3)
    
    return  s7 ^ s18 ^ r3

def sub_1(x):
    s17 = ror(x, 17)
    s19 = ror(x, 19)
    r10 = rShift(x, 10)
    
    return s17 ^ s19 ^ r10
    
