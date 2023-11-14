import time
import sqlite3


#Regarder la complexité de ces deux fonctions

def no_print_map(map_ex):
        result = list(map_ex)
    
# no_print_map(map_ex)

def no_print_map2(map_ex):
        result = map_ex
        for _ in result:
            pass  # Ne rien faire dans la boucle

def periodic(Instance_service,duration, pause):
    start_time = time.time()
    while time.time() - start_time < duration:
        Instance_service.ingest()
        time.sleep(pause)

def voir_ids_disponibles(db_path, nombre_ids):
    # Ouvrir la connexion à la base de données
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Exécuter la requête pour obtenir les 'id'
    query = "SELECT id FROM Station LIMIT ?"
    cursor.execute(query, (nombre_ids,))

    # Récupérer les résultats
    ids = cursor.fetchall()

    # Fermer la connexion
    conn.close()

    return ids

def compter_ids(db_path, table_name,primary_key):
    # Ouvrir la connexion à la base de données
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Exécuter la requête pour compter les 'id'
    query = f"SELECT COUNT({primary_key}) FROM {table_name}"
    cursor.execute(query)

    # Récupérer le résultat
    nombre_ids = cursor.fetchone()[0]

    # Fermer la connexion
    conn.close()

    return nombre_ids

def codeInsee_to_code(stationcode):  #renvoie 75xxx si 75 est le début de station code et deux premiers caractères de station code sinon
    if len(stationcode) == 5:
        return stationcode[:2]  # Les deux premiers caractères
    elif len(stationcode) == 4: #cas id_station est un arrondissement de paris de 1 à 9
        return stationcode[0]   # Seulement le premier caractère
    else:
        # Gérer d'autres cas si nécessaire
        return None
         

def trouver_premiere_derniere_heure(db_path, table_name, time_column):
    # Ouvrir la connexion à la base de données
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Requête pour trouver la première heure (la plus ancienne)
    query_premiere_heure = f"SELECT MIN({time_column}) FROM {table_name}"
    cursor.execute(query_premiere_heure)
    premiere_heure = cursor.fetchone()[0]

    # Requête pour trouver la dernière heure (la plus récente)
    query_derniere_heure = f"SELECT MAX({time_column}) FROM {table_name}"
    cursor.execute(query_derniere_heure)
    derniere_heure = cursor.fetchone()[0]

    # Fermer la connexion
    conn.close()

    return premiere_heure, derniere_heure