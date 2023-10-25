import requests
import psycopg2

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
  id integer,
  name text,
  status text,
  bike_stands integer,
  available_bike_stands integer,
  available_bikes integer
);
""")

# Importez les données
cur.copy_from(data, "stations", columns=data.columns, null="")

# Committez les modifications
conn.commit()

# Fermez la connexion
conn.close()



