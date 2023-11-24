import unittest
from DAO.StationFaitsDAO import StationFaitsDAO, stf

class TestStationFaitsDAO(unittest.TestCase):
    def setUp(self):
        # Vous pouvez initialiser ici des objets ou des données nécessaires pour les tests.
        pass

    def tearDown(self):
        # Vous pouvez effectuer des opérations de nettoyage ici, si nécessaire.
        pass

    def test_create(self):
        dao = StationFaitsDAO("votre_chemin_de_bdd")
        station_faits = stf.StationFaits("id_station_test", 10, 5, 3, 2, True, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00")

        dao.create(station_faits)

        # Ajoutez des assertions pour vérifier que la station_faits a bien été créée dans la base de données
        # ...

    def test_create2(self):
        dao = StationFaitsDAO("votre_chemin_de_bdd")
        station_faits_dict = {
            "stationcode": "id_station_test",
            "capacity": 10,
            "numbikesavailable": 5,
            "mechanical": 3,
            "ebike": 2,
            "is_returning": True,
            "duedate": "2023-11-16T00:00:00"
        }

        dao.create2(station_faits_dict)

        # Ajoutez des assertions pour vérifier que la station_faits a bien été créée dans la base de données
        # ...

    def test_read(self):
        dao = StationFaitsDAO("votre_chemin_de_bdd")
        id_station = "id_station_test"

        result = dao.read(id_station)

        # Ajoutez des assertions pour vérifier que le résultat correspond à ce que vous attendez
        # ...

    def test_update(self):
        dao = StationFaitsDAO("votre_chemin_de_bdd")
        id_station = "id_station_test"
        new_data = stf.StationFaits(id_station, 8, 4, 2, 1, False, "frequence_test", "2023-11-16T00:00:00", "2023-11-17T00:00:00")

        dao.update(id_station, new_data)

        # Ajoutez des assertions pour vérifier que la station_faits a bien été mise à jour dans la base de données
        # ...

    def test_update2(self):
        dao = StationFaitsDAO("votre_chemin_de_bdd")
        station_faits_dict = {
            "stationcode": "id_station_test",
            "capacity": 8,
            "numbikesavailable": 4,
            "mechanical": 2,
            "ebike": 1,
            "is_returning": False,
            "duedate": "2023-11-16T00:00:00"
        }

        dao.update2(station_faits_dict)

        # Ajoutez des assertions pour vérifier que la station_faits a bien été mise à jour dans la base de données
        # ...

    def test_delete(self):
        dao = StationFaitsDAO("votre_chemin_de_bdd")
        id_station = "id_station_test"

        dao.delete(id_station)

        # Ajoutez des assertions pour vérifier que la station_faits a bien été supprimée de la base de données
        # ...

    def test_upsert2(self):
        dao = StationFaitsDAO("votre_chemin_de_bdd")
        station_faits_dict = {
            "stationcode": "id_station_test",
            "capacity": 8,
            "numbikesavailable": 4,
            "mechanical": 2,
            "ebike": 1,
            "is_returning": False,
            "duedate": "2023-11-16T00:00:00"
        }

        dao.upsert2(station_faits_dict)

    def test_close(StationFaitsDAO):
        # Assurer que la connexion est ouverte avant de fermer
        assert StationFaitsDAO.conn is not None

        # Utilisation de la méthode close pour fermer la connexion
        StationFaitsDAO.close()

        # Assurer que la connexion est fermée après l'appel à close
        assert StationFaitsDAO.conn is None

if __name__ == '__main__':
    unittest.main()