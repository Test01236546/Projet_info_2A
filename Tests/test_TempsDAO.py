import unittest
from src.DAO.TempsDAO import TempsDAO, tp

class TestTempsDAO(unittest.TestCase):
    def setUp(self):
        # Initialisation des données nécessaires pour les tests.
        self.dao = TempsDAO("src.BDD.BDD.sql")

    def tearDown(self):
        # On s'assure que la connexion est fermée après chaque test.
        self.dao.close()

    def test_create(self):
        temps = tp.Temps("id_temps_test", "2023-11-16T12:30:00", 2023, 11, 16, 12, 30)
        self.dao.create(temps)
        result = self.dao.read("id_temps_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_temps_test", "2023-11-16T12:30:00", 2023, 11, 16, 12, 30))

    def test_create2(self):
        temps_dict = {
            "id_temps": "id_temps_test",
            "duedate": "2023-11-16T12:30:00"
        }
        self.dao.create2(temps_dict)
        result = self.dao.read("id_temps_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_temps_test", "2023-11-16T12:30:00", 2023, 11, 16, 12, 30))

    def test_read(self):
        id_temps = "id_temps_test"
        result = self.dao.read(id_temps)
        self.assertIsNone(result)

    def test_update(self):
        id_temps = "id_temps_test"
        new_data = tp.Temps(id_temps, "2023-11-16T14:45:00", 2023, 11, 16, 14, 45)
        self.dao.update(id_temps, new_data)
        result = self.dao.read("id_temps_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_temps_test", "2023-11-16T14:45:00", 2023, 11, 16, 14, 45))

    def test_update2(self):
        temps_dict = {
            "id_temps": "id_temps_test",
            "duedate": "2023-11-16T14:45:00"
        }
        self.dao.update2(temps_dict)
        result = self.dao.read("id_temps_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_temps_test", "2023-11-16T14:45:00", 2023, 11, 16, 14, 45))

    def test_delete(self):
        id_temps = "id_temps_test"
        self.dao.delete(id_temps)
        result = self.dao.read("id_temps_test")
        self.assertIsNone(result)  # Comme le temps a été supprimé

    def test_upsert2(self):
        temps_dict = {
            "id_temps": "id_temps_test",
            "duedate": "2023-11-16T14:45:00"
        }
        self.dao.upsert2(temps_dict)
        result = self.dao.read("id_temps_test")
        self.assertIsNotNone(result)
        self.assertEqual(result, ("id_temps_test", "2023-11-16T14:45:00", 2023, 11, 16, 14, 45))

    def test_close(self):
        # On s'assure que la connexion est ouverte avant de fermer
        assert self.dao.conn is not None

        # Utilisation de la méthode close pour fermer la connexion
        self.dao.close()

        # On s'assure que la connexion est fermée après l'appel à close
        assert self.dao.conn is None

if __name__ == '__main__':
    unittest.main()