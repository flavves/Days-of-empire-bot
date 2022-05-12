# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/masaüstü/yazılımileilgilihersey/onluk/osmanli oyun bot/yeni versiyon/giris.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 628)
        MainWindow.setStyleSheet("selection-color: rgb(170, 170, 255);\n"
"background-color: rgb(167, 167, 167);\n"
"alternate-background-color: rgb(85, 0, 0);\n"
"selection-background-color: rgb(85, 255, 127);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 641, 641))
        self.scrollArea.setStyleSheet("color: rgb(85, 170, 0);\n"
"color: rgb(0, 0, 255);\n"
"selection-color: rgb(170, 170, 255);\n"
"border-top-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.logo.setGeometry(QtCore.QRect(220, 40, 200, 200))
        self.logo.setMinimumSize(QtCore.QSize(200, 200))
        self.logo.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logo.setFont(font)
        self.logo.setObjectName("logo")
        self.email = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.email.setGeometry(QtCore.QRect(160, 310, 350, 41))
        self.email.setMinimumSize(QtCore.QSize(350, 41))
        self.email.setMaximumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setOverwriteMode(False)
        self.email.setObjectName("email")
        self.sifre = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.sifre.setGeometry(QtCore.QRect(160, 380, 350, 41))
        self.sifre.setMinimumSize(QtCore.QSize(350, 41))
        self.sifre.setMaximumSize(QtCore.QSize(350, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sifre.setFont(font)
        self.sifre.setOverwriteMode(False)
        self.sifre.setObjectName("sifre")
        
        
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(160, 260, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        
        
        self.girisbuton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.girisbuton.setGeometry(QtCore.QRect(360, 450, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.girisbuton.setFont(font)
        self.girisbuton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.girisbuton.setObjectName("girisbuton")

        self.kayitbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.kayitbutton.setGeometry(QtCore.QRect(160, 450, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.kayitbutton.setFont(font)
        self.kayitbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 255);")
        self.kayitbutton.setObjectName("kayitbutton")        
        

        
        
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(0, 520, 641, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(0, 570, 641, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(190, 533, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGiri = QtWidgets.QAction(MainWindow)
        self.actionGiri.setObjectName("actionGiri")
        self.actionHesaplar_Ekle = QtWidgets.QAction(MainWindow)
        self.actionHesaplar_Ekle.setObjectName("actionHesaplar_Ekle")
        self.actionBot_Ba_lar = QtWidgets.QAction(MainWindow)
        self.actionBot_Ba_lar.setObjectName("actionBot_Ba_lar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOBOT"))
        self.logo.setText(_translate("MainWindow", "LOGO"))
        self.email.setPlaceholderText(_translate("MainWindow", "Kullanıcı Adı"))
        self.sifre.setPlaceholderText(_translate("MainWindow", "Şifre"))
        self.label.setText(_translate("MainWindow", "Sisteme Giriş Yapabilmek İçin Kullanıcı Bilgilerini Giriniz"))
        self.girisbuton.setText(_translate("MainWindow", "Giriş"))
        self.kayitbutton.setText(_translate("MainWindow", "Bilgisayar Kayıt"))        
        self.label_2.setText(_translate("MainWindow", "www.muhtesemosmanlibot.com"))
        self.actionGiri.setText(_translate("MainWindow", "Giriş"))
        self.actionHesaplar_Ekle.setText(_translate("MainWindow", "Hesapları Ekle"))
        self.actionBot_Ba_lar.setText(_translate("MainWindow", "Bot Başlat"))

