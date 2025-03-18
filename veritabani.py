import sqlite3

class Database:
    def __init__(self, db_path="veritabani.db"):
        """Veritabanı bağlantısını başlatır."""
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        """Veritabanına bağlanır."""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self

    def close(self):
        """Veritabanı bağlantısını kapatır."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def get_filesname(self):
        """file tablosundan dosya adlarını çeker."""
        self.cursor.execute("SELECT fileName FROM File") 
        return [row[0] for row in self.cursor.fetchall()] 

    def add_file(self, filename):
        """Yeni bir dosya ekler."""
        self.cursor.execute("INSERT INTO File (filename) VALUES (?)", (filename,))
        self.conn.commit()

    def delete_last_file(self):
        """Son dosyayı siler."""
        self.cursor.execute("DELETE FROM file WHERE id = (SELECT MAX(id) FROM file)")
        self.conn.commit()
