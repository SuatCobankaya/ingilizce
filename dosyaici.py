from PyQt5.QtWidgets import *
from ui_dosyaiciyeni import Ui_MainWindow

class dosyaicipencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.dosyaici_pencere = Ui_MainWindow()
        self.dosyaici_pencere.setupUi(self)
        self.dosyaici_pencere.pushButton_geri.clicked.connect(self.geri)
        self.dosyaici_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.dosyaici_pencere.centralwidget) 
    def geri(self, ):
        from dosya import dosyapencere
        self.giris = dosyapencere()
        self.giris.show()
        self.close() 
    def anasayfa(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close() 