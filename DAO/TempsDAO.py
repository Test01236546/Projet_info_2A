
import sqlite3

class TempsDAO:
    TABLE_NAME = "Temps"

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create(self, temps):
        self.cur.execute(f"""
        INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (temps.id_temps, temps.date, temps.annee, temps.mois, temps.jour, temps.heure, temps.minute))
        self.conn.commit()
        print("Temps créé")

    def read(self, id_temps):
        self.cur.execute(f"SELECT * FROM {self.TABLE_NAME} WHERE id_temps=?", (id_temps,))
        temps_data = self.cur.fetchone()
        if temps_data:
            print("Temps trouvé:", temps_data)
            return temps_data
        else:
            print("Temps non trouvé")
            return None

    def update(self, id_temps, new_data):
        self.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET date=?, annee=?, mois=?, jour=?, heure=?, minute=? WHERE id_temps=?
        """, (new_data.date, new_data.annee, new_data.mois, new_data.jour, new_data.heure, new_data.minute, id_temps))
        self.conn.commit()
        print("Temps mis à jour")

    def delete(self, id_temps):
        self.cur.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id_temps=?", (id_temps,))
        self.conn.commit()
        print("Temps supprimé")

    def close(self):
        self.conn.close()
