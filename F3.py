import urllib.request
import json
import pandas as pd

# Faire une requête à l'API pour obtenir les données de fréquentation
start_date = '2023-10-25T00:00:00Z'
end_date = '2023-10-25T23:59:59Z'

api_url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel?q=timestamp%3E%27{}%27%20AND%27{}%27'.format(start_date, end_date)

# Créer un objet Request
request = urllib.request.Request(api_url)

# Faire la requête et obtenir la réponse
response = urllib.request.urlopen(request)

# Lire la réponse
data = json.loads(response.read())

# Prétraiter les données JSON
# Supprimer les stations sans vélos disponibles
data = filter(lambda station: station.get('numbikesavailable', 0) > 0, data)
data = filter(lambda station: isinstance(station['numbikesavailable'], int) and int(station['numbikesavailable']) > 0, data)
# Convertir les données JSON en un DataFrame Pandas
df = pd.DataFrame(data)

# Grouper les données par arrondissement et calculer la fréquentation totale
station_frequentation = df.groupby('arrondissement')['numbikesavailable'].sum()

# Trouver l'arrondissement avec la fréquentation totale la plus élevée
arrondissement_plus_frequente = station_frequentation.idxmax()

# Ajouter une documentation
print("Ce code permet d'obtenir les données de fréquentation des stations Vélib à Paris pour une période donnée.")

# Ajouter des tests
def test_api_url():
    assert api_url == 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel?q=timestamp%3E%272023-10-25T00:00:00Z%27%20AND%272023-10-25T23:59:59Z%27'

def test_data():
    assert len(data) > 0

def test_df():
    assert df.shape[0] == len(data)

def test_station_frequentation():
    assert len(station_frequentation) == 20

def test_arrondissement_plus_frequente():
    assert arrondissement_plus_frequente == 1

# Exécuter les tests
test_api_url()
test_data()
test_df()
test_station_frequentation()
test_arrondissement_plus_frequente()

# Convertir les données en fréquence horaire
station_frequentation = station_frequentation.asfreq('H', fill_value=0)

# Afficher les résultats
print("L'arrondissement le plus fréquenté sur la période est :", arrondissement_plus_frequente)
print(station_frequentation)