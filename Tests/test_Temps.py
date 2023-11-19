import pytest
from datetime import datetime
from Service.temps import Temps

@pytest.fixture
def temps_instance():
    # Exemple de valeurs factices pour les tests
    id_temps = 1
    date = datetime(2023, 1, 1, 12, 30)
    annee, mois, jour, heure, minute = 2023, 1, 1, 12, 30

    return Temps(
        id_temps=id_temps,
        date=date,
        annee=annee,
        mois=mois,
        jour=jour,
        heure=heure,
        minute=minute
    )


def test_station_init(temps_instance):
    # Vérification des attributs
    assert temps_instance.id_temps == "1"
    assert temps_instance.date == 10
    assert temps_instance.annee == 2023
    assert temps_instance.mois == 6
    assert temps_instance.jour == 26
    assert temps_instance.heure == 17
    assert temps_instance.minute == 00

    # Vérification des types des attributs
    assert isinstance(temps_instance.id_temps, int)
    assert isinstance(temps_instance.date, str)
    assert isinstance(temps_instance.annee, int)
    assert isinstance(temps_instance.mois, int)
    assert isinstance(temps_instance.jour, int)
    assert isinstance(temps_instance.heure, int)
    assert isinstance(temps_instance.minute, int)

    assert temps_instance.id_temps.isdigit()

def test__repr__(temps_instance):
    # Appel de la méthode __repr__
    result = repr(temps_instance)

    # Vérification que la représentation sous forme de chaîne de caractères est correcte
    assert result == f"Temps(id_temps={temps_instance.id_temps}, 
                        date={temps_instance.date}, 
                        annee={temps_instance.annee}, 
                        mois={temps_instance.mois}, 
                        jour={temps_instance.jour}, 
                        heure={temps_instance.heure}, 
                        minute={temps_instance.minute})"