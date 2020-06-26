import F00,F01

def lihatKritik():
        colIdWahana = 2
        colUsername = 0
        colTanggal = 1
        colKritik = 3
        Jumlah = F00.banyakParam(F01.dataKritikSaran)
        #Proses sorting dengan fungsi sortParam dari F00
        tmpDataKritik = F00.sortParam(F01.dataKritikSaran,colIdWahana+1,2,Jumlah,True)
        print("Kritik dan saran:")
        for idxDataKritikSaran in range(Jumlah-1): 
            print(tmpDataKritik[idxDataKritikSaran][colIdWahana]," | ",tmpDataKritik[idxDataKritikSaran][colTanggal]," | ",tmpDataKritik[idxDataKritikSaran][colUsername]," | ",tmpDataKritik[idxDataKritikSaran][colKritik])
