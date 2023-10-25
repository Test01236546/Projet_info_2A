import requests
from geopy.distance import geodesic

def trouver_station_proche(lat, lon):
    # Faire une requête à l'API
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        stations = data["data"]["stations"]

        # Initialiser les variables pour la station la plus proche
        station_proche = None
        distance_min = float('inf')

        for station in res["results"]:
            station_fonc = station["is_installed"] 
            
            lon = station["coordonnees_geo"]["lon"]
            lat = station["coordonnees_geo"]["lat"]
            coordinates_list.append((lat, lon))
            # Calculer la distance entre les coordonnées
            distance = geodesic((lat, lon), coords_station).meters

            # Vérifier si la station a au moins un vélo disponible
            if station["num_bikes_available"] > 0 and distance < distance_min:
                distance_min = distance
                station_proche = station

        if station_proche:
            return station_proche["name"]
        else:
            return "Aucune station avec un vélo disponible à proximité."
    else:
        return "Erreur lors de la requête à l'API."

# Coordonnées à partir desquelles vous souhaitez trouver la station
latitude = 48.8566
longitude = 2.3522

nom_station_proche = trouver_station_proche(latitude, longitude)
print(f"La station la plus proche est : {nom_station_proche}")
