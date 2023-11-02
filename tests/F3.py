import urllib.request
import json
import pandas as pd


##############################################requete 1######################################################
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


#################requete2 chat gpt charles##################################################
import sqlite3



import sqlite3

def trouver_arrondissement_plus_frequent(date_debut, date_fin):
    # Connexion à la base de données
    conn = sqlite3.connect('votre_base_de_donnees.db')
    cursor = conn.cursor()
    
    # Requête SQL pour récupérer l'arrondissement le plus fréquenté
    query = """
        SELECT id_commune_ou_arr, SUM(total_freq_par_station) as total_freq_par_com_ou_arr
        FROM (
            SELECT Station.id_station, SUM(frequence) as total_freq_par_station
            FROM StationFaits
            JOIN Station ON StationFaits.id_station = Station.id_station
            WHERE date_fait_deb >= ? AND date_fait_fin <= ?
            GROUP BY Station.id_station
        ) as StationFreq
        JOIN CommuneOuArr ON StationFreq.id_station = CommuneOuArr.id_station
        GROUP BY id_commune_ou_arr
        ORDER BY total_freq_par_com_ou_arr DESC
        LIMIT 1
    """
    cursor.execute(query, (date_debut, date_fin))
    
    # Récupérer le résultat de la requête
    arrondissement_plus_frequente = cursor.fetchone()[0]
    
    # Fermer la connexion à la base de données
    conn.close()
    
    return arrondissement_plus_frequente

# Utilisation de la fonction
date_debut = '2023-10-29T00:00:00'
date_fin = '2023-10-30T00:00:00'
arrondissement_plus_frequent = trouver_arrondissement_plus_frequent(date_debut, date_fin)
print(f"L'arrondissement le plus fréquenté entre {date_debut} et {date_fin} est : {arrondissement_plus_frequent}")




# Connexion à la base de données
conn = sqlite3.connect('votre_base_de_donnees.db')
cursor = conn.cursor()

# Remplacez les valeurs de debut_timestamp et fin_timestamp par vos propres timestamps
debut_timestamp = '2023-10-29T00:00:00+01:00'
fin_timestamp = '2023-10-30T00:00:00+01:00'

# Exécution de la requête SQL
cursor.execute("""
    SELECT COUNT(cf.id_commune_ou_arr) as freq, coa.nom_commune_ou_arr
    FROM CommuneOuArr as coa
    JOIN StationFaits as sf ON coa.id_commune_ou_arr = sf.id_commune_ou_arr
    JOIN Temps as t ON sf.id_temps = t.id_temps
    WHERE t.timestamp >= ? AND t.timestamp <= ?
    GROUP BY coa.nom_commune_ou_arr
    ORDER BY freq DESC
    LIMIT 1;
""", (debut_timestamp, fin_timestamp))

# Récupération du résultat
resultat = cursor.fetchone()

# Fermeture de la connexion à la base de données
conn.close()

# Affichage du résultat
if resultat:
    freq, nom_commune_ou_arr = resultat
    print(f"L'arrondissement le plus fréquenté est {nom_commune_ou_arr} avec une fréquence de {freq} utilisations.")
else:
    print("Aucun résultat trouvé.")
