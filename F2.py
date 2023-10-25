"""
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
"""
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