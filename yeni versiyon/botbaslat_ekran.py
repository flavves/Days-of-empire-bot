# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:05:29 2022

@author: okmen
"""

import mysql.connector
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
global suresayac
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal,Qt
import pyperclip
import pyautogui
import win32api, win32con
import time
import datetime
from botbaslat_python import Ui_MainWindow3
global suresayac
import shutil
suresayac=0


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    songiris = pyqtSignal(str)
    resimgonder = pyqtSignal(str)
    

    def run(self):
        """Long-running task."""

        kullanicisayisi=0
        girisyapilacakusernum=0
        
        
        def _workaround_write(text):
            """
            This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
            It copies the text to clipboard and pastes it, instead of typing it.
            """
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
            pyperclip.copy('')
        
        
        def click(x,y):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.3) #This pauses the script for 0.1 seconds
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            
            
            
            
            
            
            
        def Kullaniciadi_sifre_txt():
            # Using readlines()
            file1 = open('kullanici-id-pass-farmturu.txt', 'r')
            Lines = file1.readlines()
            kullaniciAdi=[]
            sifre=[]
            farmMetodu=[]
            count = 0
            # Strips the newline character
            for line in Lines:
                
                if count%3==0:
                    kullaniciAdi.append(line.strip())
                elif count%3==1:
                    sifre.append(line.strip())
                else :
                    farmMetodu.append(line.strip())
                count=count+1
                    
            return kullaniciAdi ,sifre,farmMetodu
        class Kullanici():
          def __init__(self, kullaniciAdi, sifre , farmMetodu):
            self.kullaniciAdi = kullaniciAdi
            self.sifre = sifre
            self.farmMetodu=farmMetodu
        
        def kullanicilari_yukle(kullanicisayisi):
        
            KullaniciAdi_SifreListesi=Kullaniciadi_sifre_txt()
            kullanicisayisi=len(KullaniciAdi_SifreListesi[0])
            #print(kullanicisayisi)
            kullanici=[0]*kullanicisayisi
            
            kullanicitimer=0
            while kullanicitimer<kullanicisayisi:#10 olacak
                kullanici[kullanicitimer]=Kullanici(KullaniciAdi_SifreListesi[0][kullanicitimer], KullaniciAdi_SifreListesi[1][kullanicitimer], KullaniciAdi_SifreListesi[2][kullanicitimer])
                kullanicitimer=kullanicitimer+1
                
            return kullanici
            
            
            
            
            
            
        def SeviyeKontrol():
            yenigirisyapildi=False
            seviye=pyautogui.locateOnScreen('inc/seviye6.png',confidence=0.98 ,grayscale = False)
            while seviye==None and yenigirisyapildi==False:
              

                click(1017,889)
                time.sleep(0.5)
                seviye=pyautogui.locateOnScreen('inc/seviye6.png',confidence=0.98 ,grayscale = False)
                yenigiris=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8)
                if yenigiris!=None:
                    yenigirisyapildi=True
        
        def BirlikKontrol(BirlikVar):
            birlik=pyautogui.locateOnScreen('inc/birlikyok.png',confidence=0.93 ,grayscale = True)
            if birlik!=None:
                click(695,89)
                BirlikVar=False
            else:
                click(1108, 992)
                BirlikVar=True
            return 
        
                
        def tahilCallBack():
        
            time.sleep(2)
            BirlikVar=True
            yenigiris=False
            while BirlikVar==True and yenigiris==False:
               
                
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    yenigiris=True
                    break
        
        
                
                time.sleep(0.7)
                aramabutonu=pyautogui.locateOnScreen('inc/aramabutonu.png',confidence=0.6)
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.7)
                    click(korx,kory)
                    time.sleep(0.7)
                    click(korx,kory)
                    
                    time.sleep(0.7)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789, 2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(1)
                    
        
                    tahilfoto=pyautogui.locateOnScreen('inc/tahilsecim.png',confidence=0.7)
                    if tahilfoto!=None:
                        x, y = pyautogui.center(tahilfoto)
                        click(x,y)
                        time.sleep(1.5)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1.5)
                        ses=pyautogui.locateOnScreen('inc/tahil.png',confidence=0.5)
                        if ses!=None:
                            x, y = pyautogui.center(ses)
                            click(x, y)
                            time.sleep(1.5)
                            isgalet=pyautogui.locateOnScreen('inc/isgalet.png',confidence=0.7)
                            if isgalet!=None:
                                click(x+137,y+35)
                                time.sleep(1.5)
                                
                                
                                MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                                if MaksimumSaldiriSiniri!=None:
                                    click(861,306)
                                    BirlikVar=False
                                    break
                                
                                
                                birlik=pyautogui.locateOnScreen('inc/birlikyok.png',confidence=0.93 ,grayscale = True)
                                if birlik!=None:
                                    click(695,89)
                                    BirlikVar=False
                                else:
                                    time.sleep(1)
                                    click(1108, 992)
                                    BirlikVar=True
                                    
                gerigelme=pyautogui.locateOnScreen('inc/gerigelmebutonu.png',confidence=0.8,grayscale=False)
                if aramabutonu==None and gerigelme!=None and yenigiris==False:
                        time.sleep(1)
                        click(699,90)
                    
                if aramabutonu==None and gerigelme==None and yenigiris==False:
                        time.sleep(1)
                        click(1094,863)
                        time.sleep(1)
                        click(699,90)
                time.sleep(1)
                    
                    
        def KuvarsCallBack():
        
            time.sleep(2)
            BirlikVar=True
            yenigiris=False
            while BirlikVar==True and yenigiris==False:
               
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                time.sleep(0.7)
                aramabutonu=pyautogui.locateOnScreen('inc/aramabutonu.png',confidence=0.6)
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.7)
                    click(korx,kory)
                    time.sleep(0.7)
                    click(korx,kory)
                    
                    time.sleep(0.7)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789, 2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(1.3)
                    kuvarsfoto=pyautogui.locateOnScreen('inc/kuvarssecim.png',confidence=0.7)
                    if kuvarsfoto!=None:
                        x, y = pyautogui.center(kuvarsfoto)
                        click(x,y)
                        time.sleep(1)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1.5)
                        ses=pyautogui.locateOnScreen('inc/kuvars.png',confidence=0.5)
                        if ses!=None:
                            x, y = pyautogui.center(ses)
                            click(x, y)
                            time.sleep(1.2)
                            isgalet=pyautogui.locateOnScreen('inc/isgalet.png',confidence=0.7)
                            if isgalet!=None:
                                click(x+137,y+35)
                                time.sleep(0.5)
                                
                                
                                MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                                if MaksimumSaldiriSiniri!=None:
                                    click(861,306)
                                    BirlikVar=False
                                    break
                                
                                
                                birlik=pyautogui.locateOnScreen('inc/birlikyok.png',confidence=0.93 ,grayscale = True)
                                if birlik!=None:
                                    click(695,89)
                                    BirlikVar=False
                                else:
                                    time.sleep(0.5)
                                    click(1108, 992)
                                    BirlikVar=True
                gerigelme=pyautogui.locateOnScreen('inc/gerigelmebutonu.png',confidence=0.8,grayscale=False)
                if aramabutonu==None and gerigelme!=None and yenigiris==False:
                        time.sleep(0.5)
                        click(699,90)
                    
                if aramabutonu==None and gerigelme==None and yenigiris==False:
                        time.sleep(1)
                        click(1094,863)
                        time.sleep(1)
                        click(699,90)
                time.sleep(1)
        def DemirCallBack():
        
            time.sleep(5)
            BirlikVar=True
            yenigiris=False
            while BirlikVar==True and yenigiris==False:
               
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                time.sleep(0.7)
                aramabutonu=pyautogui.locateOnScreen('inc/aramabutonu.png',confidence=0.6)
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.7)
                    click(korx,kory)
                    time.sleep(0.7)
                    click(korx,kory)
                    
                    time.sleep(0.7)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789,2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(1)
                    demirfoto=pyautogui.locateOnScreen('inc/demirsecim.png',confidence=0.7)
                    if demirfoto!=None:
                        x, y = pyautogui.center(demirfoto)
                        click(x,y)
                        time.sleep(1.5)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1.5)
                        ses=pyautogui.locateOnScreen('inc/demir.png',confidence=0.5)
                        if ses!=None:
                            x, y = pyautogui.center(ses)
                            click(x, y)
                            time.sleep(1.5)
                            isgalet=pyautogui.locateOnScreen('inc/isgalet.png',confidence=0.7)
                            if isgalet!=None:
                                click(x+137,y+35)
                                time.sleep(0.7)
                                
                                
                                MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                                if MaksimumSaldiriSiniri!=None:
                                    click(861,306)
                                    BirlikVar=False
                                    break
                                
                                
                                birlik=pyautogui.locateOnScreen('inc/birlikyok.png',confidence=0.93 ,grayscale = True)
                                if birlik!=None:
                                    click(695,89)
                                    BirlikVar=False
                                else:
                                    time.sleep(0.7)                    
                                    click(1108, 992)
                                    BirlikVar=True
                gerigelme=pyautogui.locateOnScreen('inc/gerigelmebutonu.png',confidence=0.8,grayscale=False)
                if aramabutonu==None and gerigelme!=None and yenigiris==False :
                        time.sleep(1)
                        click(699,90)
                    
                if aramabutonu==None and gerigelme==None and yenigiris==False:
                        time.sleep(1)
                        click(1094,863)
                        time.sleep(1)
                        click(699,90)
                time.sleep(1)
                
                
                
        def OdunCallBack():
        
            time.sleep(2)
            BirlikVar=True
            yenigiris=False
            while BirlikVar==True and yenigiris==False:
                
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    
                    yenigiris=True
                    break
        
                time.sleep(0.7)
                aramabutonu=pyautogui.locateOnScreen('inc/aramabutonu.png',confidence=0.6)
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.6)
                    click(korx,kory)
                    time.sleep(1)
                    click(korx,kory)
                    
                    time.sleep(1)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789, 2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(1)
                    odunfoto=pyautogui.locateOnScreen('inc/odunsecim.png',confidence=0.7)
                    if odunfoto!=None:
                        x, y = pyautogui.center(odunfoto)
                        click(x,y)
                        time.sleep(1)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1)
                        ses=pyautogui.locateOnScreen('inc/odun.png',confidence=0.5)
                        if ses!=None:
                            x, y = pyautogui.center(ses)
                            click(x, y)
                            time.sleep(1)
                            isgalet=pyautogui.locateOnScreen('inc/isgalet.png',confidence=0.7)
                            if isgalet!=None:
                                click(x+137,y+35)
                                time.sleep(1)
                                
                                
                                MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                                if MaksimumSaldiriSiniri!=None:
                                    click(861,306)
                                    BirlikVar=False
                                    break
                                
                                
                                birlik=pyautogui.locateOnScreen('inc/birlikyok.png',confidence=0.93 ,grayscale = True)
                                if birlik!=None:
                                    click(695,89)
                                    BirlikVar=False
                                else:
                                    time.sleep(1)
                                    click(1108, 992)
                                    BirlikVar=True
                gerigelme=pyautogui.locateOnScreen('inc/gerigelmebutonu.png',confidence=0.8,grayscale=False)
                if aramabutonu==None and gerigelme!=None and yenigiris==False :
                        time.sleep(1)
                        click(699,90)
                    
                if aramabutonu==None and gerigelme==None and yenigiris==False:
                        time.sleep(1)
                        click(1094,863)
                        time.sleep(1)
                        click(699,90)
                time.sleep(1)
                                
        def MadenArttirma():
            pyautogui.moveTo(954,850)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(660,0,2)
            pyautogui.mouseUp(button='left')
            time.sleep(1.5)
            click(836,615)
            time.sleep(1.5)
            click(814,739)
            time.sleep(1.5)
            
            click(1122,225)
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/Tamam.png',confidence=0.8 ,grayscale = False)
            if tamam!=None:
                click(1050,621)
            else:
                click(934,106)
            
            time.sleep(1)
            click(1137,325)
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/Tamam.png',confidence=0.8 ,grayscale = False)
            if tamam!=None:
                click(1050,621)
            else:
                click(934,106)
            time.sleep(1)
            
            
            click(1133,436)  
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/Tamam.png',confidence=0.8 ,grayscale = False)
            if tamam!=None:
                click(1050,621)
            else:
                click(934,106)
            time.sleep(1)
            
            
            click(1143,535)
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/Tamam.png',confidence=0.8 ,grayscale = False)
            if tamam!=None:
                click(1050,621)
            else:
                click(934,106)
            time.sleep(1)
            
            
            click(704,98)#Maden Arttırma Bitiş
        
        def kiliga():
            i=1
            click(1165,1000)
            time.sleep(1)
            click(803, 650)
            time.sleep(1)
            click(868,261)
            time.sleep(1)
            bagis=pyautogui.locateOnScreen('inc/bagis.png',confidence=0.75 ,grayscale = False)
            tamam2=pyautogui.locateOnScreen('inc/tamam2.png',confidence=0.6 ,grayscale = False)
            while bagis!=None and tamam2==None:
                    
                    bagis=pyautogui.locateOnScreen('inc/bagis.png',confidence=0.75 ,grayscale = False)
                    tamam2=pyautogui.locateOnScreen('inc/tamam2.png',confidence=0.6 ,grayscale = False)
                    click(1078, 730)
                    time.sleep(0.5)
        
        
                        
            time.sleep(1)
            click(945, 85)
            time.sleep(1)
            click(832,108)
            time.sleep(1)
            click(699,92)
            time.sleep(1)
            click(796,809)
            time.sleep(1)
            ucretsiz=pyautogui.locateOnScreen('inc/ucretsiz.png',confidence=0.8 ,grayscale = False)
            if ucretsiz!=None:
                click(1140,443)
                time.sleep(0.5)
                
                
                
                click(948,155)
                time.sleep(0.5)
                
                topla=pyautogui.locateOnScreen('inc/kiligatopla.png',confidence=0.8 ,grayscale = False)
                if topla!=None:
                    x, y = pyautogui.center(topla)
                    click(x, y)
                    time.sleep(1)
                time.sleep(1)
                
                kiligayardim=pyautogui.locateOnScreen('inc/yardim.png',confidence=0.8 ,grayscale = False)
                if kiligayardim!=None:
                    x1, y1 = pyautogui.center(kiligayardim)
                    click(x1, y1)
                    time.sleep(1)
                #time.sleep(1)
                
        
                time.sleep(1)
                click(1118, 151)
        
                topla2=pyautogui.locateOnScreen('inc/topla2.png',confidence=0.8 ,grayscale = False)
                if topla2!=None:
                    x2, y2 = pyautogui.center(topla2)
                    click(x2, y2)
                    time.sleep(1)
                time.sleep(0.5)
                
                topla2=pyautogui.locateOnScreen('inc/topla2.png',confidence=0.8 ,grayscale = False)
                if topla2!=None:
                    x2, y2 = pyautogui.center(topla2)
                    click(x2, y2)
                    time.sleep(0.75)
                time.sleep(0.5)
                
                kiligayardim2=pyautogui.locateOnScreen('inc/yardim.png',confidence=0.8 ,grayscale = False)
                if kiligayardim2!=None:
                    x3, y3 = pyautogui.center(kiligayardim2)
                    time.sleep(1)
                    click(x3,y3)
                time.sleep(1)
                
                time.sleep(1)
                click(698,89)
                time.sleep(0.8)
                click(698,89)
                
            else:
            
                click(948,155)
                time.sleep(0.5)
                
                
                topla3=pyautogui.locateOnScreen('inc/kiligatopla.png',confidence=0.8 ,grayscale = False)
                if topla3!=None:
                    x5, y5 = pyautogui.center(topla3)
                    click(x5,y5)
                    time.sleep(1)
                time.sleep(1)
                toplaa3=pyautogui.locateOnScreen('inc/kiligatopla.png',confidence=0.8 ,grayscale = False)
                if toplaa3!=None:
                    x5, y5 = pyautogui.center(toplaa3)
                    click(x5,y5)
                    time.sleep(1)
                time.sleep(1)
                kiligayardim3=pyautogui.locateOnScreen('inc/yardim.png',confidence=0.8 ,grayscale = False)
                if kiligayardim3!=None:
                    x6, y6 = pyautogui.center(kiligayardim3)
                    click(x6,y6)
                    time.sleep(1)
                time.sleep(1)
                
                time.sleep(1)
                click(1118, 151)
                time.sleep(1)
                
                
                time.sleep(1)
                topla4=pyautogui.locateOnScreen('inc/topla2.png',confidence=0.8 ,grayscale = False)
                if topla4!=None:
                    x7, y7 = pyautogui.center(topla4)
                    click(x7,y7)
                    time.sleep(1)
                time.sleep(1)
                topla4=pyautogui.locateOnScreen('inc/topla2.png',confidence=0.8 ,grayscale = False)
                if topla4!=None:
                    x7, y7 = pyautogui.center(topla4)
                    click(x7,y7)
                    time.sleep(1)
                    
                time.sleep(1)
                
                
                kiligayardim4=pyautogui.locateOnScreen('inc/yardim.png',confidence=0.8 ,grayscale = False)
                if kiligayardim4!=None:
                    x8, y8 = pyautogui.center(kiligayardim4)
                    click(x8,y8)
                    time.sleep(1)
                    
                time.sleep(1)
                
                time.sleep(1)
                click(698,89)
                time.sleep(1)
                
                click(806,869)
                time.sleep(1.2)
                hepsineyardimet=pyautogui.locateOnScreen('inc/hepsineyardimet.png',confidence=0.8 ,grayscale = False)
                if hepsineyardimet!=None:
                    hepsineyardimx, hepsineyardimy = pyautogui.center(hepsineyardimet)
                    click(hepsineyardimx,hepsineyardimy)
                    time.sleep(1)
                    click(698,89)
                
                time.sleep(1)
                click(698,89)
                
            
        def Kaleicitopla():
            time.sleep(1)
            click(1901,404)
            time.sleep(1)
            click(1901, 404)
            time.sleep(1)    
        def KiligaExtra():
            time.sleep(2)
            click(1174, 887)#düzen 1
            time.sleep(1)
            click(774,442)
            time.sleep(1)
            hasatet=pyautogui.locateOnScreen('inc/hasatet.png',confidence=0.8 ,grayscale = False)
            if hasatet!=None:
                 time.sleep(1)
                 x, y = pyautogui.center(hasatet)
                 click(x, y)
                 time.sleep(1)
                 click(920, 946)#aktif et
                 time.sleep(1)
                 click(942,858)#ortaya tıkla
                 time.sleep(1)
                 
            click(1174, 887)
            time.sleep(1)
            click(774,442)
            time.sleep(1)
            
            
            hizlitopla=pyautogui.locateOnScreen('inc/hizlitopla.png',confidence=0.8 ,grayscale = False)
            if hizlitopla!=None:
                 time.sleep(2.5)
                 x, y = pyautogui.center(hizlitopla)
                 click(x, y)
                 time.sleep(1)
                 click(920, 946)#aktif et
                 time.sleep(1)
                 click(942,858)#ortaya tıkla
                 time.sleep(1)
                 
        
            click(1174, 887)#düzen 1
            time.sleep(1)
            click(887, 438)#♥düzen 2
            time.sleep(1)
            
            hasatet2=pyautogui.locateOnScreen('inc/hasatet.png',confidence=0.8 ,grayscale = False)
            if hasatet2!=None:
                 time.sleep(1)
                 x, y = pyautogui.center(hasatet2)
                 click(x, y)
                 time.sleep(1)
                 click(920, 946)#aktif et
                 time.sleep(1)
                 click(942,858)#ortaya tıkla
                 time.sleep(1)
                
            click(1174, 887)#düzen 1
            time.sleep(1)
            click(887, 438)#♥düzen 2
            time.sleep(1)
            
            hizlitopla2=pyautogui.locateOnScreen('inc/hizlitopla.png',confidence=0.8 ,grayscale = False)
            if hizlitopla2!=None:
                 time.sleep(1)
                 x, y = pyautogui.center(hizlitopla2)
                 click(x, y)
                 time.sleep(1)
                 click(920, 946)#aktif et
                 time.sleep(1)
                 click(942,858)#ortaya tıkla
                 time.sleep(1)
            time.sleep(1)
            
            
            click(1174, 887)#düzen 1
            time.sleep(1)
            click(887, 438)#♥düzen 2
            time.sleep(1)
            click(997,437)#düzen3
            time.sleep(1)
            duzen3=pyautogui.locateOnScreen('inc/duzen3.png',confidence=0.8 ,grayscale = False)#iptal butonu
            if duzen3==None:
                hasatet2=pyautogui.locateOnScreen('inc/hasatet.png',confidence=0.8 ,grayscale = False)
                if hasatet2!=None:
                     time.sleep(1)
                     x, y = pyautogui.center(hasatet2)
                     click(x, y)
                     time.sleep(1)
                     click(920, 946)#aktif et
                     time.sleep(1)
                     click(942,858)#ortaya tıkla
                     time.sleep(1)
                    
                click(1174, 887)#düzen 1
                time.sleep(1)
                click(887, 438)#♥düzen 2
                time.sleep(1)
                
                hizlitopla2=pyautogui.locateOnScreen('inc/hizlitopla.png',confidence=0.8 ,grayscale = False)
                if hizlitopla2!=None:
                     time.sleep(1)
                     x, y = pyautogui.center(hizlitopla2)
                     click(x, y)
                     time.sleep(1)
                     click(920, 946)#aktif et
                     time.sleep(1)
                     click(942,858)#ortaya tıkla
                     time.sleep(1)
                time.sleep(1)
            else:
                x, y = pyautogui.center(duzen3)
                click(x, y)
                time.sleep(1)
                click(944,127)
                time.sleep(1)
                click(944,127)
                
            
            
            
            click(1174, 887)#düzen 1
            time.sleep(1.2)
            click(1050,379)
            time.sleep(2)
            tamponhasat=pyautogui.locateOnScreen('inc/tamponhasat.png',confidence=0.8 ,grayscale = False)
            if tamponhasat!=None:
                 time.sleep(1)
                 x, y = pyautogui.center(tamponhasat)
                 click(x, y)
                 time.sleep(1)
                 click(920, 946)#aktif et
                 time.sleep(1)
                 click(943, 144)#cıkıs
                 time.sleep(1)
            time.sleep(1)
            
            
                 
            click(943, 144)#cıkıs
            time.sleep(1)
                 
        
            time.sleep(2)
            
        
        def Harici():
            time.sleep(4)
            MadenArttirma()#ilk girilen değirmen
            time.sleep(2)
            Kaleicitopla()#ekranda toplama
            time.sleep(3)
            kiliga()#Lonca olayları
            time.sleep(1.2)
            KiligaExtra()#sonradan ekledik hizli arttırma falan
            time.sleep(1)
            click(939,1011)
            time.sleep(6)
            yenigiris=False
        
            while yenigiris==False:
                
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                kale=pyautogui.locateOnScreen('inc/kale.png',confidence=0.8 ,grayscale = False)
                if kale!=None:
                    click(936,574)#kendi kaleme tikla
                    time.sleep(1.5)
                    sehirbonusugiris=pyautogui.locateOnScreen('inc/sehirbonusugiris.png',confidence=0.8 ,grayscale = False)#sehir bonusu tıkla
                    if sehirbonusugiris!=None:#sehir bonusuna giris yapar
                        sehirx,sehiry=pyautogui.center(sehirbonusugiris)
                        click(sehirx,sehiry)
                        time.sleep(1)
                        pyautogui.moveTo(919,645)
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(919,189, 1)
                        pyautogui.mouseUp(button='left')
                        time.sleep(1.5)
                        bonus=pyautogui.locateOnScreen('inc/bonus.png',confidence=0.8 ,grayscale = False)
                        
                        
                        if bonus !=None:#bonusa girince sıkıntı yok
                                bonusx, bonusy = pyautogui.center(bonus)
                                click(bonusx, bonusy)
                                time.sleep(2)
                                time.sleep(1)
                                kullan=pyautogui.locateOnScreen('inc/kullan.png',confidence=0.8 ,grayscale = False)
                                if kullan !=None:
                                        kullanx, kullany = pyautogui.center(kullan)
                                        click(kullanx, kullany)
                                        time.sleep(1.5)
                                        click(924,172)
                                        time.sleep(1)
                                        click(694,92)
                                        time.sleep(1)
                    time.sleep(1.2)
                    click(694,92) 
                    break
                else:
                    
                    time.sleep(1.5)
                
            
        def Harici2():
            time.sleep(2)
            MadenArttirma()#ilk girilen değirmen
            time.sleep(1)
            Kaleicitopla()#ekranda toplama
            time.sleep(2)
            kiliga()#Lonca olayları
            time.sleep(3)
            KiligaExtra()#sonradan ekledik hizli arttırma falan
            time.sleep(2)
            click(939,1011)
            time.sleep(6)
            yenigiris=False
        
            while yenigiris==False:
               
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                kale=pyautogui.locateOnScreen('inc/kaleyegel.png',confidence=0.8 ,grayscale = False)
                if kale!=None:
                    click(936,574)#kendi kaleme tikla
                    time.sleep(3)
                    sehirbonusugiris=pyautogui.locateOnScreen('inc/sehirbonusugiris.png',confidence=0.8 ,grayscale = False)#sehir bonusu tıkla
                    if sehirbonusugiris!=None:#sehir bonusuna giris yapar
                        sehirx,sehiry=pyautogui.center(sehirbonusugiris)
                        click(sehirx,sehiry)
                        time.sleep(1.5)
                        pyautogui.moveTo(919,645)
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(919,189, 1)
                        pyautogui.mouseUp(button='left')
                        time.sleep(1.5)
                        bonus=pyautogui.locateOnScreen('inc/bonus.png',confidence=0.8 ,grayscale = False)
                        
                        
                        if bonus !=None:#bonusa girince sıkıntı yok
                                bonusx, bonusy = pyautogui.center(bonus)
                                click(bonusx, bonusy)
                                time.sleep(2)
                                time.sleep(1.5)
                                kullan=pyautogui.locateOnScreen('inc/kullan.png',confidence=0.8 ,grayscale = False)
                                if kullan !=None:
                                        kullanx, kullany = pyautogui.center(kullan)
                                        click(kullanx, kullany)
                                        time.sleep(1)
                                        click(924,172)
                                        time.sleep(1.2)
                                        click(694,92)
                                        time.sleep(1)
                    time.sleep(1.2)
                    click(694,92) 
                    break
                else:
                    
                    time.sleep(1.5)
        
            
        def KaleDegistir(girisyapilacakusernum,user):
            
            
            
            click(264,13)
            time.sleep(2)
            click(1121,88)
            time.sleep(1.5)
        
            
        
            while 1:
                
                oyunekran=pyautogui.locateOnScreen('inc/oyun.png',confidence=0.8 ,grayscale = False)
                if oyunekran !=None:
                    oyunx, oyuny = pyautogui.center(oyunekran)
                    click(oyunx, oyuny)
                    break
            #time.sleep(1)
        
            time.sleep(1)
            kullaniciadi=user[girisyapilacakusernum].kullaniciAdi
            time.sleep(1)
            sifre=user[girisyapilacakusernum].sifre
            time.sleep(1)
            
            yenigiris=False
            
        
            while yenigiris==False:
              
                anaekran=pyautogui.locateOnScreen('inc/anaekran.png',confidence=0.8 ,grayscale = False)
                if anaekran!=None:
                    break
                time.sleep(2)
                
                
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                time.sleep(1)
            
            time.sleep(2)
            oyunvip=pyautogui.locateOnScreen('inc/carpi.png',confidence=0.7 ,grayscale = False)
            if oyunvip !=None:
                    time.sleep(2)
                    click(1173,154)
                    time.sleep(1)
            time.sleep(2)
            postakutusu=pyautogui.locateOnScreen('inc/posta.png',confidence=0.6 ,grayscale = False)
            if postakutusu !=None:
                    time.sleep(2)
                    x, y = pyautogui.center(postakutusu)
                    time.sleep(1.2)
                    click(x,y)
            
           
            time.sleep(1.2)
            
            click(690,103)
            time.sleep(2)
            click(1169, 996)
            time.sleep(2)
            click(745, 228)
            time.sleep(2)
            click(946, 1012)
            time.sleep(2.2)
            click(867,247)
            time.sleep(2.2)
            _workaround_write(kullaniciadi)
            time.sleep(2.2)
            click(757,301)
            time.sleep(2)
            _workaround_write(sifre)  
            time.sleep(2.2)
            click(944,366)
            
            while yenigiris==False:
              
                anaekran=pyautogui.locateOnScreen('inc/anaekran.png',confidence=0.8 ,grayscale = False)
                if anaekran!=None:
                    break
                time.sleep(2)
                
                
                yenigirissekme=pyautogui.locateOnScreen('inc/yenigiris.png',confidence=0.8,grayscale=False)
                if yenigirissekme!=None:
                    yenigiris=True
                    break
            
            time.sleep(1)
            
            oyunvip=pyautogui.locateOnScreen('inc/carpi.png',confidence=0.7 ,grayscale = False)
            if oyunvip !=None:
                    time.sleep(2)
                    click(1173,154)
                    time.sleep(1)
            postakutusu=pyautogui.locateOnScreen('inc/posta.png',confidence=0.7 ,grayscale = False)
            if postakutusu !=None:
                    time.sleep(2)
                    x, y = pyautogui.center(postakutusu)
                    time.sleep(1.2)
                    click(x,y)
        

     
        
        def GorevBaslat(user):
            usernum=0
            with open("neredekaldi.txt","r") as dosya:
                usernum=int(dosya.readline())
            dosya.close()
            while True:
                
                        now_e = datetime.datetime.now()
                        raporicinsure = now_e.strftime("%H")
                        raporicinsure=int(raporicinsure)
                        if raporicinsure==0:
                            raporicinad = now_e.strftime("%d-%m-%Y %H-%M-%S")
                            #os.mkdir("raporlar/"+raporicinad)
                            try:
                                
                                shutil.copytree("ss", "raporlar/"+raporicinad)
                            except:
                                pass
                            
                        self.progress.emit(usernum+1)
                        
                        now = datetime.datetime.now()
                        dt_string = now.strftime("%H:%M")
                        self.songiris.emit(dt_string+";"+str(usernum+1))
                        
                        global suresayac
                        suresayac=int(datetime.datetime.now().minute)+10
                        if suresayac >= 60:
                            suresayac=suresayac-60
                            
                        KaleDegistir(usernum,user)
                        if user[usernum].farmMetodu=="tahil":
                            Harici()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                            tahilCallBack()
                        elif user[usernum].farmMetodu=="kuvars":
                            Harici()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                            KuvarsCallBack()
                        elif user[usernum].farmMetodu=="demir":
                            Harici()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                            DemirCallBack()
                        elif user[usernum].farmMetodu=="odun" :
                            Harici()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                            OdunCallBack()
                        time.sleep(1)
                        usernum=usernum+1
                        time.sleep(1)
                        if usernum==user.__len__():#10 yap
                            usernum=0
                            #(usernum)
        def GorevBaslat2(user):
            usernum=0
            with open("neredekaldi.txt","r") as dosya:
                usernum=int(dosya.readline())
            dosya.close()
            while True: 
                
                        now_e = datetime.datetime.now()
                        raporicinsure = now_e.strftime("%H")
                        raporicinsure=int(raporicinsure)
                        if raporicinsure==0:
                            raporicinad = now_e.strftime("%d-%m-%Y %H-%M-%S")
                            #os.mkdir("raporlar/"+raporicinad)
                            try:
                                
                                shutil.copytree("ss", "raporlar/"+raporicinad)
                            except:
                                pass
                            
                            
                            
                        self.progress.emit(usernum+1)
                        global suresayac
                        suresayac=int(datetime.datetime.now().minute)+10
                        if suresayac >= 60:
                            suresayac=suresayac-60
                        now = datetime.datetime.now()
                        dt_string = now.strftime("%H:%M")
                        self.songiris.emit(dt_string+";"+str(usernum+1))
                        
                        KaleDegistir(usernum,user)
                        
                        
                        if user[usernum].farmMetodu=="tahil":
                            Harici2()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                        elif user[usernum].farmMetodu=="kuvars":
                            Harici2()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                        elif user[usernum].farmMetodu=="demir":
                            Harici2()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                        elif user[usernum].farmMetodu=="odun" :
                            Harici2()
                            im = pyautogui.screenshot("ss/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("ss/"+str(usernum)+".png"+";"+str(usernum+1))
                        time.sleep(1)
                
                        usernum=usernum+1
                        time.sleep(1)
                        if usernum==user.__len__():#10 yap
                            usernum=0
         
        user=kullanicilari_yukle(kullanicisayisi)   
        #user[0].kullaniciAdi
        
        with open("farmturu1ve0.txt","r") as dosya:
                secim=dosya.readline()
        dosya.close()
        #self.progress.emit(3)
        
        if secim == "1": 
            print("Başladı 1")
            GorevBaslat(user)        
        elif secim == "2":    
            print("başladı 2")
            GorevBaslat2(user)
        
        
        
        self.finished.emit()

class MainWindow3(QMainWindow):
        def __init__(self):
            super(MainWindow3, self).__init__()
            self.ui = Ui_MainWindow3()
            self.ui.setupUi(self)
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.ui.farm1.clicked.connect(self.farm1)
            self.ui.farm2.clicked.connect(self.farm2)            
            self.ui.stop.clicked.connect(self.stop)
            
            
            try:
                for n in range(1,21):
                    
            
                    pixmap = QPixmap("ss/"+str(n-1))
                    
                    #pixmap=pixmap.scaled(235, 41)
                    if n == 1:   
                        self.ui.gold.setPixmap(pixmap)   
                    if n == 2:        
                        (self.ui.gold_2.setPixmap(pixmap)   )
                    elif n == 3:
                      (self.ui.gold_3.setPixmap(pixmap)   )
                    elif n == 4:
                      (self.ui.gold_4.setPixmap(pixmap)   )
                    elif n == 5:
                      (self.ui.gold_5.setPixmap(pixmap)   )
                    elif n == 6:
                      (self.ui.gold_6.setPixmap(pixmap)   )
                    elif n == 7:
                      (self.ui.gold_7.setPixmap(pixmap)   )
                    elif n == 8:
                      (self.ui.gold_8.setPixmap(pixmap)   )
                    elif n == 9:
                      (self.ui.gold_9.setPixmap(pixmap)   )
                    elif n == 10:
                      (self.ui.gold_10.setPixmap(pixmap)   )
                    elif n == 11:
                      (self.ui.gold_11.setPixmap(pixmap)   )
                    elif n == 12:
                      (self.ui.gold_12.setPixmap(pixmap)   )
                    elif n == 13:
                      (self.ui.gold_13.setPixmap(pixmap)   )
                    elif n == 14:
                      (self.ui.gold_14.setPixmap(pixmap)   )
                    elif n == 15:
                      (self.ui.gold_15.setPixmap(pixmap)   )
                    elif n == 16:
                      (self.ui.gold_16.setPixmap(pixmap)   )
                    elif n == 17:
                      (self.ui.gold_17.setPixmap(pixmap)   )
                    elif n == 18:
                      (self.ui.gold_18.setPixmap(pixmap)   )
                    elif n == 19:
                      (self.ui.gold_19.setPixmap(pixmap)   )
                    elif n == 20:
                      (self.ui.gold_20.setPixmap(pixmap)   )
            
            
            
            except:
                pass
            
            
            
            
            
            
        def stop(self):
            
            self.thread.terminate()         
            self.thread = None
            
        def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Question',
                "Are you sure you want to close the application?",
                 QMessageBox.Yes,
                 QMessageBox.No)
            if reply == QMessageBox.Yes:
                if self.thread:
                    self.thread.quit()
                del self.thread
                self.msg.close()
    
                super(MainWindow3, self).closeEvent(event)
            else:
                event.ignore()
        def reportProgress(self, n):
            with open("neredekaldi.txt","w") as dosya:
                dosya.write(str(n-1))
            dosya.close()
            print(f"Long-Running Step: {n}")
            if n == 1:   
                self.ui.sira.setStyleSheet('color: yellow')
            else: (self.ui.sira.setStyleSheet('color: green'))
            if n == 2:        
                (self.ui.sira_2.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_2.setStyleSheet('color: green'))
            if n == 3:
              (self.ui.sira_3.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_3.setStyleSheet('color: green'))
            if n == 4:
              (self.ui.sira_4.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_4.setStyleSheet('color: green'))
            if n == 5:
              (self.ui.sira_5.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_5.setStyleSheet('color: green'))
            if n == 6:
              (self.ui.sira_6.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_6.setStyleSheet('color: green'))
            if n == 7:
              (self.ui.sira_7.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_7.setStyleSheet('color: green'))
            if n == 8:
              (self.ui.sira_8.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_8.setStyleSheet('color: green'))
            if n == 9:
              (self.ui.sira_9.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_9.setStyleSheet('color: green'))
            if n == 10:
              (self.ui.sira_10.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_10.setStyleSheet('color: green'))
            if n == 11:
              (self.ui.sira_11.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_11.setStyleSheet('color: green'))
            if n == 12:
              (self.ui.sira_12.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_12.setStyleSheet('color: green'))
            if n == 13:
              (self.ui.sira_13.setStyleSheet('color: yellow'))
            else: (self.ui.sira_13.setStyleSheet('color: green'))
            if n == 14:
              (self.ui.sira_14.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_14.setStyleSheet('color: green'))
            if n == 15:
              (self.ui.sira_15.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_15.setStyleSheet('color: green'))
            if n == 16:
              (self.ui.sira_16.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_16.setStyleSheet('color: green'))
            if n == 17:
              (self.ui.sira_17.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_17.setStyleSheet('color: green'))
            if n == 18:
              (self.ui.sira_18.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_18.setStyleSheet('color: green'))
            if n == 19:
              (self.ui.sira_19.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_19.setStyleSheet('color: green'))
            if n == 20:
              (self.ui.sira_20.setStyleSheet('color: yellow')) 
            else: (self.ui.sira_20.setStyleSheet('color: green'))
        def songirisprogress(self,geldi):
            print(geldi)
            n=int(geldi.split(";")[1])
            
            if n == 1:   
                self.ui.lastlogin.setText(str(geldi.split(";")[0]))
            if n == 2:        
                (self.ui.lastlogin_2.setText(str(geldi.split(";")[0])))
            elif n == 3:
              (self.ui.lastlogin_3.setText(str(geldi.split(";")[0])))
            elif n == 4:
              (self.ui.lastlogin_4.setText(str(geldi.split(";")[0])))
            elif n == 5:
              (self.ui.lastlogin_5.setText(str(geldi.split(";")[0])))
            elif n == 6:
              (self.ui.lastlogin_6.setText(str(geldi.split(";")[0])))
            elif n == 7:
              (self.ui.lastlogin_7.setText(str(geldi.split(";")[0])))
            elif n == 8:
              (self.ui.lastlogin_8.setText(str(geldi.split(";")[0])))
            elif n == 9:
              (self.ui.lastlogin_9.setText(str(geldi.split(";")[0])))
            elif n == 10:
              (self.ui.lastlogin_10.setText(str(geldi.split(";")[0])))
            elif n == 11:
              (self.ui.lastlogin_11.setText(str(geldi.split(";")[0])))
            elif n == 12:
              (self.ui.lastlogin_12.setText(str(geldi.split(";")[0])))
            elif n == 13:
              (self.ui.lastlogin_13.setText(str(geldi.split(";")[0])))
            elif n == 14:
              (self.ui.lastlogin_14.setText(str(geldi.split(";")[0])))
            elif n == 15:
              (self.ui.lastlogin_15.setText(str(geldi.split(";")[0])))
            elif n == 16:
              (self.ui.lastlogin_16.setText(str(geldi.split(";")[0])))
            elif n == 17:
              (self.ui.lastlogin_17.setText(str(geldi.split(";")[0])))
            elif n == 18:
              (self.ui.lastlogin_18.setText(str(geldi.split(";")[0])))
            elif n == 19:
              (self.ui.lastlogin_19.setText(str(geldi.split(";")[0])))
            elif n == 20:
              (self.ui.lastlogin_20.setText(str(geldi.split(";")[0])))
        def resim(self,resimicin):
            n=int(resimicin.split(";")[1])
            
            pixmap = QPixmap(resimicin.split(";")[0])
            
            #pixmap=pixmap.scaled(235, 41)
            if n == 1:   
                self.ui.gold.setPixmap(pixmap)   
            if n == 2:        
                (self.ui.gold_2.setPixmap(pixmap)   )
            elif n == 3:
              (self.ui.gold_3.setPixmap(pixmap)   )
            elif n == 4:
              (self.ui.gold_4.setPixmap(pixmap)   )
            elif n == 5:
              (self.ui.gold_5.setPixmap(pixmap)   )
            elif n == 6:
              (self.ui.gold_6.setPixmap(pixmap)   )
            elif n == 7:
              (self.ui.gold_7.setPixmap(pixmap)   )
            elif n == 8:
              (self.ui.gold_8.setPixmap(pixmap)   )
            elif n == 9:
              (self.ui.gold_9.setPixmap(pixmap)   )
            elif n == 10:
              (self.ui.gold_10.setPixmap(pixmap)   )
            elif n == 11:
              (self.ui.gold_11.setPixmap(pixmap)   )
            elif n == 12:
              (self.ui.gold_12.setPixmap(pixmap)   )
            elif n == 13:
              (self.ui.gold_13.setPixmap(pixmap)   )
            elif n == 14:
              (self.ui.gold_14.setPixmap(pixmap)   )
            elif n == 15:
              (self.ui.gold_15.setPixmap(pixmap)   )
            elif n == 16:
              (self.ui.gold_16.setPixmap(pixmap)   )
            elif n == 17:
              (self.ui.gold_17.setPixmap(pixmap)   )
            elif n == 18:
              (self.ui.gold_18.setPixmap(pixmap)   )
            elif n == 19:
              (self.ui.gold_19.setPixmap(pixmap)   )
            elif n == 20:
              (self.ui.gold_20.setPixmap(pixmap)   )
            
            
            
            
        def farm2(self):
            
            comboBox=str(self.ui.comboBox.currentIndex())
            comboBox_2=str(self.ui.comboBox_2.currentIndex())
            comboBox_3=str(self.ui.comboBox_3.currentIndex())
            comboBox_4=str(self.ui.comboBox_4.currentIndex())
            comboBox_5=str(self.ui.comboBox_5.currentIndex())
            comboBox_6=str(self.ui.comboBox_6.currentIndex())
            comboBox_7=str(self.ui.comboBox_7.currentIndex())
            comboBox_8=str(self.ui.comboBox_8.currentIndex())
            comboBox_9=str(self.ui.comboBox_9.currentIndex())
            comboBox_10=str(self.ui.comboBox_10.currentIndex())
            comboBox_11=str(self.ui.comboBox_11.currentIndex())
            comboBox_12=str(self.ui.comboBox_12.currentIndex())
            comboBox_13=str(self.ui.comboBox_13.currentIndex())
            comboBox_14=str(self.ui.comboBox_14.currentIndex())
            comboBox_15=str(self.ui.comboBox_15.currentIndex())
            comboBox_16=str(self.ui.comboBox_16.currentIndex())
            comboBox_17=str(self.ui.comboBox_17.currentIndex())
            comboBox_18=str(self.ui.comboBox_18.currentIndex())
            comboBox_19=str(self.ui.comboBox_19.currentIndex())
            comboBox_20=str(self.ui.comboBox_20.currentIndex())
            
            global kullanicilar 
            
            with open("kullanici.txt","r") as dosya:
                veriler=dosya.readline()
            dosya.close()
            
            ada=veriler.split("flavvesbatu")
            ada.pop(-1)
            ada_copy=veriler.split("flavvesbatu")
            ada_copy.pop(-1)
            #commbobox atama
            

            #ada_copy[0]=ada_copy[0].replace(" ",comboBox)
            
            
            ada_copy[0]=ada_copy[0].replace(" ",comboBox)
            ada_copy[1]=ada_copy[1].replace(" ",comboBox_2)
            ada_copy[2]=ada_copy[2].replace(" ",comboBox_3)
            ada_copy[3]=ada_copy[3].replace(" ",comboBox_4)
            ada_copy[4]=ada_copy[4].replace(" ",comboBox_5)
            ada_copy[5]=ada_copy[5].replace(" ",comboBox_6)
            ada_copy[6]=ada_copy[6].replace(" ",comboBox_7)
            ada_copy[7]=ada_copy[7].replace(" ",comboBox_8)
            ada_copy[8]=ada_copy[8].replace(" ",comboBox_9)
            ada_copy[9]=ada_copy[9].replace(" ",comboBox_10)
            ada_copy[10]=ada_copy[10].replace(" ",comboBox_11)
            ada_copy[11]=ada_copy[11].replace(" ",comboBox_12)
            ada_copy[12]=ada_copy[12].replace(" ",comboBox_13)
            ada_copy[13]=ada_copy[13].replace(" ",comboBox_14)
            ada_copy[14]=ada_copy[14].replace(" ",comboBox_15)
            ada_copy[15]=ada_copy[15].replace(" ",comboBox_16)
            ada_copy[16]=ada_copy[16].replace(" ",comboBox_17)
            ada_copy[17]=ada_copy[17].replace(" ",comboBox_18)
            ada_copy[18]=ada_copy[18].replace(" ",comboBox_19)
            ada_copy[19]=ada_copy[19].replace(" ",comboBox_20)
            
            
            
            
            
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
            #comboboxtan gelen veriyi al bitir şimdilik.
            print(kullanicilar)
            
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
                    
                    
            #bot başlatma ekranı
         
            with open("farmturu1ve0.txt","w") as dosya:
                dosya.write("2")
            dosya.close()
            
            
            # Step 2: Create a QThread object
            self.thread = QThread()
            # Step 3: Create a worker object
            self.worker = Worker()
            # Step 4: Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Step 5: Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.reportProgress)
            self.worker.songiris.connect(self.songirisprogress)
            self.worker.resimgonder.connect(self.resim)
            # Step 6: Start the thread
            self.thread.start()
    
            # Final resets
            #self.ui.farm2.setEnabled(False)
            self.thread.finished.connect(
                lambda: print("bitti2")
            )
   
        
        

        def farm1(self):
            


            comboBox=str(self.ui.comboBox.currentIndex())
            comboBox_2=str(self.ui.comboBox_2.currentIndex())
            comboBox_3=str(self.ui.comboBox_3.currentIndex())
            comboBox_4=str(self.ui.comboBox_4.currentIndex())
            comboBox_5=str(self.ui.comboBox_5.currentIndex())
            comboBox_6=str(self.ui.comboBox_6.currentIndex())
            comboBox_7=str(self.ui.comboBox_7.currentIndex())
            comboBox_8=str(self.ui.comboBox_8.currentIndex())
            comboBox_9=str(self.ui.comboBox_9.currentIndex())
            comboBox_10=str(self.ui.comboBox_10.currentIndex())
            comboBox_11=str(self.ui.comboBox_11.currentIndex())
            comboBox_12=str(self.ui.comboBox_12.currentIndex())
            comboBox_13=str(self.ui.comboBox_13.currentIndex())
            comboBox_14=str(self.ui.comboBox_14.currentIndex())
            comboBox_15=str(self.ui.comboBox_15.currentIndex())
            comboBox_16=str(self.ui.comboBox_16.currentIndex())
            comboBox_17=str(self.ui.comboBox_17.currentIndex())
            comboBox_18=str(self.ui.comboBox_18.currentIndex())
            comboBox_19=str(self.ui.comboBox_19.currentIndex())
            comboBox_20=str(self.ui.comboBox_20.currentIndex())
            
            global kullanicilar 
            
            with open("kullanici.txt","r") as dosya:
                veriler=dosya.readline()
            dosya.close()
            
            ada=veriler.split("flavvesbatu")
            ada.pop(-1)
            ada_copy=veriler.split("flavvesbatu")
            ada_copy.pop(-1)
            #commbobox atama
            

            #ada_copy[0]=ada_copy[0].replace(" ",comboBox)
            
            
            ada_copy[0]=ada_copy[0].replace(" ",comboBox)
            ada_copy[1]=ada_copy[1].replace(" ",comboBox_2)
            ada_copy[2]=ada_copy[2].replace(" ",comboBox_3)
            ada_copy[3]=ada_copy[3].replace(" ",comboBox_4)
            ada_copy[4]=ada_copy[4].replace(" ",comboBox_5)
            ada_copy[5]=ada_copy[5].replace(" ",comboBox_6)
            ada_copy[6]=ada_copy[6].replace(" ",comboBox_7)
            ada_copy[7]=ada_copy[7].replace(" ",comboBox_8)
            ada_copy[8]=ada_copy[8].replace(" ",comboBox_9)
            ada_copy[9]=ada_copy[9].replace(" ",comboBox_10)
            ada_copy[10]=ada_copy[10].replace(" ",comboBox_11)
            ada_copy[11]=ada_copy[11].replace(" ",comboBox_12)
            ada_copy[12]=ada_copy[12].replace(" ",comboBox_13)
            ada_copy[13]=ada_copy[13].replace(" ",comboBox_14)
            ada_copy[14]=ada_copy[14].replace(" ",comboBox_15)
            ada_copy[15]=ada_copy[15].replace(" ",comboBox_16)
            ada_copy[16]=ada_copy[16].replace(" ",comboBox_17)
            ada_copy[17]=ada_copy[17].replace(" ",comboBox_18)
            ada_copy[18]=ada_copy[18].replace(" ",comboBox_19)
            ada_copy[19]=ada_copy[19].replace(" ",comboBox_20)
            
            
            
            
            
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
            #comboboxtan gelen veriyi al bitir şimdilik.
            print(kullanicilar)
            
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
            #bot başlatma ekranı
            with open("farmturu1ve0.txt","w") as dosya:
                dosya.write("1")
            dosya.close()
            
            # Step 2: Create a QThread object
            self.thread = QThread()
            # Step 3: Create a worker object
            self.worker = Worker()
            # Step 4: Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Step 5: Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.reportProgress)
            self.worker.songiris.connect(self.songirisprogress)
            self.worker.resimgonder.connect(self.resim)
            # Step 6: Start the thread
            self.thread.start()
    
            # Final resets
            #self.ui.farm1.setEnabled(False)
            self.thread.finished.connect(
                lambda: print("bitti")
            )

            
            
                
       


if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow3()
        window.setWindowTitle("Days of Empire Bot")
        window.show()

        sys.exit(app.exec_())
        





