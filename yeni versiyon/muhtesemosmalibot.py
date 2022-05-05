# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:54:45 2022

@author: okmen
"""
import mysql.connector
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
global suresayac



from giris_python import Ui_MainWindow
from hesapekle_ekran import MainWindow2
#from botbaslat_python import Ui_MainWindow3
suresayac=0

global kullaniciusername
kullaniciusername=""
class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.hesapekle_EKRAN= MainWindow2()
            #self.botbaslat_EKRAN= Ui_MainWindow3()
            self.ui.girisbuton.clicked.connect(self.girisbuton)
            
            #logo ekleme
            
            pixmap = QPixmap("logo.png")
            pixmap=pixmap.scaled(240, 240)
            self.ui.logo.setPixmap(pixmap)
            global girisonay
            girisonay=False
        
        
        
        global giris
        def giris():
            global kullaniciusername,kullanicisifre,kacgunkaldi,girisonay
            global kacgunkaldi
            try:
                mydb = mysql.connector.connect(
                  host="193.36.63.250",
                  user="admin",
                  password="8[#w*mh0&K]q",
                  database="bot"
                )
        
            except:
                print("Db baglantisi yok")
                
            mycursor = mydb.cursor()
        
            sorgu="SELECT * FROM kullanici WHERE username ="+kullaniciusername+" AND sifre =" + kullanicisifre
            
            
            mycursor.execute(sorgu)
            
            myresult = mycursor.fetchall()
            
            if len(myresult)>0:
        
                kacgunkaldi=(myresult[0][3]-myresult[0][4]).days
                if kacgunkaldi > 0 and myresult[0][5]!=1:
                    print("giris basarili")
                    girisonay=True
                else:
                    if kacgunkaldi<0:
                        print("Süre Bitti")
                    else:
                        print("Baska Bilgisayarda Calisiyor")
            else:
                print("böyle bir kullanici yok")
            
        
        
        
        def girisbuton(self):
            global kullaniciusername,kullanicisifre,kacgunkaldi,girisonay
            kullaniciusername=str(self.ui.email.toPlainText())
            kullanicisifre=str(self.ui.sifre.toPlainText())
            #kullaniciusername="'admin'"
            #kullanicisifre="'password'"
            giris()
            if girisonay==True:
                def programCalistirildi():
                    try:
                        mydb = mysql.connector.connect(
                          host="193.36.63.250",
                          user="admin",
                          password="8[#w*mh0&K]q",
                          database="bot"
                        )
                
                    except:
                        print("Db baglantisi yok")
                    mycursor = mydb.cursor()
                    mycursor.execute("UPDATE kullanici SET calisiyor = '1' WHERE kullanici.username ="+kullaniciusername)
                    mydb.commit()
                #programCalistirildi()
                self.hesapekle_EKRAN.show()
                self.close()
            else:
                pass
                
                  

if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("Days of Empire Bot")
        window.show()

        sys.exit(app.exec_())
        












































