import urllib.request
import json
import pandas as pd

# Faire une requête à l'API pour obtenir les données de fréquentation
start_date = '2023-10-25T00:00:00Z'
end_date = '2023-10-25T23:59:59Z'

api_url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel?q=timestamp%3E%27{}%27%20AND%20timestamp%3C%27{}%27'.format(start_date, end_date)
# Créer un objet Request
request = urllib.request.Request(api_url)

# Faire la requête et obtenir la réponse
response = urllib.request.urlopen(request)

# Lire la réponse
data = json.loads(response.read())

# Prétraiter les données JSON
# Supprimer les stations qui n'ont pas de vélos disponibles
data = [station for station in data if station['numbikesavailable'] > 0]

# Convertir les données JSON en un DataFrame Pandas
df = pd.DataFrame(data)

# Grouper les données par arrondissement et calculer la fréquentation totale
station_frequentation = df.groupby('arrondissement')['numbikesavailable'].sum()

# Trouver l'arrondissement avec la fréquentation totale la plus élevée
arrondissement_plus_frequente = station_frequentation.idxmax()

print("L'arrondissement le plus fréquenté sur la période est :", arrondissement_plus_frequente)