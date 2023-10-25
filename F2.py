import requests
import pandas as pd

# Faire une requête à l'API pour obtenir les données de fréquentation
api_url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel'
response = requests.get(api_url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    data = response.json()  # Supposons que les données sont au format JSON
    # Convertir les données JSON en un DataFrame Pandas
    df = pd.DataFrame(data)

    # Grouper les données par station et calculer la fréquentation totale
    station_frequentation = df.groupby('stationcode')['numbikesavailable'].sum()

    # Trouver la station la moins fréquentée
    station_moins_frequente = station_frequentation.idxmin()

    print("La station la moins fréquentée est :", station_moins_frequente)
else:
    print("Échec de la requête à l'API. Code de statut :", response.status_code)
