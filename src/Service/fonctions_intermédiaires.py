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

# def codeInsee_to_code(stationcode):  #renvoie 75xxx si 75 est le début de station code et deux premiers caractères de station code sinon
#     if len(stationcode) == 5:
#         return stationcode[:2]  # Les deux premiers caractères
#     elif len(stationcode) == 4: #cas id_station est un arrondissement de paris de 1 à 9
#         return stationcode[0]   # Seulement le premier caractère
#     else:
#         # Gérer d'autres cas si nécessaire
#         return None
         
def codeInsee_to_code(stationcode):  #renvoie 75xxx si 75 est le début de station code et deux premiers caractères de station code sinon
    if len(stationcode) == 5:
        if stationcode[:2]=='75':
            return stationcode[2:]
        return stationcode
    else:                    #cas id_station est un arrondissement de paris de 1 à 9 longueur 
        return '00'+stationcode[0]   # Seulement le premier caractère
    
         

def afficher_nom_commune_complete(stationcode,nom_arrondissement_commune):#testp
    if len(codeInsee_to_code(stationcode)) == 3 :
        return f"Paris arrondissement :  {codeInsee_to_code(stationcode)}"
    else :
        return nom_arrondissement_commune


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

import sqlite3

def list_tables(db_path):
    """
    List all tables in the SQLite database.

    Args:
    db_path (str): Path to the SQLite database file.

    Returns:
    list: A list of table names.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Close the connection
    conn.close()

    # Extracting table names from the tuples
    return [table[0] for table in tables]

# Example usage
# db_path = 'your_database_file.db'  # Replace with your database file path
# print(list_tables(db_path))
# liste_tables("C:/Users/jerem/OneDrive/Documents/GitHub/Projet_info_2A/Projet_info_2A-7/src/BDD/BDD.sql")

def get_frequencies(db_path):
    """
    Get the frequencies of all records in the StationFaits table.

    Args:
    db_path (str): Path to the SQLite database file.

    Returns:
    list: A list of frequencies.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT frequence FROM StationFaits;")
    frequencies = cursor.fetchall()

    # Close the connection
    conn.close()

    # Extracting frequency values from the tuples
    return [frequency[0] for frequency in frequencies]