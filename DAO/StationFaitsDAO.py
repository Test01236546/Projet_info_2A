



import sqlite3

class StationFaitsDAO:
    TABLE_NAME = "StationFaitsDAO"

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create(self, station_faits):
        self.cur.execute(f"""
        INSERT INTO {self.TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (station_faits.id, station_faits.nb_bornettes, station_faits.velos_dispos, 
              station_faits.meca_dispo, station_faits.elec_dispo, station_faits.retour_velo, 
              station_faits.frequence, station_faits.date_fait_deb, station_faits.date_fait_fin))
        self.conn.commit()
        print("StationFaits créé")

    def read(self, id):
        self.cur.execute(f"SELECT * FROM {self.TABLE_NAME} WHERE id=?", (id,))
        station_faits_data = self.cur.fetchone()
        if station_faits_data:
            print("StationFaits trouvé:", station_faits_data)
            return StationFaits(*station_faits_data)
        else:
            print("StationFaits non trouvé")
            return None

    def update(self, id, new_data):
        self.cur.execute(f"""
        UPDATE {self.TABLE_NAME} SET nb_bornettes=?, velos_dispos=?, meca_dispo=?, elec_dispo=?, 
        retour_velo=?, frequence=?, date_fait_deb=?, date_fait_fin=? WHERE id=?
        """, (new_data.nb_bornettes, new_data.velos_dispos, new_data.meca_dispo, new_data.elec_dispo, 
              new_data.retour_velo, new_data.frequence, new_data.date_fait_deb, 
              new_data.date_fait_fin, id))
        self.conn.commit()
        print("StationFaits mis à jour")

    def delete(self, id):
        self.cur.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (id,))
        self.conn.commit()
        print("StationFaits supprimé")

    def close(self):
        self.conn.close()
