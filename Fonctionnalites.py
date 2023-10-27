import requests as r 
from geopy.distance import geodesic
import geopy

class Fonctionnalites():
    def __init__(self):
        pass
    
    
    def F1(self,lon, lat):
       # Faire une requête à l'API
        lon = float(lon)
        lat = float(lat)
        null=None # car dans la base de donnée response 
        url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json?lang=fr&timezone=Europe%2FBerlin"
        response = r.get(url)
    

        if response.status_code == 200:
            stations_data = response.json()
        
        
        # Filtre les stations qui sont installées et ouvertes à la location et qui ont au moins 1 vélo dispo.
            stations_utilisables = [station for station in stations_data if station["is_installed"] == "OUI" and station["is_renting"] == "OUI" and station["numdocksavailable"] >= 1]

        #verification qu'il y au moins une station utilisable
            if stations_utilisables:
            
            # Calcule la distance entre la position et chaque station.
                distances = []
                for station in stations_utilisables:
                    distance = geopy.distance.distance((lon, lat), (station["coordonnees_geo"]["lon"],station["coordonnees_geo"]["lat"])).km
                    distances.append((distance, station["name"]))

            # Renvoie la station avec la distance la plus courte.

                return min(distances, key=lambda x: x[0])[1]
    
            else:
                return "Aucune station avec un vélo disponible à proximité."
        
        else:
            return "Erreur lors de la requête à l'API."

    def F2(self):
        pass
    def F3(self):
        pass