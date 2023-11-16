import pytest
from datetime import datetime, timedelta
from Service.Fonctionnalites import Fonctionnalites

class TestFonctionnalites :
    
    @pytest.fixture
    def fonctionnalites():
        return Fonctionnalites()

    def test_recup_stations():
        # Utilisation de la fonction recup_stations
        fonctionnalites = Fonctionnalites()
        stations = fonctionnalites.recup_stations()

        # Vérification que la liste des stations n'est pas vide
        assert stations

    def test_F1():
        # Utilisation de la fonction F1
        fonctionnalites = Fonctionnalites()

        # Adresse factice pour le test
        address = "Paris, France"
        
        # Appel de la fonction F1
        result = fonctionnalites.F1(address)

        # Vérification que le résultat n'est pas vide
        assert result

    def test_F2():
        # Utilisation de la fonction F2
        fonctionnalites = Fonctionnalites()

        # Dates factices pour le test
        date_debut = "2023-01-01"
        date_fin = "2023-01-10"
        
        # Appel de la fonction F2
        result = fonctionnalites.F2(date_debut, date_fin)

        # Vérification que le résultat n'est pas vide
        assert result

    def test_F3():
        # Utilisation de la fonction F3
        fonctionnalites = Fonctionnalites()

        # Dates factices pour le test
        date_debut = "2023-01-01"
        date_fin = "2023-01-10"
        
        # Appel de la fonction F3
        result = fonctionnalites.F3(date_debut, date_fin)

        # Vérification que le résultat n'est pas vide
        assert result