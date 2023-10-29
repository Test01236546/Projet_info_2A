import requests as r 
from geopy.distance import geodesic
import geopy

class Fonctionnalites():
    def __init__(self):
        pass
    
    
    def F1(self,address):
        def get_coordinates_from_address(address):
            # Faire une requête à l'API Etalab
            url = f"https://api-adresse.data.gouv.fr/search/?q={address}&limit=1"
            response = r.get(url)

            if response.status_code == 200:
                data = response.json()
                if data['features']:
                    lon, lat = data['features'][0]['geometry']['coordinates']
                    return lat, lon
                else:
                    return None, None
            else:
                return None, None

        lat, lon = get_coordinates_from_address(address) #on obtient les coordonnées gps à partir de l'adresse

        if lat is not None and lon is not None:
            # Faire une requête à l'API
            null = None
            url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json?lang=fr&timezone=Europe%2FBerlin"
            response = r.get(url)

            if response.status_code == 200:
                response_json = response.json()
                stations_data= response_json["results"]
        
                # Filtre les stations qui sont installées et ouvertes à la location et qui ont au moins 1 vélo dispo.
                stations_utilisables = [station for station in stations_data if station["is_installed"] == "OUI" and station["is_renting"] == "OUI" and station["numbikesavailable"] >= 1]

                # Vérification qu'il y a au moins une station utilisable
                if stations_utilisables:
            
                    # Calcule la distance entre la position et chaque station.
                    distances = []
                    for station in stations_utilisables:
                        distance = geopy.distance.distance((lon, lat), (station["coordonnees_geo"]["lon"],station["coordonnees_geo"]["lat"])).km
                        distances.append((distance, station["name"]))

                    # Renvoie le nom de la station avec la distance la plus courte.
                    return min(distances, key=lambda x: x[0])[1]
    
                else:
                    return "Aucune station avec un vélo disponible à proximité."
    
            else:
                return "Erreur lors de la requête à l'API."
        else:
            return "Impossible de trouver les coordonnées de l'adresse."


    def F2(self):
        pass
    def F3(self):
        pass