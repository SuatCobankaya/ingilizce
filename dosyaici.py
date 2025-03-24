from PyQt5.QtWidgets import *
from ui_dosyaiciyeni import Ui_MainWindow
from anasayfa import apply_theme  # Tema fonksiyonunu import et

class dosyaicipencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.dosyaici_pencere = Ui_MainWindow()
        self.dosyaici_pencere.setupUi(self)
        self.dosyaici_pencere.pushButton_geri.clicked.connect(self.geri)
        self.dosyaici_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.dosyaici_pencere.centralwidget) 
        
        # Başlangıçta global temayı uygula
        apply_theme(self)

    def geri(self):
        from dosya import dosyapencere
        self.close()
        self.giris = dosyapencere()
        apply_theme(self.giris)  # Yeni pencereye temayı uygula
        self.giris.show()

    def anasayfa(self):
        from anasayfa import anapencere
        self.close()
        self.giris = anapencere()
        apply_theme(self.giris)  # Yeni pencereye temayı uygula
        self.giris.show()