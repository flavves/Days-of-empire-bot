# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:09:53 2022

@author: okmen
"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal,Qt
import time
import datetime
import pyautogui
import win32api, win32con
import pyperclip
from PyQt5.QtGui import QPixmap
import os
global suresayac
import shutil
from PyQt5 import QtWidgets
#from giris_python import Ui_MainWindow
from hesapekle_python import Ui_MainWindow2
try:
    
    from botbaslat_ekran import MainWindow3
except:
    pass

class MainWindow2(QMainWindow):
        def __init__(self):
            super(MainWindow2, self).__init__()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi(self)
            self.botbaslat_EKRAN= MainWindow3()
            self.setWindowTitle("Days of Empire Bot hesap ekle")
            #self.hesapekle_EKRAN= Ui_MainWindow2()
            #self.botbaslat_EKRAN= Ui_MainWindow3()
            self.ui.save.clicked.connect(self.save)
            #self.ui.menuBot_Baslat.triggered.connect(self.menuBot_Baslat)
            #self.ui.menuBot_Baslat.addAction('Option #1', self.menuBot_Baslat)
            self.ui.toolBar.actionTriggered[QtWidgets.QAction].connect(self.menuBot_Baslat)
            #guncelleme icin 
            
            global kullanicilar 
            
            with open("kullanici.txt","r") as dosya:
                veriler=dosya.readline()
            dosya.close()
            
            ada=veriler.split("flavvesbatu")
            ada.pop(-1)
            ada_copy=veriler.split("flavvesbatu")
            ada_copy.pop(-1)
                    
            for i in range(0,len(ada)):
                    try:
                            
                        mail=ada[i].split(";")[0]
                        sifre=ada[i].split(";")[1]
                        #farm=ada[i].split(";")[2]
                        if len(mail)==0 or len(sifre)==0:
                            yeri=ada.index(ada[i])
                            ada_copy.pop(yeri) 
                    except:
                        pass
                        
            kullanicilar=ada_copy
           
            try:
                    
                (self.ui.email.setPlainText(kullanicilar[0].split(";")[0]))
                (self.ui.email_2.setPlainText(kullanicilar[1].split(";")[0]))
                (self.ui.email_3.setPlainText(kullanicilar[2].split(";")[0]))
                (self.ui.email_4.setPlainText(kullanicilar[3].split(";")[0]))
                (self.ui.email_5.setPlainText(kullanicilar[4].split(";")[0]))
                (self.ui.email_6.setPlainText(kullanicilar[5].split(";")[0]))
                (self.ui.email_7.setPlainText(kullanicilar[6].split(";")[0]))
                (self.ui.email_8.setPlainText(kullanicilar[7].split(";")[0]))
                (self.ui.email_9.setPlainText(kullanicilar[8].split(";")[0]))
                (self.ui.email_10.setPlainText(kullanicilar[9].split(";")[0]))
                (self.ui.email_11.setPlainText(kullanicilar[10].split(";")[0]))
                (self.ui.email_12.setPlainText(kullanicilar[11].split(";")[0]))
                (self.ui.email_13.setPlainText(kullanicilar[12].split(";")[0]))
                (self.ui.email_14.setPlainText(kullanicilar[13].split(";")[0]))
                (self.ui.email_15.setPlainText(kullanicilar[14].split(";")[0]))
                (self.ui.email_16.setPlainText(kullanicilar[15].split(";")[0]))
                (self.ui.email_17.setPlainText(kullanicilar[16].split(";")[0]))
                (self.ui.email_18.setPlainText(kullanicilar[17].split(";")[0]))
                (self.ui.email_19.setPlainText(kullanicilar[18].split(";")[0]))
                (self.ui.email_20.setPlainText(kullanicilar[19].split(";")[0]))
            except:
                pass
            
            try:
                    
                (self.ui.sifre.setPlainText(kullanicilar[0].split(";")[1]))
                (self.ui.sifre_2.setPlainText(kullanicilar[1].split(";")[1]))
                (self.ui.sifre_3.setPlainText(kullanicilar[2].split(";")[1]))
                (self.ui.sifre_4.setPlainText(kullanicilar[3].split(";")[1]))
                (self.ui.sifre_5.setPlainText(kullanicilar[4].split(";")[1]))
                (self.ui.sifre_6.setPlainText(kullanicilar[5].split(";")[1]))
                (self.ui.sifre_7.setPlainText(kullanicilar[6].split(";")[1]))
                (self.ui.sifre_8.setPlainText(kullanicilar[7].split(";")[1]))
                (self.ui.sifre_9.setPlainText(kullanicilar[8].split(";")[1]))
                (self.ui.sifre_10.setPlainText(kullanicilar[9].split(";")[1]))
                (self.ui.sifre_11.setPlainText(kullanicilar[10].split(";")[1]))
                (self.ui.sifre_12.setPlainText(kullanicilar[11].split(";")[1]))
                (self.ui.sifre_13.setPlainText(kullanicilar[12].split(";")[1]))
                (self.ui.sifre_14.setPlainText(kullanicilar[13].split(";")[1]))
                (self.ui.sifre_15.setPlainText(kullanicilar[14].split(";")[1]))
                (self.ui.sifre_16.setPlainText(kullanicilar[15].split(";")[1]))
                (self.ui.sifre_17.setPlainText(kullanicilar[16].split(";")[1]))
                (self.ui.sifre_18.setPlainText(kullanicilar[17].split(";")[1]))
                (self.ui.sifre_19.setPlainText(kullanicilar[18].split(";")[1]))
                (self.ui.sifre_20.setPlainText(kullanicilar[19].split(";")[1]))
            except:
                pass
        def menuBot_Baslat(self, selection):
            name = selection.text()
            if name=="Bot Başlat":
                self.botbaslat_EKRAN.show()
                self.close()
           
            
        def save(self):
            email=str(self.ui.email.toPlainText())
            email_2=str(self.ui.email_2.toPlainText())
            email_3=str(self.ui.email_3.toPlainText())
            email_4=str(self.ui.email_4.toPlainText())
            email_5=str(self.ui.email_5.toPlainText())
            email_6=str(self.ui.email_6.toPlainText())
            email_7=str(self.ui.email_7.toPlainText())
            email_8=str(self.ui.email_8.toPlainText())
            email_9=str(self.ui.email_9.toPlainText())
            email_10=str(self.ui.email_10.toPlainText())
            email_11=str(self.ui.email_11.toPlainText())
            email_12=str(self.ui.email_12.toPlainText())
            email_13=str(self.ui.email_13.toPlainText())
            email_14=str(self.ui.email_14.toPlainText())
            email_15=str(self.ui.email_15.toPlainText())
            email_16=str(self.ui.email_16.toPlainText())
            email_17=str(self.ui.email_17.toPlainText())
            email_18=str(self.ui.email_18.toPlainText())
            email_19=str(self.ui.email_19.toPlainText())
            email_20=str(self.ui.email_20.toPlainText())
            
            sifre=str(self.ui.sifre.toPlainText())
            sifre_2=str(self.ui.sifre_2.toPlainText())
            sifre_3=str(self.ui.sifre_3.toPlainText())
            sifre_4=str(self.ui.sifre_4.toPlainText())
            sifre_5=str(self.ui.sifre_5.toPlainText())
            sifre_6=str(self.ui.sifre_6.toPlainText())
            sifre_7=str(self.ui.sifre_7.toPlainText())
            sifre_8=str(self.ui.sifre_8.toPlainText())
            sifre_9=str(self.ui.sifre_9.toPlainText())
            sifre_10=str(self.ui.sifre_10.toPlainText())
            sifre_11=str(self.ui.sifre_11.toPlainText())
            sifre_12=str(self.ui.sifre_12.toPlainText())
            sifre_13=str(self.ui.sifre_13.toPlainText())
            sifre_14=str(self.ui.sifre_14.toPlainText())
            sifre_15=str(self.ui.sifre_15.toPlainText())
            sifre_16=str(self.ui.sifre_16.toPlainText())
            sifre_17=str(self.ui.sifre_17.toPlainText())
            sifre_18=str(self.ui.sifre_18.toPlainText())
            sifre_19=str(self.ui.sifre_19.toPlainText())
            sifre_20=str(self.ui.sifre_20.toPlainText())
            
            comboBox=" "
            
            
        
           

            with open("kullanici.txt","w") as dosya:
                dosya.write(email+";"+sifre+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_2+";"+sifre_2+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_3+";"+sifre_3+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_4+";"+sifre_4+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_5+";"+sifre_5+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_6+";"+sifre_6+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_7+";"+sifre_7+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_8+";"+sifre_8+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_9+";"+sifre_9+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_10+";"+sifre_10+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_11+";"+sifre_11+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_12+";"+sifre_12+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_13+";"+sifre_13+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_14+";"+sifre_14+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_15+";"+sifre_15+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_16+";"+sifre_16+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_17+";"+sifre_17+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_18+";"+sifre_18+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_19+";"+sifre_19+";"+comboBox+";")
                dosya.write('flavvesbatu')
                dosya.write(email_20+";"+sifre_20+";"+comboBox+";")
                dosya.write('flavvesbatu')
            dosya.close()
            
            global kullanicilar 
            
            with open("kullanici.txt","r") as dosya:
                veriler=dosya.readline()
            dosya.close()
            
            ada=veriler.split("flavvesbatu")
            ada.pop(-1)
            ada_copy=veriler.split("flavvesbatu")
            ada_copy.pop(-1)
                    
            for i in range(0,len(ada)):
                    try:
                            
                        mail=ada[i].split(";")[0]
                        sifre=ada[i].split(";")[1]
                        #farm=ada[i].split(";")[2]
                        if len(mail)==0 or len(sifre)==0:
                            yeri=ada.index(ada[i])
                            ada_copy.pop(yeri)         
                    except:
                        pass
            kullanicilar=ada_copy
            
            
            with open("kullanici-id-pass-farmturu.txt","w") as dosya:
                for kullanicilaryazma in kullanicilar:
                    ad=kullanicilaryazma.split(";")[0]
                    sifre=kullanicilaryazma.split(";")[1]
                    tur=kullanicilaryazma.split(";")[2]
                    
                    if tur == "0":
                        tur="tahil"
                    elif tur == "1":
                        tur="odun"
                    elif tur == "2":
                        tur="kuvars"
                    elif tur == "3":
                        tur="demir"
                    
                    dosya.write(ad+"\n"+sifre+"\n"+tur+"\n")
                
                
            
     
        
     
        
     
        
                        

if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow2()
        window.setWindowTitle("Days of Empire Bot hesap ekle")
        window.show()
    
        sys.exit(app.exec_())