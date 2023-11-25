import unittest
import sqlite3
from datetime import datetime
from src.DAO.StationDAO import StationDAO
import json

class TestStationDAO(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect('src.BDD.BDD.sql')  # Utilisez une base de données en mémoire pour les tests
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE Station (id TEXT PRIMARY KEY, nom_station TEXT, capacite INTEGER, coordonnees_station TEXT, id_commune TEXT, en_fonctionnement TEXT, date_deb TEXT, date_fin TEXT, borne_paiement TEXT, nb_bornettes INTEGER)")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_create_and_read(self):
        dao = StationDAO(self.conn)

        # Création d'une station pour le test
        station_data = {'stationcode': '75001', 'name': 'Station Test', 'capacity': 10, 'coordonnees_geo': [2.3522, 48.8566], 'is_renting': 'True', 'duedate': '2023-01-01', 'nom_arrondissement_communes': 'Paris 1er'}
        dao.create2(station_data)

        # Vérification de la création
        self.cur.execute("SELECT * FROM Station WHERE id=?", ('75001',))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result, ('75001', 'Station Test', 10, json.dumps([2.3522, 48.8566]), '75001', 'True', 'date_deb 75001', '2023-01-01', 'borne_paiement 75001', 10))

        # Test de la méthode read
        station = dao.read('75001')
        self.assertIsNotNone(station)
        self.assertEqual(station, ('75001', 'Station Test', 10, json.dumps([2.3522, 48.8566]), '75001', 'True', 'date_deb 75001', '2023-01-01', 'borne_paiement 75001', 10))

    def test_update_and_delete(self):
        dao = StationDAO(self.conn)

        # Création d'une station pour le test
        station_data = {'stationcode': '75001', 'name': 'Station Test', 'capacity': 10, 'coordonnees_geo': [2.3522, 48.8566], 'is_renting': 'True', 'duedate': '2023-01-01', 'nom_arrondissement_communes': 'Paris 1er'}
        dao.create2(station_data)

        # Test de la méthode update
        dao.update2({'stationcode': '75001', 'name': 'New Station', 'capacity': 15, 'coordonnees_geo': [2.3522, 48.8566], 'is_renting': 'False', 'duedate': '2023-02-01', 'nom_arrondissement_communes': 'Paris 1er'})
        updated_station = dao.read('75001')
        self.assertIsNotNone(updated_station)
        self.assertEqual(updated_station, ('75001', 'New Station', 15, json.dumps([2.3522, 48.8566]), '75001', 'False', 'date_deb 75001', '2023-02-01', 'borne_paiement 75001', 15))

        # Test de la méthode delete
        dao.delete('75001')
        deleted_station = dao.read('75001')
        self.assertIsNone(deleted_station)

    def test_upsert2(self):
        dao = StationDAO(self.conn)

        # Création d'une station pour le test
        station_data = {'stationcode': '75001', 'name': 'Station Test', 'capacity': 10, 'coordonnees_geo': [2.3522, 48.8566], 'is_renting': 'True', 'duedate': '2023-01-01', 'nom_arrondissement_communes': 'Paris 1er'}
        dao.upsert2(station_data)

        # Test de la méthode upsert2 pour la mise à jour
        dao.upsert2({'stationcode': '75001', 'name': 'New Station', 'capacity': 15, 'coordonnees_geo': [2.3522, 48.8566], 'is_renting': 'False', 'duedate': '2023-02-01', 'nom_arrondissement_communes': 'Paris 1er'})
        updated_station = dao.read('75001')
        self.assertIsNotNone(updated_station)
        self.assertEqual(updated_station, ('75001', 'New Station', 15, json.dumps([2.3522, 48.8566]), '75001', 'False', 'date_deb 75001', '2023-02-01', 'borne_paiement 75001', 15))

        # Test de la méthode upsert2 pour l'insertion
        dao.upsert2({'stationcode': '75002', 'name': 'Station 2', 'capacity': 20, 'coordonnees_geo': [2.3522, 48.8566], 'is_renting': 'True', 'duedate': '2023-03-01', 'nom_arrondissement_communes': 'Paris 2ème'})
        new_station = dao.read('75002')
        self.assertIsNotNone(new_station)
        self.assertEqual(new_station, ('75002', 'Station 2', 20, json.dumps([2.3522, 48.8566]), '75002', 'True', 'date_deb 75002', '2023-03-01', 'borne_paiement 75002', 20))  

    def test_close(self):
        # On s'assure que la connexion est ouverte avant de fermer
        assert self.conn is not None

        # Utilisation de la méthode close pour fermer la connexion
        self.conn.close()

        # On s'assure que la connexion est fermée après l'appel à close
        assert self.conn is None


if __name__ == '__main__':
    unittest.main()