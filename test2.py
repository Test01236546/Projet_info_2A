import requests
import psycopg2
import pandas as pd

# Récupérez les données de l'API
response = requests.get(
    "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=10000&apikey=" 
)

# Convertissez les données en un tableau Pandas
data = response.json()["records"]
data = pd.DataFrame(data)

# Importez les données dans la base PostgreSQL
conn = psycopg2.connect("host=localhost dbname=velib user=postgres password=mypassword")
cur = conn.cursor()

# Créez la table
cur.execute("""
CREATE TABLE stations (
  name text,
  stationcode integer,
  ebike integer,
  mechanical integer,
  coordonnees_geo list,
  duedate date,
  numbikesavailable integer,
  numdocksavailable integer,
  capacity integer,
  is_renting text,
  is_installed text,
  nom_arrondissement_communes text,
  is_returning text                   
);
""")

# Importez les données
cur.copy_from(data, "stations", columns=data.columns, null="")

# Committez les modifications
conn.commit()

# Fermez la connexion
conn.close()



