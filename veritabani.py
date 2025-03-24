import sqlite3
import os
import random
class database():
    def baglantiac(self):
            self.con = sqlite3.connect("veritabani.db")
            self.cursor = self.con.cursor()
    def dosyalarigetir(self):
         self.baglantiac()
         self.cursor.execute("SELECT FileName FROM Files")
         dosyalar = self.cursor.fetchall()
         self.baglantikapat()
         return [row[0] for row in dosyalar]
    def ara(self,kelime):
         kelime = kelime.lower()
         self.baglantiac()
         self.cursor.execute("SELECT Meaning FROM WORDS WHERE EnglishWord = ?", (kelime,))
         anlamlar = self.cursor.fetchall()
         self.baglantikapat()
         return [row[0] for row in anlamlar]
    def kelimelerigetir(self,a):
         self.baglantiac()
         self.cursor.execute("SELECT EnglishWord, Meaning, ExampleSentences FROM WORDS WHERE FileId = ?", (a,))
         kelimeler = self.cursor.fetchall()
         self.baglantikapat()
         return kelimeler
    def random(self,dosyaid,sayi):
         self.baglantiac()
         self.cursor.execute("SELECT EnglishWord, Meaning FROM WORDS WHERE FileId = ?", (dosyaid,))
         rastgele = self.cursor.fetchall()
         self.baglantikapat()
         if len(rastgele) < sayi:
          return rastgele
         else:
          rastgele = random.sample(rastgele, sayi)
          return rastgele
    def dosyaekle(self,dosyaadi):
         self.baglantiac()
         self.cursor.execute("""INSERT INTO Files (FileName) VALUES (?);""", (dosyaadi,))
         self.con.commit()
         self.baglantikapat()
    def dosyasil(self,dosyaismi):
         self.baglantiac()
         self.cursor.execute("""DELETE FROM Files WHERE FileName = ?;""", (dosyaismi,))
         self.con.commit()
         self.baglantikapat()
    def dosyaidgetir(self,a):
         self.baglantiac()
         self.cursor.execute("SELECT FileId FROM Files WHERE FileName = ?", (a,))
         id = self.cursor.fetchall()
         self.baglantikapat()
         return id
    def kelimeekle(self,kelime,anlam,dosyaid,cumle=None):
         self.baglantiac()
         self.cursor.execute("""INSERT INTO WORDS (EnglishWord, Meaning, FileId, ExampleSentences) VALUES (?, ?, ?, ?);""", (kelime,anlam,dosyaid,cumle))
         self.con.commit()
         self.baglantikapat()
    def baglantikapat(self):
        self.con.close()


