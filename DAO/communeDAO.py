import sqlite3

class CommuneDAO:

    def __init__(self,path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self,commune):
        self.cur.execute("""
        INSERT INTO Commune VALUES (?, ?)
        """, (commune.id_commune, commune.nom_commune))
        self.conn.commit()
        print("Commune créée")

    def read(self, id_commune):
        self.cur.execute("SELECT * FROM Commune WHERE id_commune=?", (id_commune,))
        commune = self.cur.fetchone()
        if commune:
            print("Commune trouvée:", commune)
            return commune
            # return Commune(*commune_data) si on ne manipulait pas déja des communes
        else:
            print("Commune non trouvée")
            return None

    def update(self, id_commune, new_data):
        self.cur.execute("""
        UPDATE Commune SET nom_commune=? WHERE id_commune=?
        """, (new_data.nom_commune, id_commune))
        self.conn.commit()
        print("Commune mise à jour")

    def delete(self, id_commune):
        self.cur.execute("DELETE FROM Commune WHERE id_commune=?", (id_commune,))
        self.conn.commit()
        print("Commune supprimée")


