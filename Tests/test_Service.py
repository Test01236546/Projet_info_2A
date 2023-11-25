import pytest
from unittest.mock import Mock
from src.Service.Service import Service

@pytest.fixture
def service_instance():
    return Service()

# Mock pour la réponse de l'API
@pytest.fixture
def mock_api_response():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'results': [
            # Exemple de données de station pour les tests
            {'stationcode': '001', 'name': 'Test Station 1', 'capacity': 10, 'coordonnees_geo': {'latitude': 123.456, 'longitude': 789.012}, 'is_renting': True, 'duedate': '2023-01-01'},
            {'stationcode': '002', 'name': 'Test Station 2', 'capacity': 15, 'coordonnees_geo': {'latitude': 111.222, 'longitude': 333.444}, 'is_renting': False, 'duedate': '2023-02-01'},
        ]
    }
    return mock_response

# Mock pour remplacer les méthodes DAO
@pytest.fixture
def mock_dao_methods(monkeypatch):
    monkeypatch.setattr('chemin.vers.votre.classe.StationDAO.upsert2', Mock())
    monkeypatch.setattr('chemin.vers.votre.classe.CommuneDAO.upsert2', Mock())
    monkeypatch.setattr('chemin.vers.votre.classe.TempsDAO.upsert2', Mock())
    monkeypatch.setattr('chemin.vers.votre.classe.StationFaitsDAO.upsert2', Mock())

def test_ingest_calls_dao_methods(service_instance, mock_api_response, mock_dao_methods):
    # Remplacez 'Service.url' par l'URL de l'API que vous utilisez dans votre test
    service_instance.url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"

    # Mock pour remplacer la méthode requests.get
    with pytest.MonkeyPatch().context() as m:
        m.setattr('requests.get', lambda x: mock_api_response)

        # Exécution de la méthode ingest
        service_instance.ingest()

    # Vérification que les méthodes DAO appropriées ont été appelées
    assert service_instance.Instance_StationDAO.upsert2.call_count == 2  # Remplacez le nombre d'appels en fonction de votre nombre de stations
    assert service_instance.Instance_CommuneDAO.upsert2.call_count == 2  # Remplacez le nombre d'appels en fonction de votre nombre de stations
    assert service_instance.Instance_TempsDAO.upsert2.call_count == 2  # Remplacez le nombre d'appels en fonction de votre nombre de stations
    assert service_instance.Instance_StationFaitsDAO.upsert2.call_count == 2  # Remplacez le nombre d'appels en fonction de votre nombre de stations