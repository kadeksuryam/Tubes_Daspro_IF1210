import F00,F01,F02,F03,F04,F05,F06,F07,F08,F09,F10,F11,F12,F13,F14,F15,B02,B03,B04

print("Selamat Datang, Silahkan Load File dan Login Terlebih Dahulu!")
print("Ketikkan perintah sesuai dengan perintah yang terdaftar di file main.py secara benar!")
isExit = False
while(isExit == False):
    perintah = input()
    if(F02.isLogin == True):
        if(perintah == "save"):
            F03.saveFile()
        elif(perintah == "signup"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                F04.signup()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "caripemain"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                F05.pencarianPemain()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "cariwahana"):
            F06.pencarianWahana()
        elif(perintah == "belitiket"):
            F07.beliTiket()
        elif(perintah == "pakaitiket"):
            F08.pakaiTiket()
        elif(perintah == "refund"):
            F09.refund()
        elif(perintah == "isikritik"):
            F10.kritikDanSaran()
        elif(perintah == "lihatkritik"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                F11.lihatKritik()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "tambahwahana"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                F12.tambahWahana()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "topup"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                F13.topup()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "riwayatwahana"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                F14.riwayat_wahana()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "tiketpemain"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                F15.cariTiket()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "tikethilang"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                B04.laporanTiketHilang()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "upgradeakun"):
            if(F00.cariRoleUser(F02.usernameLogin) == "admin"):
                B02.goldenAccount()
            else:
                print('Hanya admin yang dapat melakukan perintah ' + perintah +'!')
        elif(perintah == "bestwahana"):
            B03.bestWahana()
        elif(perintah == "exit"):
            pil = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
            if(pil == "Y"):
                isExit = True
                F03.saveFile()
                F04.isLogin = False 
            elif(pil == "N"):
                isExit = True
                F04.isLogin = False
    else:
        if(perintah == "load"):
            F01.loadFile()
        elif(perintah == "login"):
            F02.login()
        else:
            ("Anda harus login terlebih dahulu untuk mendapatkan fitur tersebut!")
      
    
