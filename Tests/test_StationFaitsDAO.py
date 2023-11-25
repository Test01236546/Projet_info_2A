import unittest
from src.DAO.StationFaitsDAO import StationFaitsDAO, stf

class TestStationFaitsDAO(unittest.TestCase):
    def setUp(self):
        # Initialisation des objets ou des données nécessaires pour les tests.
        self.dao = StationFaitsDAO("src.BDD.BDD.sql")

    def tearDown(self):
        # On s'assure que la connexion est fermée après chaque test.
        self.dao.close()

    def test_create(self):
        station_faits = stf.StationFaits("id_station_test", 10, 5, 3, 2, True, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00")
        self.dao.create(station_faits)
        result = self.dao.read("id_station_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_station_test", 10, 5, 3, 2, True, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00"))

    def test_create2(self):
        station_faits_dict = {
            "stationcode": "id_station_test",
            "capacity": 10,
            "numbikesavailable": 5,
            "mechanical": 3,
            "ebike": 2,
            "is_returning": True,
            "duedate": "2023-11-16T00:00:00"
        }
        self.dao.create2(station_faits_dict)
        result = self.dao.read("id_station_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_station_test", 10, 5, 3, 2, True, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00"))

    def test_read(self):
        id_station = "id_station_test"
        result = self.dao.read(id_station)
        self.assertIsNone(result)  # Comme la station_faits n'existe pas encore

    def test_update(self):
        id_station = "id_station_test"
        new_data = stf.StationFaits(id_station, 8, 4, 2, 1, False, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00")
        self.dao.update(id_station, new_data)
        result = self.dao.read("id_station_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_station_test", 8, 4, 2, 1, False, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00"))

    def test_update2(self):
        station_faits_dict = {
            "stationcode": "id_station_test",
            "capacity": 8,
            "numbikesavailable": 4,
            "mechanical": 2,
            "ebike": 1,
            "is_returning": False,
            "duedate": "2023-11-16T00:00:00"
        }
        self.dao.update2(station_faits_dict)
        result = self.dao.read("id_station_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_station_test", 8, 4, 2, 1, False, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00"))

    def test_delete(self):
        id_station = "id_station_test"
        self.dao.delete(id_station)
        result = self.dao.read("id_station_test")
        self.assertIsNone(result)  # Comme la station_faits a été supprimée

    def test_upsert2(self):
        station_faits_dict = {
            "stationcode": "id_station_test",
            "capacity": 8,
            "numbikesavailable": 4,
            "mechanical": 2,
            "ebike": 1,
            "is_returning": False,
            "duedate": "2023-11-16T00:00:00"
        }
        self.dao.upsert2(station_faits_dict)
        result = self.dao.read("id_station_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_station_test", 8, 4, 2, 1, False, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00"))

    def test_close(self):
        # On s'assure que la connexion est ouverte avant de fermer
        assert self.dao.conn is not None

        # Utilisation de la méthode close pour fermer la connexion
        self.dao.close()

        # On s'assure que la connexion est fermée après l'appel à close
        assert self.dao.conn is None

if __name__ == '__main__':
    unittest.main()