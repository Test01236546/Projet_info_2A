import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
from src.Service.StationFaits import StationFaits
import re

@pytest.fixture
def station_faits():
    # Exemple de valeurs factices pour les tests
    id_station = "1"
    nb_bornettes = 10
    velos_dispos = 5
    meca_dispo = 3
    elec_dispo = 2
    retour_velo = True
    frequence = 10
    date_fait_deb = "2023-01-01T00:00:00+00:00"
    date_fait_fin = "2023-01-10T23:59:59+00:00"

    return StationFaits(
        id_station=id_station,
        nb_bornettes=nb_bornettes,
        velos_dispos=velos_dispos,
        meca_dispo=meca_dispo,
        elec_dispo=elec_dispo,
        retour_velo=retour_velo,
        frequence=frequence,
        date_fait_deb=date_fait_deb,
        date_fait_fin=date_fait_fin
    )


def test_station_init(station_faits):
    # Vérification des attributs
    assert station_faits.id_station == "1"
    assert station_faits.nb_bornettes == 10
    assert station_faits.velos_dispos == 5
    assert station_faits.meca_dispo == 3
    assert station_faits.elec_dispo == 2
    assert station_faits.retour_velo is True
    assert station_faits.frequence == 10
    assert station_faits.date_fait_deb == "2023-01-01T00:00:00+00:00"
    assert station_faits.date_fait_fin == "2023-01-10T12:30:00+00:00"

    # Vérification des types des attributs
    assert isinstance(station_faits.id_station, str)
    assert isinstance(station_faits.nb_bornettes, int)
    assert isinstance(station_faits.velos_dispos, int)
    assert isinstance(station_faits.meca_dispo, int)
    assert isinstance(station_faits.elec_dispo, int)
    assert isinstance(station_faits.retour_velo, bool)
    assert isinstance(station_faits.frequence, int)
    assert isinstance(station_faits.date_fait_deb, str)
    assert isinstance(station_faits.date_fait_fin, str)

    assert station_faits.id_station.isdigit()
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", station_faits.date_fait_debut)
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", station_faits.date_fait_fin)


def test_calcul_frequence(station_faits):
    # Création d'une StationFaits précédente pour le test
    former_station_faits = StationFaits(
        id_station="1",
        nb_bornettes=10,
        velos_dispos=5,
        meca_dispo=3,
        elec_dispo=2,
        retour_velo=True,
        frequence=5,  # La fréquence précédente
        date_fait_deb = "2023-01-01T00:00:00+00:00",
        date_fait_fin = "2023-01-10T12:30:00+00:00"
    )

    # Appel de la méthode calcul_frequence
    result = station_faits.calcul_frequence(former_station_faits)

    # Vérification que la fréquence est correctement calculée
    assert result == abs(station_faits.meca_dispo + station_faits.elec_dispo - (former_station_faits.meca_dispo + former_station_faits.elec_dispo))

def test_str_representation(station_faits):
    # Appel de la méthode __str__
    result = str(station_faits)

    # Vérifiecation que la représentation sous forme de chaîne de caractères est correcte
    assert result == f"StationFaits(id={station_faits.id_station}, 
                        nb_bornettes={station_faits.nb_bornettes}, 
                        velos_dispos={station_faits.velos_dispos},
                        meca_dispo={station_faits.meca_dispo}, 
                        elec_dispo={station_faits.elec_dispo}, 
                        retour_velo={station_faits.retour_velo}, 
                        frequence={station_faits.frequence}, 
                        date_fait_deb={station_faits.date_fait_deb}, 
                        date_fait_fin={station_faits.date_fait_fin})"