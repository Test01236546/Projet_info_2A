import pytest
from Service.station import Station
import json
import re

@pytest.fixture
def station_instance():
    # Exemple de valeurs factices pour les tests
    id=1
    nom_station="Test Station"
    capacite=10
    coordonnees_station=json.dumps({"latitude": 123.456, "longitude": 789.012})
    id_commune=123
    en_fonctionnement=True,
    date_deb="2023-01-01T00:00:00+00:00"
    date_fin="2023-01-10T12:30:00+00:00"
    borne_paiement="borne_test"
    nb_bornettes=5

    return Station(
        id=id,
        nom_station=nom_station,
        capacite=capacite,
        coordonnees_station=coordonnees_station,
        id_commune=id_commune,
        en_fonctionnement=en_fonctionnement,
        date_deb=date_deb,
        date_fin=date_fin,
        borne_paiement=borne_paiement,
        nb_bornettes=nb_bornettes
    )


def test_station_init(station_instance):
    # Vérification des attributs
    assert station_instance.id == "1"
    assert station_instance.nom_station == "Test Station"
    assert station_instance.capacite == 10
    assert station_instance.coordonnees_station == json.dumps({"latitude": 123.456, "longitude": 789.012})
    assert station_instance.id_commune == "123"
    assert station_instance.en_fonctionnement is True
    assert station_instance.date_deb == "2023-01-01T00:00:00+00:00"
    assert station_instance.date_fin == "2023-01-10T12:30:00+00:00"
    assert station_instance.borne_paiement == "borne_test"
    assert station_instance.nb_bornettes == 5

    # Vérification des types des attributs
    assert isinstance(station_instance.id, str)
    assert isinstance(station_instance.nom_station, str)
    assert isinstance(station_instance.capacite, int)
    assert isinstance(station_instance.coordonnees_station, dict)
    assert isinstance(station_instance.id_commune, str)
    assert isinstance(station_instance.en_fonctionnement, bool)
    assert isinstance(station_instance.date_deb, str)
    assert isinstance(station_instance.date_fin, str)
    assert isinstance(station_instance.borne_paiement, str)
    assert isinstance(station_instance.nb_bornettes, int)

    assert station_instance.id.isdigit()
    assert station_instance.id_commune.isdigit()
    assert station_instance.nom_station.isalpha()
    assert station_instance.borne_paiement.isalpha()
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", station_instance.date_debut)
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", station_instance.date_fin)



def test_str_method_returns_station_info(station_instance):
    # Appel de la méthode __str__ et vérification si elle renvoie les informations attendues
    expected_output = "Station(id=1, nom_station=Test Station, capacite=10, coordonnees_station={'latitude': 123.456, 'longitude': 789.012},id_commune=Commune1, en_fonctionnement=True, date_deb=2023-01-01, date_fin=2023-01-31,borne_paiement=Borne1, nb_bornettes=5)"
    assert str(station_instance) == expected_output