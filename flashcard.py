from PyQt5.QtWidgets import *
from ui_flashcard import Ui_MainWindow

class flashcardpencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.flashcard_pencere = Ui_MainWindow()
        self.flashcard_pencere.setupUi(self)
        self.flashcard_pencere.pushButton_geri.clicked.connect(self.geri)
        self.flashcard_pencere.pushButton_anasayfa.clicked.connect(self.anasayfa)
        self.setCentralWidget(self.flashcard_pencere.centralwidget) 
    def geri(self, ):
        from yenikelime import yenikelimepencere
        self.giris = yenikelimepencere()
        self.giris.show()
        self.close() 
    def anasayfa(self, ):
        from anasayfa import anapencere
        self.giris = anapencere()
        self.giris.show()
        self.close() 