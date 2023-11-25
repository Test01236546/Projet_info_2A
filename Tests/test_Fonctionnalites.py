import pytest
import re
from datetime import datetime, timedelta
from src.Service.Fonctionnalites import Fonctionnalites

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

        # Vérification que address est une chaîne de caractères
        assert isinstance(address, str)


    def test_F2():
        # Utilisation de la fonction F2
        fonctionnalites = Fonctionnalites()

        # Dates factices pour le test
        date_debut = "2023-01-01T00:00:00+00:00"
        date_fin = "2023-01-10T23:59:59+00:00"
        
        # Appel de la fonction F2
        result = fonctionnalites.F2(date_debut, date_fin)

        # Vérification que le résultat n'est pas vide
        assert result

        # Vérification que address est une chaîne de caractères au format "AAAA-MM-DDTHH:NN:SS+00:00"
        assert isinstance(date_debut, str)
        assert isinstance(date_fin, str)
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", date_debut)
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", date_fin)


    def test_F3():
        # Utilisation de la fonction F3
        fonctionnalites = Fonctionnalites()

        # Dates factices pour le test
        date_debut = "2023-01-01T00:00:00+00:00"
        date_fin = "2023-01-10T23:59:59+00:00"

        # Appel de la fonction F3
        result = fonctionnalites.F3(date_debut, date_fin)

        # Vérification que le résultat n'est pas vide
        assert result

        # Vérification que address est une chaîne de caractères au format "AAAA-MM-DDTHH:NN:SS+00:00"
        assert isinstance(date_debut, str)
        assert isinstance(date_fin, str)
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", date_debut)
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", date_fin)
