import requests
from geopy.distance import geodesic
import geopy
#import json

def get_coordinates_from_address(address):
    # Faire une requête à l'API Etalab
    url = f"https://api-adresse.data.gouv.fr/search/?q={address}&limit=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['features']:
            lon, lat = data['features'][0]['geometry']['coordinates']
            return lat, lon
        else:
            return None, None
    else:
        return None, None

def trouver_station_proche(lat, lon):
    # Faire une requête à l'API
    null=None # car dans la base de donnée response 
    url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json?lang=fr&timezone=Europe%2FBerlin"
    response = requests.get(url)
    

    if response.status_code == 200:
        stations_data = response.json()
        
        
        # Filtre les stations qui sont installées et ouvertes à la location et qui ont au moins 1 vélo dispo.
        stations_utilisables = [station for station in stations_data if station["is_installed"] == "OUI" and station["is_renting"] == "OUI" and station["numbikesavailable"] >= 1]

        #verification qu'il y au moins une station utilisable
        if stations_utilisables:
            
            # Calcule la distance entre la position et chaque station.
            distances = []
            for station in stations_utilisables:
                distance = geopy.distance.distance((lon, lat), (station["coordonnees_geo"]["lon"],station["coordonnees_geo"]["lat"])).km
                distances.append((distance, station["name"]))
#station["name"] a remplacer à la place de station
            # Renvoie la station avec la distance la plus courte.

            return min(distances, key=lambda x: x[0])[1]
    
        else:
            return "Aucune station avec un vélo disponible à proximité."
        
    else:
        return "Erreur lors de la requête à l'API."

# Coordonnées à partir desquelles vous souhaitez trouver la station
latitude = 48.8182338426597
longitude = 2.271145564431678

nom_station_proche = trouver_station_proche(latitude, longitude)
print(f"La station la plus proche est : {nom_station_proche}")

# Utilisation des fonctions
address = "30, rue de Sèvres, 75007"
lat, lon = get_coordinates_from_address(address)

if lat is not None and lon is not None:
    station = trouver_station_proche(lat, lon)
    print(f"La station Vélib la plus proche de l'adresse est : {station}")
else:
    print("Impossible de trouver les coordonnées de l'adresse.")