#Implementasi SHA-256, Modifikasi dan Penjelasan dari Referensi
#referensi : https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
#            https://github.com/jasonzhou1/sha256/blob/master/hash.py

from util import *
from intUtil import *
from preprocessing import *
import copy

def updateRegisters(sha):
    #sebuah dictionary, kita pakai dictionary karena untuk menggantikan index 0- 7 yang akan terpakai
    reg = dict() 
    reg['a'] = sha[0]
    reg['b'] = sha[1]
    reg['c'] = sha[2]
    reg['d'] = sha[3]
    reg['e'] = sha[4]
    reg['f'] = sha[5]
    reg['g'] = sha[6]
    reg['h'] = sha[7]
    return reg

def expandBlocks(block):
    #inisialisasi wList/messange schedule
    #wList isinya 64 buah 32 bit integer
    wList = [0]*64
    
    #Pertama, bagi dulu 512 bit block menjadi 16 buah 32 bit chunk, yang akan menjadi nilai wList 0-15 (dalam integer)
    for t in range(0, 16):
        chunk = block[t*32:(t+1)*32]
        wList[t] = binToInt(chunk) 
    for t in range(16, 64):
        #proses wList 16-64 dengan rumus berikut yang bergantung kepada wList sebelumnya
        t1 = (sub_0(wList[t-15]) + wList[t-16]) & 0xFFFFFFFF #modulo dengan 2^32 agar tidak overflow dari 32 bit
        t2 = (t1 + wList[t-7]) & 0xFFFFFFFF
        t3 = (t2 + sub_1(wList[t-2])) & 0xFFFFFFFF
        wList[t] = t3
    return wList


def hashMyPassword(pesan):
    #Preprocessing
    binPesan = padding(pesan)
    #parse binPesan menjadi kelipatan 512, sehingga panjang blockList = len(binPesan)/512
    blockList = parsing(binPesan) #blockList merupakan array 2 dimensi
    #Main loop
    sha = copy.deepcopy(nilaiInitHash) #sha merupakan array yang berisi nilai hash dari pesan
    for i in range(len(blockList)):
        #reg awalnya berisi nilai hash awal/reg merupakan variabel temporary untuk hash
        reg = updateRegisters(sha)
        wList = expandBlocks(blockList[i]) #proses messange schedule blockList ke i
        #messange schedule 0-63 yang didapat diproses dengan rumus berikut
        #proses ini bergantung kepada nilai dari reg awal, lalu nilai reg setiap prosesnya di update
        for j in range(0,64):
            #& 0xFFFFFFFF sama dengan modulo 2^32
            CH = ch(reg['e'],reg['f'],reg['g'])
            MAJ = maj(reg['a'],reg['b'],reg['c'])
            sig0 = sig_0(reg['a'])
            sig1 = sig_1(reg['e'])
            WjKj = (nilaiK[j]+wList[j]) & 0xFFFFFFFF
            t1Tmp = (reg['h']+ WjKj + CH) & 0xFFFFFFFF
            T1 = (t1Tmp + sig1) & 0xFFFFFFFF
            T2 = (sig0 + MAJ) & 0xFFFFFFFF
            
            #update nilai reg dengan susunan berikut
            reg['h'] = reg['g']
            reg['g'] = reg['f']
            reg['f'] = reg['e']
            reg['e'] = (reg['d'] + T1) & 0xFFFFFFFF
            reg['d'] = reg['c']
            reg['c'] = reg['b']
            reg['b'] = reg['a']
            reg['a'] = (T1 + T2) & 0xFFFFFFFF
        
        #print(sha)
            
        
        #update nilai hash dengan rumus berikut, yang bergantung pada nilai reg
        sha[0] = (sha[0] + reg['a']) & 0xFFFFFFFF
        sha[1] = (sha[1] + reg['b']) & 0xFFFFFFFF
        sha[2] = (sha[2] + reg['c']) & 0xFFFFFFFF
        sha[3] = (sha[3] + reg['d']) & 0xFFFFFFFF
        sha[4] = (sha[4] + reg['e']) & 0xFFFFFFFF
        sha[5] = (sha[5] + reg['f']) & 0xFFFFFFFF
        sha[6] = (sha[6] + reg['g']) & 0xFFFFFFFF
        sha[7] = (sha[7] + reg['h']) & 0xFFFFFFFF
    #print(len(hex(sha[7])))
    #ubah integer pada hash ke hexadecimal, lalu append setiap nilainya sehingga menjadi string hexadecimal
    return makeDigest(sha) 

def makeDigest(sha):
    hash = ""
    for elm in sha:
        #ambil dari index kedua, karena hexadecimal pada sistem selalu diawali dengan 0x
        if(len(hex(elm)) < 10):
            hash += '0'
        hash += hex(elm)[2:] 
    return hash

#satu satunya cara verifikasi password adalah dengan menghash password inputan,
#lalu menyamakannya dengan hash password di database
def verifikasiPassword(storedPass, providedPass):
	passHash = hashMyPassword(providedPass)    
	return (passHash == storedPass)

#print(binToInt([1,0,1,1]))
#print(hashMyPassword("aaaaaaaaaaaaaaaa") == "0c0beacef8877bbf2416eb00f2b5dc96354e26dd1df5517320459b1236860f8c")