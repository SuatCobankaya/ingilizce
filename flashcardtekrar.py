from PyQt5.QtWidgets import *
from ui_flashcardtekrar import Ui_MainWindow

class flashcardtekrarpencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.flashcardtekrar_pencere = Ui_MainWindow()
        self.flashcardtekrar_pencere.setupUi(self)
        self.flashcardtekrar_pencere.pushButton_geri.clicked.connect(self.geri)
        self.flashcardtekrar_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.flashcardtekrar_pencere.centralwidget) 
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