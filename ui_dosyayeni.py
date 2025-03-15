from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Üstteki butonlar için horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Geri butonu
        self.pushButton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_geri.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_geri.setIcon(icon)
        self.pushButton_geri.setDefault(True)
        self.pushButton_geri.setObjectName("pushButton_geri")
        self.horizontalLayout.addWidget(self.pushButton_geri)

        # Anasayfa butonu
        self.pushButton_anasayfa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anasayfa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_anasayfa.setIcon(icon1)
        self.pushButton_anasayfa.setDefault(True)
        self.pushButton_anasayfa.setObjectName("pushButton_anasayfa")
        self.horizontalLayout.addWidget(self.pushButton_anasayfa)

        # Boşluk ekle
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # Scroll Area oluştur
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # GroupBox oluştur
        self.groupBox = QtWidgets.QGroupBox()
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        # GroupBox için grid layout
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        # Buton ve label'ları ekle
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.label_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setDefault(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton_ogren_1 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_ogren_1.setFont(font)
        self.pushButton_ogren_1.setDefault(True)
        self.pushButton_ogren_1.setObjectName("pushButton_ogren_1")
        self.gridLayout.addWidget(self.pushButton_ogren_1, 0, 2, 1, 1)

        self.pushButton_ogren_2 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_ogren_2.setFont(font)
        self.pushButton_ogren_2.setDefault(True)
        self.pushButton_ogren_2.setObjectName("pushButton_ogren_2")
        self.gridLayout.addWidget(self.pushButton_ogren_2, 1, 2, 1, 1)

        self.pushButton_ogren_3 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_ogren_3.setFont(font)
        self.pushButton_ogren_3.setDefault(True)
        self.pushButton_ogren_3.setObjectName("pushButton_ogren_3")
        self.gridLayout.addWidget(self.pushButton_ogren_3, 2, 2, 1, 1)

        # GroupBox'ı scroll area'ya ekle
        self.scrollArea.setWidget(self.groupBox)
        self.verticalLayout_2.addWidget(self.scrollArea)

        # Alt butonlar için horizontal layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Boşluk ekle
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        # Sil butonu
        self.pushButton_sil = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sil.sizePolicy().hasHeightForWidth())
        self.pushButton_sil.setSizePolicy(sizePolicy)
        self.pushButton_sil.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_sil.setDefault(True)
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.horizontalLayout_2.addWidget(self.pushButton_sil)

        # Yeni butonu
        self.pushButton_yeni = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_yeni.sizePolicy().hasHeightForWidth())
        self.pushButton_yeni.setSizePolicy(sizePolicy)
        self.pushButton_yeni.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_yeni.setDefault(True)
        self.pushButton_yeni.setObjectName("pushButton_yeni")
        self.horizontalLayout_2.addWidget(self.pushButton_yeni)

        # Boşluk ekle
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        self.menuDarkmode = QtWidgets.QMenu(self.menuAyarlar)
        self.menuDarkmode.setObjectName("menuDarkmode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWhite = QtWidgets.QAction(MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.menuDarkmode.addAction(self.actionWhite)
        self.menuDarkmode.addAction(self.actionDark)
        self.menuAyarlar.addAction(self.menuDarkmode.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Görüntüle"))
        self.label_1.setText(_translate("MainWindow", "3000 Kelime"))
        self.label_2.setText(_translate("MainWindow", "Kalıplar"))
        self.pushButton_3.setText(_translate("MainWindow", "Görüntüle"))
        self.pushButton_1.setText(_translate("MainWindow", "Görüntüle"))
        self.label_3.setText(_translate("MainWindow", "Deyimler"))
        self.pushButton_ogren_1.setText(_translate("MainWindow", "Öğren"))
        self.pushButton_ogren_2.setText(_translate("MainWindow", "Öğren"))
        self.pushButton_ogren_3.setText(_translate("MainWindow", "Öğren"))
        self.pushButton_sil.setText(_translate("MainWindow", "Sil"))
        self.pushButton_yeni.setText(_translate("MainWindow", "Yeni"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuDarkmode.setTitle(_translate("MainWindow", "Tema"))
        self.actionWhite.setText(_translate("MainWindow", "White"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())