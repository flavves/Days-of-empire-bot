import sys
import time
from botbaslat_python import Ui_MainWindow3
import mysql.connector
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QMessageBox
global suresayac
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal,Qt
import pyperclip
import pyautogui
import win32api, win32con
import datetime
from hesapekle_python import Ui_MainWindow2
from giris_python import Ui_MainWindow
global suresayac
import shutil
import threading

global usernum,user
user=""
suresayac=0
usernum=0
seviyebes = 0

class AThread(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    songiris = pyqtSignal(str)
    resimgonder = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        """Long-running task."""

        kullanicisayisi=0
        girisyapilacakusernum=0
        
        def sureondkkontrol():
            global usernum,user,enbas
            with open("inc/src/timer2.txt","r") as dosya:
                suresayac=int(dosya.readline())
            dosya.close()
            suresayac_kontrol=int(datetime.datetime.now().minute)
            if suresayac_kontrol >= suresayac:
                """
                usernum=usernum+1
                if usernum>=user.__len__():#10 yap
                    +=0
                with open("inc/src/timer1.txt","w") as dosya:
                            dosya.write(str(usernum))
                dosya.close()
                enbas()
                """
                #print("süreyi aştılar")
                pass
            
        
        
        def _workaround_write(text):
            """
            This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
            It copies the text to clipboard and pastes it, instead of typing it.
            """
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
            pyperclip.copy('')
        def click3(x,y):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.5) #This pauses the script for 0.1 seconds
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
        
        def click(x,y):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.3) #This pauses the script for 0.1 seconds
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        def click2(x,y):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.1) #This pauses the script for 0.1 seconds
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            
            
            
            
            
            
            
        def Kullaniciadi_sifre_txt():
            # Using readlines()
            file1 = open('inc/src/userFmethod.txt', 'r')
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
                sureondkkontrol()
                kullanici[kullanicitimer]=Kullanici(KullaniciAdi_SifreListesi[0][kullanicitimer], KullaniciAdi_SifreListesi[1][kullanicitimer], KullaniciAdi_SifreListesi[2][kullanicitimer])
                kullanicitimer=kullanicitimer+1
                
            return kullanici
            
            
            
            
            
            
        def SeviyeKontrol():
                global seviyebes
                if seviyebes==1:
                    click(1099,899)
                    time.sleep(0.2)
                    click(1019,886)
                    time.sleep(0.2)
                    click(1095,893)
                    time.sleep(0.2)
                    click(1095,893)
                    time.sleep(0.2)
                    pyautogui.press('del')
                    time.sleep(0.2)
                    pyautogui.press('6')
                    seviyebes=seviyebes+1
                elif seviyebes<9:
                    seviyebes=seviyebes+1
                elif seviyebes==9:
                    click(1099,899)
                    time.sleep(0.2)
                    click(1019,886)
                    time.sleep(0.2)
                    click(1095,893)
                    time.sleep(0.2)
                    click(1095,893)
                    time.sleep(0.2)
                    pyautogui.press('del')
                    time.sleep(0.2)
                    pyautogui.press('5')
                    seviyebes=seviyebes+1
                else:
                    seviyebes=seviyebes+1
                    if seviyebes==18:
                        seviyebes=1
                    
        
        def BirlikKontrol(BirlikVar):
            birlik=pyautogui.locateOnScreen('inc/img/birlikyok.png',confidence=0.93 ,grayscale = True)
            sureondkkontrol()
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
                sureondkkontrol()
                
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    yenigiris=True
                    break
        
        
                
                time.sleep(0.7)
                aramabutonu=pyautogui.locateOnScreen('inc/img/aramabutonu.png',confidence=0.6)
                sureondkkontrol()
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.7)
                    click(korx,kory)
                    time.sleep(0.7)
                    click(korx,kory)
                    
                    time.sleep(0.7)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789, 0.2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(0.5)
                    
        
                    tahilfoto=pyautogui.locateOnScreen('inc/img/tahilsecim.png',confidence=0.7)
                    
                    if tahilfoto!=None:
                        x, y = pyautogui.center(tahilfoto)
                        click(x,y)
                        time.sleep(1.5)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1)
                        click(948,534)
                        time.sleep(0.3)
                        
                        isgalet=pyautogui.locateOnScreen('inc/img/isgalet.png',confidence=0.58)
                        if isgalet!=None:
                            click(1059,563)
                            time.sleep(0.8)
                            MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/img/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                            if MaksimumSaldiriSiniri!=None:
                                click(861,306)
                                BirlikVar=False
                                break
                            
                            
                            birlik=pyautogui.locateOnScreen('inc/img/birlikyok.png',confidence=0.93 ,grayscale = True)
                            if birlik!=None:
                                click(695,89)
                                BirlikVar=False
                            else:
                                time.sleep(1)
                                click(1108, 992)
                                BirlikVar=True
                                    
                gerigelme=pyautogui.locateOnScreen('inc/img/gerigelmebutonu.png',confidence=0.8,grayscale=False)

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

            #ime.sleep(2)
            BirlikVar=True
            yenigiris=False
            while BirlikVar==True and yenigiris==False:
                sureondkkontrol()
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                time.sleep(0.4)
                aramabutonu=pyautogui.locateOnScreen('inc/img/aramabutonu.png',confidence=0.6)
                sureondkkontrol()
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.5)
                    click(korx,kory)
                    time.sleep(0.5)
                    click(korx,kory)
                    
                    time.sleep(0.5)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789, 0.2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(0.5)
                    kuvarsfoto=pyautogui.locateOnScreen('inc/img/kuvarssecim.png',confidence=0.7)
   
                    if kuvarsfoto!=None:
                        x, y = pyautogui.center(kuvarsfoto)
                        click(x,y)
                        time.sleep(0.7)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1)
                        click(948,534)
          
                        time.sleep(0.7)
                        
                        isgalet=pyautogui.locateOnScreen('inc/img/isgalet.png',confidence=0.7)
                        if isgalet!=None:
                            click(1059,563)
                            time.sleep(0.8)
                            MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/img/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                            if MaksimumSaldiriSiniri!=None:
                                click(861,306)
                                BirlikVar=False
                                break
                            
                            
                            birlik=pyautogui.locateOnScreen('inc/img/birlikyok.png',confidence=0.93 ,grayscale = True)
                            if birlik!=None:
                                click(695,89)
                                BirlikVar=False
                            else:
                                time.sleep(1)
                                click(1108, 992)
                                BirlikVar=True
                                
                gerigelme=pyautogui.locateOnScreen('inc/img/gerigelmebutonu.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
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
                sureondkkontrol()
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                time.sleep(0.7)
                aramabutonu=pyautogui.locateOnScreen('inc/img/aramabutonu.png',confidence=0.6)
                sureondkkontrol()
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.7)
                    click(korx,kory)
                    time.sleep(0.7)
                    click(korx,kory)
                    
                    time.sleep(0.7)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789,0.2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(0.5)
                    demirfoto=pyautogui.locateOnScreen('inc/img/demirsecim.png',confidence=0.7)
                    sureondkkontrol()
                    if demirfoto!=None:
                        x, y = pyautogui.center(demirfoto)
                        click(x,y)
                        time.sleep(1.5)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1.5)
                        click(948,534)
                        time.sleep(0.7)
                        
                        isgalet=pyautogui.locateOnScreen('inc/img/isgalet.png',confidence=0.7)
                        if isgalet!=None:
                            click(1059,563)
                            time.sleep(0.8)
                            MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/img/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                            if MaksimumSaldiriSiniri!=None:
                                click(861,306)
                                BirlikVar=False
                                break
                            
                            
                            birlik=pyautogui.locateOnScreen('inc/img/birlikyok.png',confidence=0.93 ,grayscale = True)
                            if birlik!=None:
                                click(695,89)
                                BirlikVar=False
                            else:
                                time.sleep(1)
                                click(1108, 992)
                                BirlikVar=True
                gerigelme=pyautogui.locateOnScreen('inc/img/gerigelmebutonu.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
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
                sureondkkontrol()
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    
                    yenigiris=True
                    break
        
                time.sleep(0.7)
                aramabutonu=pyautogui.locateOnScreen('inc/img/aramabutonu.png',confidence=0.6)
                sureondkkontrol()
                if aramabutonu!=None:
                    korx, kory = pyautogui.center(aramabutonu)
                    time.sleep(0.6)
                    click(korx,kory)
                    time.sleep(1)
                    click(korx,kory)
                    
                    time.sleep(1)    
                    pyautogui.moveTo(968,799)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(768,789, 0.2)
                    pyautogui.mouseUp(button='left')
                    time.sleep(0.5)
                    odunfoto=pyautogui.locateOnScreen('inc/img/odunsecim.png',confidence=0.7)
                    sureondkkontrol()
                    if odunfoto!=None:
                        x, y = pyautogui.center(odunfoto)
                        click(x,y)
                        time.sleep(1)
                        SeviyeKontrol()
                        click(946,992)
                        time.sleep(1)
                        click(948,534)
                        time.sleep(0.7)
                        
                        isgalet=pyautogui.locateOnScreen('inc/img/isgalet.png',confidence=0.7)
                        if isgalet!=None:
                            click(1059,563)
                            time.sleep(0.8)
                            MaksimumSaldiriSiniri=pyautogui.locateOnScreen('inc/img/saldirisiniri.png',confidence=0.73 ,grayscale = False)
                            if MaksimumSaldiriSiniri!=None:
                                click(861,306)
                                BirlikVar=False
                                break
                            
                            
                            birlik=pyautogui.locateOnScreen('inc/img/birlikyok.png',confidence=0.93 ,grayscale = True)
                            if birlik!=None:
                                click(695,89)
                                BirlikVar=False
                            else:
                                time.sleep(1)
                                click(1108, 992)
                                BirlikVar=True
                gerigelme=pyautogui.locateOnScreen('inc/img/gerigelmebutonu.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
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
            pyautogui.moveTo(660,0,1)
            pyautogui.mouseUp(button='left')
            time.sleep(1.5)
            click(836,615)
            time.sleep(1.5)
            click(814,739)
            time.sleep(1.5)
            
            click(1122,225)
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/img/Tamam.png',confidence=0.8 ,grayscale = False)
            sureondkkontrol()
            if tamam!=None:
                click(1050,621)
            else:
                click(934,106)
            
            time.sleep(1)
            click(1137,325)
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/img/Tamam.png',confidence=0.8 ,grayscale = False)
            sureondkkontrol()
            if tamam!=None:
                click(1050,621)
            else:
                click(934,106)
            time.sleep(1)
            
            
            click(1133,436)  
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/img/Tamam.png',confidence=0.8 ,grayscale = False)
            sureondkkontrol()
            if tamam!=None:
                click(1050,621)
            else:
                click(934,106)
            time.sleep(1)
            
            
            click(1143,535)
            time.sleep(1)
            tamam=pyautogui.locateOnScreen('inc/img/Tamam.png',confidence=0.8 ,grayscale = False)
            sureondkkontrol()
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
            #bagis=pyautogui.locateOnScreen('inc/img/bagis.png',confidence=0.75 ,grayscale = False)
            tamam2=pyautogui.locateOnScreen('inc/img/tamam2.png',confidence=0.95 ,grayscale = False)
            while tamam2==None:
                    
                    #bagis=pyautogui.locateOnScreen('inc/img/bagis.png',confidence=0.75 ,grayscale = False)
                    time.sleep(0.1)
                    tamam2=pyautogui.locateOnScreen('inc/img/tamam2.png',confidence=0.9 ,grayscale = False)
                    
                    click2(1078, 730)
                    time.sleep(0.1)
        
        
                        
            time.sleep(1)
            click(945, 85)
            time.sleep(1)
            click(832,108)
            time.sleep(1)
            click(699,92)
            time.sleep(1)
            click(796,809)
            time.sleep(1)
            ucretsiz=pyautogui.locateOnScreen('inc/img/ucretsiz.png',confidence=0.8 ,grayscale = False)
            sureondkkontrol()
            if ucretsiz!=None:
                click(1140,443)
                time.sleep(0.5)
                
                
                
                click(948,155)
                time.sleep(0.5)
                
                topla=pyautogui.locateOnScreen('inc/img/kiligatopla.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if topla!=None:
                    x, y = pyautogui.center(topla)
                    click(x, y)
                    time.sleep(1)
                time.sleep(1)
                
                kiligayardim=pyautogui.locateOnScreen('inc/img/yardim.png',confidence=0.8 ,grayscale = False)
                if kiligayardim!=None:
                    x1, y1 = pyautogui.center(kiligayardim)
                    click(x1, y1)
                    time.sleep(1)
                #time.sleep(1)
                
        
                time.sleep(1)
                click(1118, 151)
        
                topla2=pyautogui.locateOnScreen('inc/img/topla2.png',confidence=0.8 ,grayscale = False)
                if topla2!=None:
                    x2, y2 = pyautogui.center(topla2)
                    click(x2, y2)
                    time.sleep(1)
                time.sleep(0.5)
                
                topla2=pyautogui.locateOnScreen('inc/img/topla2.png',confidence=0.8 ,grayscale = False)
                if topla2!=None:
                    x2, y2 = pyautogui.center(topla2)
                    click(x2, y2)
                    time.sleep(0.75)
                time.sleep(0.5)
                
                kiligayardim2=pyautogui.locateOnScreen('inc/img/yardim.png',confidence=0.8 ,grayscale = False)
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
                
                
                topla3=pyautogui.locateOnScreen('inc/img/kiligatopla.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if topla3!=None:
                    x5, y5 = pyautogui.center(topla3)
                    click(x5,y5)
                    time.sleep(1)
                time.sleep(1)
                toplaa3=pyautogui.locateOnScreen('inc/img/kiligatopla.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if toplaa3!=None:
                    x5, y5 = pyautogui.center(toplaa3)
                    click(x5,y5)
                    time.sleep(1)
                time.sleep(1)
                kiligayardim3=pyautogui.locateOnScreen('inc/img/yardim.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if kiligayardim3!=None:
                    x6, y6 = pyautogui.center(kiligayardim3)
                    click(x6,y6)
                    time.sleep(1)
                time.sleep(1)
                
                time.sleep(1)
                click(1118, 151)
                time.sleep(1)
                
                
                time.sleep(1)
                topla4=pyautogui.locateOnScreen('inc/img/topla2.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if topla4!=None:
                    x7, y7 = pyautogui.center(topla4)
                    click(x7,y7)
                    time.sleep(1)
                time.sleep(1)
                topla4=pyautogui.locateOnScreen('inc/img/topla2.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if topla4!=None:
                    x7, y7 = pyautogui.center(topla4)
                    click(x7,y7)
                    time.sleep(1)
                    
                time.sleep(1)
                
                
                kiligayardim4=pyautogui.locateOnScreen('inc/img/yardim.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
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
                hepsineyardimet=pyautogui.locateOnScreen('inc/img/hepsineyardimet.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
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
            click(783,80)
            time.sleep(0.75)
            click(1121,930)
            time.sleep(0.6)
            click(691,96)
            time.sleep(0.5)
            ######Mesaj########
            
            
            click(1074,997)
            time.sleep(0.5)
            tamam=pyautogui.locateOnScreen('inc/img/Tamam.png',confidence=0.8 ,grayscale = False)
            if tamam!=None:
                x,y=pyautogui.center(tamam)
                click(x,y)
                
                
            time.sleep(0.5)    
            
            
            click(927,556)
            time.sleep(0.5)
            tamam2=pyautogui.locateOnScreen('inc/img/Tamam.png',confidence=0.8 ,grayscale = False)
            if tamam2!=None:
                x2,y2=pyautogui.center(tamam2)
                click(x2,y2)
                
                
            time.sleep(0.7)
            
            
            click(931,1010)
            time.sleep(0.7)
            click(1173,1007)
            time.sleep(0.7)
            click(704,1004)
            time.sleep(0.7)
            click(947,1010)
            time.sleep(0.7)
            click(948,621)
            time.sleep(0.7)
            
            
            
            
            
            
            
            
            
            click(686,83)
            time.sleep(0.7)
            click(834,752)
            time.sleep(0.7)
            tamam3=pyautogui.locateOnScreen('inc/img/Tamam.png',confidence=0.8 ,grayscale = False)
            if tamam3!=None:
                x3,y3=pyautogui.center(tamam3)
                click(x3,y3)
                
                
                
                
            time.sleep(1)

            
            click(931,1010)
            time.sleep(0.7)
            click(1173,1007)
            time.sleep(0.7)
            click(704,1004)
            time.sleep(0.7)
            click(947,1010)
            time.sleep(0.7)
            click(948,621)
            time.sleep(0.7)
            
            
            
            
            
            
            
            click(698,84)
            time.sleep(0.5)
            click(698,84)
            time.sleep(0.5)   
        def KiligaExtra():
            time.sleep(0.5)
            click(1174, 887)#düzen 1
            time.sleep(1)
            hasatet=pyautogui.locateOnScreen('inc/img/hasatet.png',confidence=0.8 ,grayscale = False)
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
            
            hizlitopla=pyautogui.locateOnScreen('inc/img/hizlitopla.png',confidence=0.8 ,grayscale = False)
            if hizlitopla!=None:
                 time.sleep(1)
                 x, y = pyautogui.center(hizlitopla)
                 click(x, y)
                 time.sleep(1)
                 click(920, 946)#aktif et
                 time.sleep(1)
                 click(942,858)#ortaya tıkla
                 time.sleep(1)
            
            
            
            click(1174, 887)#düzen 1
            time.sleep(1.2)
            click(1050,379)
            time.sleep(2)
            tamponhasat=pyautogui.locateOnScreen('inc/img/tamponhasat.png',confidence=0.8 ,grayscale = False)
            sureondkkontrol()
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
            time.sleep(1)
            MadenArttirma()#ilk girilen değirmen
            time.sleep(1)
            Kaleicitopla()#ekranda toplama
            time.sleep(1)
            kiliga()#Lonca olayları
            time.sleep(1.2)
            KiligaExtra()#sonradan ekledik hizli arttırma falan
            time.sleep(1)
            click(939,1011)
            time.sleep(6)
            yenigiris=False
        
            while yenigiris==False:
                sureondkkontrol()
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                kale=pyautogui.locateOnScreen('inc/img/kale.png',confidence=0.8 ,grayscale = False)
                #sureondkkontrol()
                if kale!=None:
                    click(936,574)#kendi kaleme tikla
                    time.sleep(1.5)
                    sehirbonusugiris=pyautogui.locateOnScreen('inc/img/sehirbonusugiris.png',confidence=0.8 ,grayscale = False)#sehir bonusu tıkla
                    
                    if sehirbonusugiris!=None:#sehir bonusuna giris yapar
                        sehirx,sehiry=pyautogui.center(sehirbonusugiris)
                        click(sehirx,sehiry)
                        time.sleep(1)
                        pyautogui.moveTo(919,645)
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(919,189, 0.3)
                        pyautogui.mouseUp(button='left')
                        time.sleep(1.5)
                        bonus=pyautogui.locateOnScreen('inc/img/bonus.png',confidence=0.7 ,grayscale = False)
                        
                        
                        
                        if bonus !=None:#bonusa girince sıkıntı yok
                                bonusx, bonusy = pyautogui.center(bonus)
                                click(bonusx, bonusy)
                                #time.sleep(2)
                                time.sleep(2)
                                kullan=pyautogui.locateOnScreen('inc/img/kullan.png',confidence=0.8 ,grayscale = False)
                                sureondkkontrol()
                                if kullan !=None:
                                        kullanx, kullany = pyautogui.center(kullan)
                                        click(kullanx, kullany)
                                        time.sleep(1.5)
                                        click(924,172)
                                        time.sleep(1)
                                        click(694,92)
                                        time.sleep(1)
                    
                    sehirbonusugiris2=pyautogui.locateOnScreen('inc/img/sehirbonusugiris2.png',confidence=0.8 ,grayscale = False)#sehir bonusu tıkla
                    if sehirbonusugiris2!=None:#sehir bonusuna giris yapar
                        sehir2x,sehir2y=pyautogui.center(sehirbonusugiris2)
                        click(sehir2x,sehir2y)
                        time.sleep(1)
                        pyautogui.moveTo(919,645)
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(919,189, 1)
                        pyautogui.mouseUp(button='left')
                        time.sleep(1.5)
                        bonus=pyautogui.locateOnScreen('inc/img/bonus.png',confidence=0.8 ,grayscale = False)
                        
                        
                        
                        if bonus !=None:#bonusa girince sıkıntı yok
                                bonusx, bonusy = pyautogui.center(bonus)
                                click(bonusx, bonusy)
                                time.sleep(2)
                                time.sleep(1)
                                kullan=pyautogui.locateOnScreen('inc/img/kullan.png',confidence=0.8 ,grayscale = False)
                       
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
                sureondkkontrol()
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                kale=pyautogui.locateOnScreen('inc/img/kaleyegel.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if kale!=None:
                    click(936,574)#kendi kaleme tikla
                    time.sleep(3)
                    sehirbonusugiris=pyautogui.locateOnScreen('inc/img/sehirbonusugiris.png',confidence=0.8 ,grayscale = False)#sehir bonusu tıkla
                    sureondkkontrol()
                    if sehirbonusugiris!=None:#sehir bonusuna giris yapar
                        sehirx,sehiry=pyautogui.center(sehirbonusugiris)
                        click(sehirx,sehiry)
                        time.sleep(1.5)
                        pyautogui.moveTo(919,645)
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(919,189, 1)
                        pyautogui.mouseUp(button='left')
                        time.sleep(1.5)
                        bonus=pyautogui.locateOnScreen('inc/img/bonus.png',confidence=0.8 ,grayscale = False)
                        sureondkkontrol()
                        
                        
                        if bonus !=None:#bonusa girince sıkıntı yok
                                bonusx, bonusy = pyautogui.center(bonus)
                                click(bonusx, bonusy)
                                time.sleep(2)
                                time.sleep(1.5)
                                kullan=pyautogui.locateOnScreen('inc/img/kullan.png',confidence=0.8 ,grayscale = False)
                                sureondkkontrol()
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
            global seviyebes
            seviyebes=1
            click(232,20)
            click(232,20)
            time.sleep(0.5)
            click(264,13)
            click(264,13)
            time.sleep(1.5)
            click(1267,116)
            time.sleep(1.5)
        
            
        
            while 1:
                sureondkkontrol()
                oyunekran=pyautogui.locateOnScreen('inc/img/oyun.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
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
                sureondkkontrol()    
                anaekran=pyautogui.locateOnScreen('inc/img/anaekran.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if anaekran!=None:
                    break
                time.sleep(2)
                
                
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    yenigiris=True
                    break
                time.sleep(1)
            
            time.sleep(2)
            oyunvip=pyautogui.locateOnScreen('inc/img/carpi.png',confidence=0.7 ,grayscale = False)
            sureondkkontrol()
            if oyunvip !=None:
                    time.sleep(2)
                    click(1173,154)
                    time.sleep(1)
            time.sleep(2)
            postakutusu=pyautogui.locateOnScreen('inc/img/posta.png',confidence=0.6 ,grayscale = False)
            sureondkkontrol()
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
                sureondkkontrol()
                anaekran=pyautogui.locateOnScreen('inc/img/anaekran.png',confidence=0.8 ,grayscale = False)
                sureondkkontrol()
                if anaekran!=None:
                    break
                time.sleep(2)
                
                
                yenigirissekme=pyautogui.locateOnScreen('inc/img/yenigiris.png',confidence=0.8,grayscale=False)
                sureondkkontrol()
                if yenigirissekme!=None:
                    yenigiris=True
                    break
            
            time.sleep(1)
            
            oyunvip=pyautogui.locateOnScreen('inc/img/carpi.png',confidence=0.7 ,grayscale = False)
            sureondkkontrol()
            if oyunvip !=None:
                    time.sleep(2)
                    click(1173,154)
                    time.sleep(1)
            postakutusu=pyautogui.locateOnScreen('inc/img/posta.png',confidence=0.7 ,grayscale = False)
            sureondkkontrol()
            if postakutusu !=None:
                    time.sleep(2)
                    x, y = pyautogui.center(postakutusu)
                    time.sleep(1.2)
                    click(x,y)
        

     
        
        def GorevBaslat(user):
            global usernum
            global usernum,enbas
            usernum=0
            with open("inc/src/timer1.txt","r") as dosya:
                usernum=int(dosya.readline())
            dosya.close()
            while True:
                        global start_time
                        start_time = time.time()
                        print("sureyi sıfırladım: "+str(start_time))
                        sureondkkontrol()
                        now_e = datetime.datetime.now()
                        raporicinsure = now_e.strftime("%H")
                        raporicinsure=int(raporicinsure)
                        if raporicinsure==0:
                            raporicinad = now_e.strftime("%d-%m-%Y %H-%M-%S")
                            #os.mkdir("raporlar/"+raporicinad)
                            try:
                                
                                shutil.copytree("inc/img/rev", "raporlar/"+raporicinad)
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
                        with open("inc/src/timer2.txt","w") as dosya:
                                dosya.write(str(suresayac))
                        dosya.close()
                        if usernum==0:
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
                        
                            sorgu="SELECT * FROM kullanici WHERE kullanici_adi ="+kullaniciusername+" AND kullanici_pass =" + kullanicisifre
                            
                            
                            mycursor.execute(sorgu)
                            
                            myresult = mycursor.fetchall()
                            
                            if len(myresult)>0:
                                kullanici_adi=myresult[0][1]
                                kacgunkaldi=(myresult[0][6])               
                                if int(kacgunkaldi) >= 0:  
                                    print("süre bitmedi")
                                    
                                else:
                                    print("süre bitti")
                                    #QMessageBox.about(self,"Hata", "Botunuzun Süresi Bitmiştir..")
                                    app = QApplication(sys.argv)
                                    sys.exit(app.exec_())
                                    
                                    
                                    
                                    #QCoreApplication.quit()
                                    break
                                
                      
                            
                        
                        KaleDegistir(usernum,user)
                        if user[usernum].farmMetodu=="tahil":
                            Harici()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                            tahilCallBack()
                        elif user[usernum].farmMetodu=="kuvars":
                            Harici()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                            KuvarsCallBack()
                        elif user[usernum].farmMetodu=="demir":
                            Harici()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                            DemirCallBack()
                        elif user[usernum].farmMetodu=="odun" :
                            Harici()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                            OdunCallBack()
                        time.sleep(1)
                        usernum=usernum+1
                        time.sleep(1)
                        if usernum==user.__len__():#10 yap
                            usernum=0
                            #(usernum)
                            
        def GorevBaslat2(user):
            global usernum
            global usernum,enbas
            usernum=0
            with open("inc/src/timer1.txt","r") as dosya:
                usernum=int(dosya.readline())
            dosya.close()
            while True:
                        global start_time
                        start_time = time.time()
                        
                        sureondkkontrol()
                        now_e = datetime.datetime.now()
                        raporicinsure = now_e.strftime("%H")
                        raporicinsure=int(raporicinsure)
                        if raporicinsure==0:
                            raporicinad = now_e.strftime("%d-%m-%Y %H-%M-%S")
                            #os.mkdir("raporlar/"+raporicinad)
                            try:
                                
                                shutil.copytree("inc/img/rev", "raporlar/"+raporicinad)
                            except:
                                pass
                            
                            
                            
                        self.progress.emit(usernum+1)
                        global suresayac
                        suresayac=int(datetime.datetime.now().minute)+10
                        if suresayac >= 60:
                            suresayac=suresayac-60
                        now = datetime.datetime.now()
                        
                        with open("inc/src/timer2.txt","w") as dosya:
                                dosya.write(str(suresayac))
                        dosya.close()
                        
                        dt_string = now.strftime("%H:%M")
                        self.songiris.emit(dt_string+";"+str(usernum+1))
                        
                        
                        
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
                    
                        sorgu="SELECT * FROM kullanici WHERE kullanici_adi ="+kullaniciusername+" AND kullanici_pass =" + kullanicisifre
                        
                        
                        mycursor.execute(sorgu)
                        
                        myresult = mycursor.fetchall()
                        
                        if len(myresult)>0:
                            kullanıci_adi=myresult[0][1]
                            kacgunkaldi=myresult[0][6]               
                            if int(kacgunkaldi) >= 0:  
                                print("süre bitmedi")
                            else:
                                print("süre bitti")
                                break
                        
                        
                        KaleDegistir(usernum,user)
                        
                        
                        if user[usernum].farmMetodu=="tahil":
                            Harici2()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                        elif user[usernum].farmMetodu=="kuvars":
                            Harici2()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                        elif user[usernum].farmMetodu=="demir":
                            Harici2()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                        elif user[usernum].farmMetodu=="odun" :
                            Harici2()
                            time.sleep(0.5)
                            im = pyautogui.screenshot("inc/img/rev/"+str(usernum)+".png",region=(661,34, 350, 25))
                            self.resimgonder.emit("inc/img/rev/"+str(usernum)+".png"+";"+str(usernum+1))
                        time.sleep(1)
                
                        usernum=usernum+1
                        time.sleep(1)
                        if usernum==user.__len__():#10 yap
                            usernum=0
        global user
        user=kullanicilari_yukle(kullanicisayisi)   
        #user[0].kullaniciAdi

                
        with open("inc/src/fMethod.txt","r") as dosya:
                    secim=dosya.readline()
        dosya.close()
            #self.progress.emit(3)
        
        
        
        if secim == "1": 
                print("Başladı 1")
                GorevBaslat(user)        
        elif secim == "2":    
                print("başladı 2")
                GorevBaslat2(user)
        
        
        
from getmac import get_mac_address as gma
import mysql.connector
global macid
        
global kullaniciusername
kullaniciusername=""
class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            #self.hesapekle_EKRAN= MainWindow2()
            #self.botbaslat_EKRAN= Ui_MainWindow3()
            self.ui.girisbuton.clicked.connect(self.girisbuton)
            self.ui.kayitbutton.clicked.connect(self.MacidKayit)
            #logo ekleme
            
            pixmap = QPixmap("inc/img/logo.png")
            pixmap=pixmap.scaled(240, 240)
            self.ui.logo.setPixmap(pixmap)
            global girisonay
            girisonay=False
        
        
        
        global giris
        def giris(self):
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
        
            sorgu="SELECT * FROM kullanici WHERE kullanici_adi ="+kullaniciusername+" AND kullanici_pass =" + kullanicisifre
            
            
            mycursor.execute(sorgu)
            
            myresult = mycursor.fetchall()

            
            if len(myresult)>0:
                macid=gma()
                kacgunkaldi=int(myresult[0][6])
                if int(kacgunkaldi) >= 0 and myresult[0][5]!='0' and macid==myresult[0][5] :
                    print("giris basarili")
                    girisonay=True
                    
 
                else:
                    if int(kacgunkaldi)<0:
                        print("Süre Bitti")
                        girisonay=False
                        QMessageBox.warning(self,"Hata", "Süreniz bitmiştir")
                    if (myresult[0][5])=='0':
                        print("Lütfen PC Kayıt butonuna basınız")
                        girisonay=False
                        QMessageBox.warning(self,"Hata", "Lütfen Bilgisayar Kayıt butonuna basınız")
                    if (myresult[0][5])!=macid and myresult[0][5]!='0':
                        print("Bu hesap başka bilgisayarda kayıtlı!")
                        girisonay=False
                        QMessageBox.critical(self,"Hata", "Bu hesap başka bilgisayarda kayıtlı")
            else:
                print("böyle bir kullanici yok")
                girisonay=False
                QMessageBox.critical(self,"Hata", "Lütfen kullanıcı adınızı veya şifrenizi kontrol ediniz.")
                    
        
        
       
                    
        def MacidKayit(self):
                        global macid
                        global kullaniciusername,kullanicisifre,kacgunkaldi,girisonay
                        kullaniciusername="'"+str(self.ui.email.toPlainText())+"'"
                        kullanicisifre="'"+str(self.ui.sifre.toPlainText())+"'"
                        macid="'"+gma()+"'"
                        
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
                    
                        sorgu="SELECT * FROM kullanici WHERE kullanici_adi ="+kullaniciusername+" AND kullanici_pass =" + kullanicisifre
                        
                        
                        mycursor.execute(sorgu)
                        
                        myresult = mycursor.fetchall()
                    
                        
                        if myresult[0][5] == '0' :
                            mycursor = mydb.cursor()
                            mycursor.execute("UPDATE kullanici SET macid ="+macid+"WHERE kullanici.kullanici_adi ="+kullaniciusername)
                            mydb.commit()
                            QMessageBox.about(self,"Kayıt Başarılı","Bilgisayar kaydı başarıyla tamamlandı!")
                            
                        else:
                            QMessageBox.warning(self,"Hata","Bu kullanıcı adı ve şifre'nin bilgisayar kaydı zaten yapılmıştır!!")
                            #print("Bu kullanıcı adı ve şifre'nin bilgisayar kaydı zaten yapılmıştır!!")
                        
                    
    
        def girisbuton(self):
            global kullaniciusername,kullanicisifre,kacgunkaldi,girisonay
            kullaniciusername="'"+str(self.ui.email.toPlainText())+"'"
            kullanicisifre="'"+str(self.ui.sifre.toPlainText())+"'"
            #kullaniciusername="'admin'"
            #kullanicisifre="'password'"
            giris(self)
            #burasını kontrol et false yap
            #girisonay=True
            print(girisonay)
            if girisonay==True:
                girisonay=False
                self.cams = MainWindow2() 
                self.cams.show()
                self.close()
            else:
                pass
        def kayitbuton(self):
            print("kayitedildi")
                
                  

class MainWindow3(QMainWindow):
    def __init__(self):
            super(MainWindow3, self).__init__()
            self.ui = Ui_MainWindow3()
            self.ui.setupUi(self)
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.ui.toolBar.actionTriggered[QtWidgets.QAction].connect(self.menuBot_Baslat)
            self.ui.farm1.clicked.connect(self.farm1)    
            self.ui.farm2.clicked.connect(self.farm2)   
            self.ui.stop.clicked.connect(self.stop)
            self.myworker = None
            self.counter  = 0            
            self.show()
            
            
            
            try:
                with open("inc/src/farmcombobox.txt","r") as dosya:
                    combolarihizala=dosya.readline()
                combolarihizala=combolarihizala.split(";")
                combolarihizala.pop(-1)
                self.ui.comboBox.setCurrentIndex(int(combolarihizala[0]))
                self.ui.comboBox_2.setCurrentIndex(int(combolarihizala[1]))
                self.ui.comboBox_3.setCurrentIndex(int(combolarihizala[2]))
                self.ui.comboBox_4.setCurrentIndex(int(combolarihizala[3]))
                self.ui.comboBox_5.setCurrentIndex(int(combolarihizala[4]))
                self.ui.comboBox_6.setCurrentIndex(int(combolarihizala[5]))
                self.ui.comboBox_7.setCurrentIndex(int(combolarihizala[6]))
                self.ui.comboBox_8.setCurrentIndex(int(combolarihizala[7]))
                self.ui.comboBox_9.setCurrentIndex(int(combolarihizala[8]))
                self.ui.comboBox_10.setCurrentIndex(int(combolarihizala[9]))
                self.ui.comboBox_11.setCurrentIndex(int(combolarihizala[10]))
                self.ui.comboBox_12.setCurrentIndex(int(combolarihizala[11]))
                self.ui.comboBox_13.setCurrentIndex(int(combolarihizala[12]))
                self.ui.comboBox_14.setCurrentIndex(int(combolarihizala[13]))
                self.ui.comboBox_15.setCurrentIndex(int(combolarihizala[14]))
            except:pass
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
        
            sorgu="SELECT * FROM kullanici WHERE kullanici_adi ="+kullaniciusername+" AND kullanici_pass =" + kullanicisifre
            
            
            mycursor.execute(sorgu)
            
            myresult = mycursor.fetchall()
            
            if len(myresult)>0:
                kullanıci_adi=myresult[0][1]
                kacgunkaldi=myresult[0][6]               
                self.ui.log_isim.setText(("Kullanıcı: "+str(kullanıci_adi) + " | Kalan Süre :" + str(kacgunkaldi)+ " Gün"))
                            
                    
                    
                    
            try:
                for n in range(1,21):
                    
            
                    pixmap = QPixmap("inc/img/rev/"+str(n-1))
                    
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
            
    # signal baglantıları
    
    def reportProgress(self, n):
            with open("inc/src/timer1.txt","w") as dosya:
                dosya.write(str(n-1))
            dosya.close()
            print(f"Long-Running Step: {n}")
            if n == 1:   
                self.ui.sira.setStyleSheet('color: green')
            else: (self.ui.sira.setStyleSheet('color: white'))
            if n == 2:        
                (self.ui.sira_2.setStyleSheet('color: green')) 
            else: (self.ui.sira_2.setStyleSheet('color: white'))
            if n == 3:
              (self.ui.sira_3.setStyleSheet('color: green')) 
            else: (self.ui.sira_3.setStyleSheet('color: white'))
            if n == 4:
              (self.ui.sira_4.setStyleSheet('color: green')) 
            else: (self.ui.sira_4.setStyleSheet('color: white'))
            if n == 5:
              (self.ui.sira_5.setStyleSheet('color: green')) 
            else: (self.ui.sira_5.setStyleSheet('color: white'))
            if n == 6:
              (self.ui.sira_6.setStyleSheet('color: green')) 
            else: (self.ui.sira_6.setStyleSheet('color: white'))
            if n == 7:
              (self.ui.sira_7.setStyleSheet('color: green')) 
            else: (self.ui.sira_7.setStyleSheet('color: white'))
            if n == 8:
              (self.ui.sira_8.setStyleSheet('color: green')) 
            else: (self.ui.sira_8.setStyleSheet('color: white'))
            if n == 9:
              (self.ui.sira_9.setStyleSheet('color: green')) 
            else: (self.ui.sira_9.setStyleSheet('color: white'))
            if n == 10:
              (self.ui.sira_10.setStyleSheet('color: green')) 
            else: (self.ui.sira_10.setStyleSheet('color: white'))
            if n == 11:
              (self.ui.sira_11.setStyleSheet('color: green')) 
            else: (self.ui.sira_11.setStyleSheet('color: white'))
            if n == 12:
              (self.ui.sira_12.setStyleSheet('color: green')) 
            else: (self.ui.sira_12.setStyleSheet('color: white'))
            if n == 13:
              (self.ui.sira_13.setStyleSheet('color: green'))
            else: (self.ui.sira_13.setStyleSheet('color: white'))
            if n == 14:
              (self.ui.sira_14.setStyleSheet('color: green')) 
            else: (self.ui.sira_14.setStyleSheet('color: white'))
            if n == 15:
              (self.ui.sira_15.setStyleSheet('color: green')) 
            else: (self.ui.sira_15.setStyleSheet('color: white'))
            if n == 16:
              (self.ui.sira_16.setStyleSheet('color: green')) 
            else: (self.ui.sira_16.setStyleSheet('color: white'))
            if n == 17:
              (self.ui.sira_17.setStyleSheet('color: green')) 
            else: (self.ui.sira_17.setStyleSheet('color: white'))
            if n == 18:
              (self.ui.sira_18.setStyleSheet('color: green')) 
            else: (self.ui.sira_18.setStyleSheet('color: white'))
            if n == 19:
              (self.ui.sira_19.setStyleSheet('color: green')) 
            else: (self.ui.sira_19.setStyleSheet('color: white'))
            if n == 20:
              (self.ui.sira_20.setStyleSheet('color: green')) 
            else: (self.ui.sira_20.setStyleSheet('color: white'))
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
            
     
    global sayac_thre
    sayac_thre=0
    #sinyal baglantilari bitti
    def farm1(self):
            global ondkicinke
            def ondkicinke():
                global sayac_thre,start_time
                sayac_thre=1
                start_time = time.time()
                kontrolcu=0
                while 1:
                    if kontrolcu==0:
                            
                        e = int(time.time() - start_time)
                        #print(start_time)
                        if e == 600:
                            print("60 sn oldu")               
                            start_time = time.time()
                            self.myworker.terminate()         
                            self.myworker = None
                            
                            with open("inc/src/timer1.txt","r") as dosya:
                                usernum=int(dosya.readline())
                            dosya.close()
                            
                            
                            
                            
                            
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

                            
                            global kullanicilar 
                            with open("inc/src/farmcombobox.txt","w") as dosya:
                                dosya.write(comboBox+";"+comboBox_2+";"+comboBox_3+";"+comboBox_4+";"+comboBox_5+";"+comboBox_6+";"+comboBox_7+";")
                                dosya.write(comboBox_8+";"+comboBox_9+";"+comboBox_10+";"+comboBox_11+";"+comboBox_12+";"+comboBox_13+";"+comboBox_14+";")
                                dosya.write(comboBox_15+";"+comboBox_16+";"+comboBox_17+";"+comboBox_18+";"+comboBox_19+";"+comboBox_20+";")

                                
                            dosya.close()
                            with open("inc/src/user.txt","r") as dosya:
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
                            
                            with open("inc/src/userFmethod.txt","w") as dosya:
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
                            with open("inc/src/fMethod.txt","w") as dosya:
                                dosya.write("1")
                            dosya.close()
                            
                            with open("inc/src/timer1.txt","w") as dosya:
                                if len(kullanicilar) == usernum:
                                   dosya.write(str(0)) 
                                else:
                                    dosya.write(str(usernum+1))
                            dosya.close()
                        
                            #hazırlık bitti
                            global myworker
                            self.myworker = AThread() 
                            self.myworker.finished.connect(self.finishedAThread)
                            self.myworker.progress.connect(self.reportProgress)
                            self.myworker.songiris.connect(self.songirisprogress)
                            self.myworker.resimgonder.connect(self.resim)
                            self.myworker.start()
                                #hazırlık yapacağız
            if sayac_thre==0:
                    
                t1 = threading.Thread(target=ondkicinke)
                t1.start()
            
                   
        
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

            
            global kullanicilar 
            with open("inc/src/farmcombobox.txt","w") as dosya:
                                dosya.write(comboBox+";"+comboBox_2+";"+comboBox_3+";"+comboBox_4+";"+comboBox_5+";"+comboBox_6+";"+comboBox_7+";")
                                dosya.write(comboBox_8+";"+comboBox_9+";"+comboBox_10+";"+comboBox_11+";"+comboBox_12+";"+comboBox_13+";"+comboBox_14+";")
                                dosya.write(comboBox_15+";")

                                
            dosya.close()
            with open("inc/src/user.txt","r") as dosya:
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
            
            with open("inc/src/userFmethod.txt","w") as dosya:
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
            with open("inc/src/fMethod.txt","w") as dosya:
                dosya.write("1")
            dosya.close()
        
        
            #hazırlık bitti
            global myworker
            self.myworker = AThread() 
            self.myworker.finished.connect(self.finishedAThread)
            self.myworker.progress.connect(self.reportProgress)
            self.myworker.songiris.connect(self.songirisprogress)
            self.myworker.resimgonder.connect(self.resim)
            self.myworker.start()
    def farm2(self):
        
        #hazırlık yapacağız
        
        
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
            
            with open("inc/src/user.txt","r") as dosya:
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
            
            with open("inc/src/userFmethod.txt","w") as dosya:
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
            with open("inc/src/fMethod.txt","w") as dosya:
                dosya.write("2")
            dosya.close()
        
        
            #hazırlık bitti

            self.myworker = AThread() 
            self.myworker.finished.connect(self.finishedAThread)
            self.myworker.progress.connect(self.reportProgress)
            self.myworker.songiris.connect(self.songirisprogress)
            self.myworker.resimgonder.connect(self.resim)
            self.myworker.start()
    
    def menuBot_Baslat(self, selection):
            print("asd")
            
            name = selection.text()
            if name=="Hesap Ekle":
               
                self.close()
           
               
                self.cams = MainWindow2() 
                self.cams.show()
                
            if name=="Giriş":
                       
                self.close()
                self.cams = MainWindow() 
                self.cams.show()
                    

                    


                

                
    def finishedAThread(self):
        self.myworker = None

    def stop(self):
        try:
                            self.myworker.terminate()         
                            self.myworker = None
                            
                            with open("inc/src/timer1.txt","r") as dosya:
                                usernum=int(dosya.readline())
                            dosya.close()
                            
                        
                            
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
                            
                            with open("inc/src/user.txt","r") as dosya:
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
                            
                            with open("inc/src/userFmethod.txt","w") as dosya:
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
                            with open("inc/src/fMethod.txt","w") as dosya:
                                dosya.write("1")
                            dosya.close()
                        
                            with open("inc/src/timer1.txt","w") as dosya:
                                if len(kullanicilar) <= usernum:
                                   dosya.write(str(0)) 
                                else:
                                    dosya.write(str(usernum+1))
                            dosya.close()

        except:
            pass       
  
    def closeEvent(self, event): 
            reply = QMessageBox.question(self, 'Dikkat !!',
                "Çıkış Yapmak Üzeresiniz, kapatmak istediğinize emin misiniz?",
                 QMessageBox.Yes,
                 QMessageBox.No)
            if reply == QMessageBox.Yes:         
                if self.myworker:
                    self.myworker.quit()                    
                del self.myworker
                super(MainWindow3, self).closeEvent(event)
            else:
                event.ignore()
                
                
            


class MainWindow2(QMainWindow):
        def __init__(self):
            super(MainWindow2, self).__init__()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi(self)
        
            self.setWindowTitle("MOBOT - Hesap Ekle")
            #self.hesapekle_EKRAN= Ui_MainWindow2()
            #self.botbaslat_EKRAN= Ui_MainWindow3()
            self.ui.save.clicked.connect(self.save)
            #self.ui.menuBot_Baslat.triggered.connect(self.menuBot_Baslat)
            #self.ui.menuBot_Baslat.addAction('Option #1', self.menuBot_Baslat)
            self.ui.toolBar.actionTriggered[QtWidgets.QAction].connect(self.menuBot_Baslat)
            #guncelleme icin 
            global kontrolcu
            kontrolcu=0
            global kullanicilar 
            
            with open("inc/src/user.txt","r") as dosya:
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

            except:
                pass
       
        def closeEvent(self, event):
            global kontrolcu
            if kontrolcu==0:
      
                reply = QMessageBox.question(self, 'Dikkat !!',
                    "Çıkış Yapmak Üzeresiniz, kapatmak istediğinize emin misiniz?",
                     QMessageBox.Yes,
                     QMessageBox.No)
                if reply == QMessageBox.Yes:
            
                    
                    super(MainWindow2, self).closeEvent(event)
                else:
                    event.ignore()
           
        
        
        
        def menuBot_Baslat(self, selection):
            global kontrolcu
            name = selection.text()
            if name=="Bot Başlat":
                self.cams = MainWindow3() 
                self.cams.show()
                kontrolcu=1
                self.close()
            if name=="Giriş":
                self.cams = MainWindow() 
                self.cams.show()
                self.close()
           
            
        def save(self):
            global kontrolcu
            kontrolcu=1
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

            
            comboBox=" "
            
            
        
           

            with open("inc/src/user.txt","w") as dosya:
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

            dosya.close()
            
            global kullanicilar 
            
            with open("inc/src/user.txt","r") as dosya:
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
            
            
            with open("inc/src/userFmethod.txt","w") as dosya:
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
            self.cams = MainWindow3() 
            self.cams.show()
            self.close()

            
     
 

if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.setWindowTitle("MOBOT")
        window.show()

        sys.exit(app.exec_())
        
