from PyQt5.QtWidgets import *
from ui_dosyayeni import Ui_MainWindow

class dosyapencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.dosya_pencere = Ui_MainWindow()
        self.dosya_pencere.setupUi(self)
        self.dosya_pencere.pushButton_geri.clicked.connect(self.geri)
        self.dosya_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.dosya_pencere.pushButton_yeni.clicked.connect(self.yeni)
        self.dosya_pencere.pushButton_sil.clicked.connect(self.sil)
        self.setCentralWidget(self.dosya_pencere.centralwidget) 
    def geri(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close() 
    def anasayfa(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close() 
    def yeni(self, ):
        from dosyaici import dosyaicipencere
        self.giris = dosyaicipencere()
        self.giris.show()
        self.close() 
    def sil(self, ):
        pass