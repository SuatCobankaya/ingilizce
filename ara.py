from PyQt5.QtWidgets import *
from ui_ara import Ui_MainWindow

class arapencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ara_pencere = Ui_MainWindow()
        self.ara_pencere.setupUi(self)
        self.ara_pencere.pushButton_geri.clicked.connect(self.geri)
        self.ara_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.ara_pencere.centralwidget) 
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