import pytest
import sqlite3

from Service.station import Station
from DAO.StationDAO import StationDAO


class TestStationDAO:

    @pytest.fixture
    def station_dao(self):
        path = "test.db"
        station_dao = StationDAO(path)
        station_dao.create(Station(id="1", nom_station="Station 1", capacite=10, coordonnees_station="(1, 2)", id_commune="1", en_fonctionnement=True, date_deb="2023-01-01", date_fin="2023-12-31", borne_paiement="CB", nb_bornettes=2))
        station_dao.create(Station(id="2", nom_station="Station 2", capacite=20, coordonnees_station="(2, 3)", id_commune="2", en_fonctionnement=False, date_deb="2023-02-02", date_fin="2023-08-08", borne_paiement="CB", nb_bornettes=3))
        return station_dao

    def test_create(self, station_dao):
        station = Station(id="3", nom_station="Station 3", capacite=30, coordonnees_station="(3, 4)", id_commune="3", en_fonctionnement=True, date_deb="2023-03-03", date_fin="2023-09-09", borne_paiement="CB", nb_bornettes=4)
        station_dao.create(station)
        station_found = station_dao.read(station.id)
        assert station_found == (station.id, station.nom_station, station.capacite, station.coordonnees_station, station.id_commune, station.en_fonctionnement, station.date_deb, station.date_fin, station.borne_paiement, station.nb_bornettes)

    def test_read(self, station_dao):
        station_found = station_dao.read("1")
        assert station_found == (station_found.id, station_found.nom_station, station_found.capacite, station_found.coordonnees_station, station_found.id_commune, station_found.en_fonctionnement, station_found.date_deb, station_found.date_fin, station_found.borne_paiement, station_found.nb_bornettes)

    def test_update(self, station_dao):
        station = Station(id="1", nom_station="Station 1 modifiée", capacite=11, coordonnees_station="(1, 2)", id_commune="1", en_fonctionnement=True, date_deb="2023-01-01", date_fin="2023-12-31", borne_paiement="CB", nb_bornettes=2)
        station_dao.update(station.id, station)
        station_found = station_dao.read(station.id)
        assert station_found == (station.id, station.nom_station, station.capacite, station.coordonnees_station, station.id_commune, station.en_fonctionnement, station.date_deb, station.date_fin, station.borne_paiement, station.nb_bornettes)

    def test_delete(self, station_dao):
        station_dao.delete("1")
        station_found = station_dao.read("1")
        assert station_found is None

    

    def station_data():
        return {
            'stationcode': '001',
            'name': 'Test Station',
            'capacity': 10,
            'coordonnees_geo': {'latitude': 123.456, 'longitude': 789.012},
            'is_renting': True,
            'duedate': '2023-01-01'
        }

    def test_upsert2_insert(station_dao, station_data):
        # Assurer que la station n'existe pas initialement
        retrieved_station = station_dao.read(station_data['stationcode'])
        assert retrieved_station is None

        # Effectuer un upsert pour insérer une nouvelle station
        station_dao.upsert2(station_data)

        # Lecture de la station insérée depuis la base de données
        retrieved_station = station_dao.read(station_data['stationcode'])

        # Vérification que la station récupérée correspond aux données insérées
        assert retrieved_station[0] == station_data['stationcode']
        assert retrieved_station[1] == station_data['name']

    def test_upsert2_update(station_dao, station_data):
        # Création d'une nouvelle station
        station_dao.create2(station_data)

        # Maj des informations de la station
        updated_data = {
            'stationcode': '001',
            'name': 'Updated Station',
            'capacity': 15,
            'coordonnees_geo': {'latitude': 111.222, 'longitude': 333.444},
            'is_renting': False,
            'duedate': '2023-02-01'
        }
        station_dao.upsert2(updated_data)

        # lecture de la station maj depuis la base de données
        retrieved_station = station_dao.read(updated_data['stationcode'])

        # Vérification que la station récupérée correspond aux données maj
        assert retrieved_station[1] == updated_data['name']
    

    def test_close(station_dao):
        # Assurer que la connexion est ouverte avant de fermer
        assert station_dao.conn is not None

        # Utilisation de la méthode close pour fermer la connexion
        station_dao.close()

        # Assurer que la connexion est fermée après l'appel à close
        assert station_dao.conn is None