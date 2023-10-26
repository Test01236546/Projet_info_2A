import requests
from geopy.distance import geodesic
import json

def trouver_station_proche(lat, lon):
    # Faire une requête à l'API
    null=None # car dans la base de donnée response 
    url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json?lang=fr&timezone=Europe%2FBerlin"
    response = requests.get(url)
    

    if response.status_code == 200:
        stations_data = json.loads(response.text)
        
        
        # Filtre les stations qui sont installées et ouvertes à la location et qui ont au moins 1 vélo dispo.
        stations_utilisables = [station for station in stations_data if station["is_installed"] == "OUI" and station["is_renting"] == "OUI" and station["numdocksavailable"] >= 1]
        
        #verification qu'il y au moins une station utilisable
        if tations_utilisables:
            
            # Calcule la distance entre la position et chaque station.
            distances = []
            for station in stations_utilisables:
                distance = geopy.distance.distance((lon, lat), station["coordonnees_geo"]).km
                distances.append((distance, station["name"]))

            # Renvoie la station avec la distance la plus courte.

            return min(distances, key=lambda x: x[0])[1]
    
        else:
            return "Aucune station avec un vélo disponible à proximité."
        
    else:
        return "Erreur lors de la requête à l'API."

# Coordonnées à partir desquelles vous souhaitez trouver la station
latitude = 48.8566
longitude = 2.3522

nom_station_proche = trouver_station_proche(latitude, longitude)
print(f"La station la plus proche est : {nom_station_proche}")
