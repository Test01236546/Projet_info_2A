import sqlite3

class CommuneDAO:

    def __init__(self,path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self):
        self.db_manager.cur.execute("""
        INSERT INTO Commune (id, nom) VALUES (?, ?)
        """, (commune.id, commune.nom))
        self.db_manager.conn.commit()
        print("Commune créée")

    def read(self, id):
        self.db_manager.cur.execute("SELECT * FROM Commune WHERE id=?", (id,))
        commune_data = self.db_manager.cur.fetchone()
        if commune_data:
            print("Commune trouvée:", commune_data)
            return Commune(*commune_data)
        else:
            print("Commune non trouvée")
            return None

    def update(self, id, new_data):
        self.db_manager.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET nom=?, population=? WHERE id=?
        """, (new_data.nom, new_data.population, id))
        self.db_manager.conn.commit()
        print("Commune mise à jour")

    def delete(self, id):
        self.db_manager.cur.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (id,))
        self.db_manager.conn.commit()
        print("Commune supprimée")


