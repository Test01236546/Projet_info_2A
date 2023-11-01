import sqlite3

class CommuneDAO:

    def __init__(self,path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self,commune):
        self.cur.execute("""
        INSERT INTO Commune (id, nom) VALUES (?, ?)
        """, (commune.id, commune.nom))
        self.conn.commit()
        print("Commune créée")

    def read(self, id):
        self.cur.execute("SELECT * FROM Commune WHERE id=?", (id,))
        commune = self.cur.fetchone()
        if commune_data:
            print("Commune trouvée:", commune)
            return commune
            # return Commune(*commune_data) si on ne manipulait pas déja des communes
        else:
            print("Commune non trouvée")
            return None

    def update(self, id, new_data):
        self.cur.execute("""
        UPDATE Commune SET nom=? WHERE id=?
        """, (new_data.nom, id))
        self.conn.commit()
        print("Commune mise à jour")

    def delete(self, id):
        self.cur.execute("DELETE FROM Commune WHERE id=?", (id,))
        self.conn.commit()
        print("Commune supprimée")


