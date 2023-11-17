import pytest
import time
import sqlite3
from Service.fonctions_intermédiaires import no_print_map, no_print_map2, periodic, voir_ids_disponibles, compter_ids, codeInsee_to_code, afficher_nom_commune_complete, trouver_premiere_derniere_heure

@pytest.fixture
def temp_db_path(tmp_path):
    return str(tmp_path / "temp_db.sqlite")

def test_no_print_map():
    # Vérification que la fonction no_print_map ne provoque pas d'erreur
    map_ex = map(lambda x: x**2, [1, 2, 3])
    no_print_map(map_ex)

def test_no_print_map2():
    # Vérification que la fonction no_print_map2 ne provoque pas d'erreur
    map_ex = map(lambda x: x**2, [1, 2, 3])
    no_print_map2(map_ex)

def test_periodic(temp_db_path):
    # Création d'une instance factice de Service pour l'ingestion
    instance_service = Service()

    # Création d'une base de données SQLite temporaire pour le test
    duration = 0.1  # 0.1 seconde pour le test
    pause = 0.01    # 0.01 seconde pour le test
    periodic(instance_service, duration, pause)

    # Ajout des assertions en fonction du comportement attendu de votre fonction

def test_voir_ids_disponibles(temp_db_path):
    # Création d'une base de données SQLite temporaire avec quelques données
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Station (id INTEGER PRIMARY KEY);")
    cursor.execute("INSERT INTO Station (id) VALUES (1), (2), (3);")
    conn.commit()

    # Appel de la fonction et vérifier le résultat
    ids = voir_ids_disponibles(temp_db_path, 2)
    assert ids == [(1,), (2,)]

def test_compter_ids(temp_db_path):
    # Création d'une base de données SQLite temporaire avec quelques données
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Station (id INTEGER PRIMARY KEY);")
    cursor.execute("INSERT INTO Station (id) VALUES (1), (2), (3);")
    conn.commit()

    # Appel de la fonction et vérifier le résultat
    nombre_ids = compter_ids(temp_db_path, 'Station', 'id')
    assert nombre_ids == 3

def test_codeInsee_to_code():
    # Vérification le comportement de la fonction pour différents cas
    assert codeInsee_to_code("75001") == "75"
    assert codeInsee_to_code("75100") == "75"
    assert codeInsee_to_code("750") is None

def test_afficher_nom_commune_complete():
    # Vérification que le comportement de la fonction pour différents cas
    assert afficher_nom_commune_complete("75001", "Nom Commune") == "Paris arrondissement : 75"
    assert afficher_nom_commune_complete("91000", "Nom Commune") == "Nom Commune"

def test_trouver_premiere_derniere_heure(temp_db_path):
    # Création d'une base de données SQLite temporaire avec quelques données
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Temps (id INTEGER PRIMARY KEY, time_column TEXT);")
    cursor.execute("INSERT INTO Temps (time_column) VALUES ('2023-01-01'), ('2023-01-02'), ('2023-01-03');")
    conn.commit()

    # Appel de la fonction et vérifier le résultat
    premiere_heure, derniere_heure = trouver_premiere_derniere_heure(temp_db_path, 'Temps', 'time_column')
    assert premiere_heure == '2023-01-01'
    assert derniere_heure == '2023-01-03'