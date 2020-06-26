from util import * #import utility

def padding(pesan):
    #ubah pesan/password user ke suatu bit string kelipatan 512 bit
    
    #pertama, ubah dulu kumpulan huruf tersebut menjadi suatu kumpulan bit
    binPesan = toBits(pesan)
    
    l = len(binPesan) #simpan dulu panjang awal dari pesan
    #cari suatu bilangan k sehingga persamaan berikut terpenuhi : l+1+k ≅ -64 (mod 512)
    #sehingga panjang bitPesan jika dimodulo dengan 512 akan bersisa 64
    k = cariK(binPesan) 
    
    #isi kumpulan bit pesan dengan 1 lalu diikuti 0 sebanyak k
    binPesan += [1]
    for i in range(0, k):
        binPesan += [0]
    
    #karena panjang bitPesan kurang 64 agar menjadi kelipatan 512
    #kita tambahkan representasi bit dari l tapi dalam 64 bit 
    binaryL = intToBin(l) #representasi bit tanpa trailing zero di depannya
    panjangL = len(binaryL)
    tmpBinPesan = [] #menampung representasi bit dari l dalam 64 bit
    for i in range(0, 64-panjangL): #tambahkan 0 didepan binaryL agar pas 64 bit
        tmpBinPesan += [0]
    binPesan += tmpBinPesan+binaryL
    
    assert (len(binPesan)%512 == 0) #binPesan haruslah sudah berkelipatan 512 bit
    
    return binPesan

def parsing(binPesan): 
    #parse binPesan menjadi 512 bit per panjang dari binPesan
    #sehingga akan terbentuk array 2 dimensi yang setiap elemennya berjumlah 512
    size = 512
    blockList = [binPesan[i:i+size] for i in range(0,len(binPesan),size)] #array 2 dimensi
    return blockList
    
def cariK(bitList):
    panjang_bit = len(bitList) 
    k = 0
    #selama belum ada k yang memenuhi:
    #panjang_bits+1+k ≅ -64 (mod 512)
    #nilai k terus ditambah
    while((panjang_bit+1+k)%512 != 448):
        k+=1
    return k
#print(padding("123"))