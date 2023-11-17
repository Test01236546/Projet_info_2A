import pytest
from Service.commune import Commune


@pytest.fixture
def test_commune_init():
    # Vérification que l'initialisation de la commune fonctionne correctement
    commune = Commune("75001", "Paris")
    assert commune.id_commune == "75001"
    assert commune.nom_commune == "Paris"
    assert isinstance(commune.id_commune, str)  # Vérifie que id_commune est une chaîne de caractères
    assert commune.id_commune.isdigit()  # Vérifie que id_commune contient uniquement des chiffres
    assert isinstance(commune.nom_commune, str)  # Vérifie que nom_commune est une chaîne de caractères
    assert commune.nom_commune.isalpha()  # Vérifie que nom_commune contient uniquement des caractères alphabétiques

def test_commune_repr():
    # Vérification que la représentation de la commune fonctionne correctement
    commune = Commune("75001", "Paris")
    assert repr(commune) == "Commune(id=75001, nom=Paris)"