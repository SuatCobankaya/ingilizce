from PyQt5.QtWidgets import *
from ui_anasayfayeni import Ui_MainWindow
from ara import arapencere
from cumle import cumlepencere
from dosya import dosyapencere
from eslestir import eslestirpencere
from istatislik import istatislikpencere
from flashcardtekrar import flashcardtekrarpencere
from test import testpencere
from yenikelime import yenikelimepencere

class anapencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ana_pencere = Ui_MainWindow()
        self.ana_pencere.setupUi(self)
        self.ana_pencere.pushButton_ara.clicked.connect(self.ara)
        self.ana_pencere.pushButton_cumle.clicked.connect(self.cumle)
        self.ana_pencere.pushButton_dosya.clicked.connect(self.dosya)
        self.ana_pencere.pushButton_eslestirme.clicked.connect(self.eslestir)
        self.ana_pencere.pushButton_istatislik.clicked.connect(self.istatislik)
        self.ana_pencere.pushButton_kart.clicked.connect(self.kart)
        self.ana_pencere.pushButton_kaydet.clicked.connect(self.kaydet)
        self.ana_pencere.pushButton_test.clicked.connect(self.test)
        self.ana_pencere.pushButton_yenikelime.clicked.connect(self.yenikelime)
        self.ana_pencere.actionDark.triggered.connect(self.darkmode)
        self.ana_pencere.actionWhite.triggered.connect(self.whitemode)
        self.setCentralWidget(self.ana_pencere.centralwidget)
    def ara(self, ):
        self.close()
        self.araac = arapencere()
        self.araac.show()
    def cumle(self, ):
        self.close()
        self.cumleac = cumlepencere()
        self.cumleac.show()
    def dosya(self, ):
        self.close()
        self.dosyaac = dosyapencere()
        self.dosyaac.show()
    def eslestir(self, ):
        self.close()
        self.eslestirac = eslestirpencere()
        self.eslestirac.show()
    def istatislik(self, ):
        self.close()
        self.istatislikac = istatislikpencere()
        self.istatislikac.show()
    def kart(self, ):
        self.close()
        self.kartac = flashcardtekrarpencere()
        self.kartac.show()
    def test(self, ):
        self.close()
        self.testac = testpencere()
        self.testac.show()
    def yenikelime(self, ):
        self.close()
        self.yenikelimeac = yenikelimepencere()
        self.yenikelimeac.show()
    def kaydet(self, ):
        pass
    def darkmode(self, ):
        dark_stylesheet = """
        QWidget {
        background-color: #2e2e2e;
        color: white;
        }
         """
        self.setStyleSheet(dark_stylesheet)
    def whitemode(self, ):
        light_stylesheet = """
        QWidget {
        background-color: #ffffff;
        color: black;
        }
        """
        self.setStyleSheet(light_stylesheet)
    