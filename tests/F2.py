""" Version 1
import requests
import pandas as pd
import json

# Faire une requête à l'API pour obtenir les données de fréquentation
api_url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel'

try:
    # Faire la requête
    response = requests.get(api_url)

    # Vérifier que la requête a réussi
    if response.status_code == 200:
        data = json.load(response)

        # Convertir les données JSON en un DataFrame Pandas
        df = pd.DataFrame(data)

        # Grouper les données par station et calculer la fréquentation totale
        station_frequentation = df.groupby('stationcode')['numbikesavailable'].sum()

        # Trouver la station la moins fréquentée
        station_moins_frequente = station_frequentation.idxmin()

        print("La station la moins fréquentée est :", station_moins_frequente)
    else:
        # Échec de la requête à l'API
        print("Échec de la requête à l'API. Code de statut :", response.status_code)
except requests.exceptions.RequestException as e:
    print("Erreur lors de la requête à l'API :", e)
"""
"""Version 2
import urllib.request
import json
import pandas as pd

# Faire une requête à l'API pour obtenir les données de fréquentation
api_url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel'

# Créer un objet Request
request = urllib.request.Request(api_url)

# Faire la requête et obtenir la réponse
response = urllib.request.urlopen(request)

# Lire la réponse
data = json.loads(response.read())

# Convertir les indices en entiers
for index, station in enumerate(data):
    station_code = int(station['stationcode'])
    data[index]['stationcode'] = station_code

# Supprimer les stations qui n'ont pas de vélos disponibles
data = [station for station in data if station['numbikesavailable'] > 0]

# Convertir la réponse JSON en un DataFrame Pandas
df = pd.DataFrame(data)

# Grouper les données par station et calculer la fréquentation totale
station_frequentation = df.groupby('stationcode')['numbikesavailable'].sum()

# Trouver la station la moins fréquentée
station_moins_frequente = station_frequentation.idxmin()

print("La station la moins fréquentée est :", station_moins_frequente)
"""

import urllib.request
import json
import pandas as pd

##############################################requete 1######################################################


# Faire une requête à l'API pour obtenir les données de fréquentation
api_url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel'

# Créer un objet Request
request = urllib.request.Request(api_url)

# Faire la requête et obtenir la réponse
response = urllib.request.urlopen(request)

# Lire la réponse
data = json.loads(response.read())

# Convertir la réponse JSON en un DataFrame Pandas
df = pd.DataFrame(data)

# Grouper les données par station et calculer la fréquentation totale
station_frequentation = df.groupby('stationcode')['numbikesavailable'].sum()

# Trouver la station la moins fréquentée
station_moins_frequente = station_frequentation.idxmin()

print("La station la moins fréquentée est :", station_moins_frequente)







############################################## requete 2 code chatgpt (requete sql validé par charles)############################
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('votre_base_de_donnees.db')  # Remplacez avec le nom de votre base de données

# Création d'un curseur pour exécuter les requêtes
cursor = conn.cursor()

# Requête SQL pour obtenir la station la moins fréquentée à partir de date_debut et date_fin les dates fournies par l'utilisateur
query = '''
    SELECT s.nom_station
    FROM StationFaits sf
    JOIN station s ON sf.id_station = s.id_station
    WHERE sf.date_fait_deb >= 'date_debut' AND sf.date_fait_fin <= 'date_fin'
    GROUP BY s.nom_station
    ORDER BY SUM(sf.frequence) ASC
    LIMIT 1;
'''

# Exécution de la requête
cursor.execute(query)

# Récupération du résultat
result = cursor.fetchone()

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()

# Affichage du résultat
if result:
    print(f"La station la moins fréquentée est : {result[0]}")
else:
    print("Aucun résultat trouvé.")
