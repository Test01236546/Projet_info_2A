import pytest
import sqlite3

from Service.Station import Station
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

