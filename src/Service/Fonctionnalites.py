import requests as r 
from geopy.distance import geodesic
import geopy
import sqlite3 #pour F2 et F3
import src.DAO.StationDAO as SDAO
import src.DAO.StationFaitsDAO as SFDAO

class Fonctionnalites():
    def __init__(self):
        """
        Initialise un objet Fonctionnalites pour effectuer différentes tâches.

        Note:
            Cette classe n'a pas besoin d'initialisation spécifique, car toutes ses méthodes sont des méthodes statiques.
        """
        pass
    
    def recup_stations(self):
        """
        Récupère tous les noms de stations Vélib' Métropole depuis l'API de données ouvertes de Paris.

        Returns:
            list: Une liste de noms de stations Vélib'.
        """

    # Récupération des données de l'API
        url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"  # Modifier le paramètre limit selon vos besoins

        response = r.get(url)

    # Vérification du code d'état
        if response.status_code != 200:
            raise Exception("Erreur lors de la récupération des données de l'API Vélib' Métropole")

    # Liste contenant les noms de stations
        data = response.json()
        stations = [station['name'] for station in data['results'] ]
        print(len(stations))
        return stations



    def F1(self,address):
        """
        Retourne le nom de la station Vélib' la plus proche d'une adresse donnée.

        Args:
            address (str): L'adresse pour laquelle vous souhaitez trouver la station la plus proche.

        Returns:
            str: Le nom de la station Vélib' la plus proche de l'adresse donnée.
        """
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
            url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"
            response = r.get(url)

            if response.status_code == 200:
                stations_data= response.json()
        
                # Filtre les stations qui sont installées et ouvertes à la location et qui ont au moins 1 vélo dispo.
                #stations_utilisables = [station for station in stations_data if int(station["is_installed"]) == 1 and int(station["is_renting"]) == 1 and int(station["numbikesavailable"]) >= 1]
                #stations_utilisables = [station for station in stations_data if station[0] == "OUI" and station[1] == "OUI" and station[2] >= 1]
                stations_utilisables = [station for station in stations_data['results'] if station["is_installed"] == "OUI" and station['is_renting'] == "OUI" and station['numbikesavailable'] >= 1]
                #stations_utilisables = [station for station in stations_data if station["is_installed"] == "OUI" and station["is_renting"] == "OUI" and station["numbikesavailable"] >= 1]
                # Vérification qu'il y a au moins une station utilisable
                if stations_utilisables:
                    # Calcule la distance entre la position et chaque station.
                    distances = []
                    for station in stations_utilisables:
                        #distance = geopy.distance.distance((lon, lat), (station["coordonnees_geo"]["lon"],station["coordonnees_geo"]["lat"])).km
                        #distances.append((distance, station["name"]))
                        distance = geopy.distance.distance((lon, lat), (station['coordonnees_geo']['lon'],station['coordonnees_geo']['lat'])).km
                        distances.append((distance, station['name']))
                    # Renvoie le nom de la station avec la distance la plus courte.
                    return min(distances, key=lambda station: station[0])[1]
                
    
                else:
                    return "Aucune station avec un vélo disponible à proximité."
    
            else:
                return "Erreur lors de la requête à l'API."
        else:
            return "Impossible de trouver les coordonnées de l'adresse."


    def F2(self,date_debut, date_fin):
        """
        Retourne le nom de la station Vélib' ayant le moins de fréquence d'utilisation dans une plage de dates donnée.

        Args:
            date_debut (str): La date de début de la plage.
            date_fin (str): La date de fin de la plage.

        Returns:
            str: Le nom de la station Vélib' avec le moins de fréquence d'utilisation dans la plage de dates.
        """
        # Connexion à la base de données
        conn = sqlite3.connect("BDD/BDD.sql")
        cursor = conn.cursor()
    
        # Requête SQL pour récupérer le nom de la station avec le moins de fréquence
        query = """
            SELECT nom_station
            FROM StationFaits
            JOIN Station ON StationFaits.id_station = Station.id
            WHERE date_fait_deb >= ? AND date_fait_fin <= ?
            GROUP BY StationFaits.id_station
            ORDER BY SUM(frequence)
            LIMIT 1
        """
        cursor.execute(query, (date_debut, date_fin))
    
        # Récupérer le résultat de la requête
        nom_station = cursor.fetchone()
    
        # Fermer la connexion à la base de données
        conn.close()
    
        return nom_station
    
    
    def F3(self,date_debut, date_fin):
        """
        Retourne l'arrondissement ou la commune la plus fréquentée par les utilisateurs de Vélib' dans une plage de dates donnée.

        Args:
            date_debut (str): La date de début de la plage.
            date_fin (str): La date de fin de la plage.

        Returns:
            str: L'arrondissement ou la commune la plus fréquentée par les utilisateurs de Vélib'.
        """
        # Connexion à la base de données
        conn = sqlite3.connect("BDD/BDD.sql")
        cursor = conn.cursor()
    
        # Requête SQL pour récupérer l'arrondissement le plus fréquenté
        query = """
            SELECT id_commune, SUM(total_freq_par_station) as total_freq_par_com_ou_arr
            FROM (
            SELECT Station.id, Commune.id_commune, SUM(frequence) as total_freq_par_station
            FROM StationFaits
            JOIN Station ON StationFaits.id_station = Station.id
            JOIN Commune ON Station.id_Commune = Commune.id_commune
            WHERE date_fait_deb >= ? AND date_fait_fin <= ?
            GROUP BY Station.id, Commune.id_commune
            ) as StationFreq
            GROUP BY id_commune
            ORDER BY total_freq_par_com_ou_arr DESC
            LIMIT 1;       
        """
        cursor.execute(query, (date_debut, date_fin))
    
        # Récupérer le résultat de la requête
        arrondissement_plus_frequente = cursor.fetchone()[0]
    
        # Fermer la connexion à la base de données
        conn.close()
    
        return arrondissement_plus_frequente
    

    def F03_modifstation(self, station_id, new_name):
            # Vérifier si la station existe
        existing_station = SDAO.StationDAO(path="BDD/BDD.sql").read(station_id)
        if not existing_station:
            raise HTTPException(status_code=404, detail="Station not found")

    # Créer un objet Station avec les nouvelles données
        updated_station = {
            "nom_station": new_name,
            "capacite": existing_station.capacite,
            "coordonnees_station": existing_station.coordonnees_station,
            "id_commune": existing_station.id_commune,
            "en_fonctionnement": existing_station.en_fonctionnement,
            "date_deb": existing_station.date_deb,
            "date_fin": existing_station.date_fin,
            "borne_paiement": existing_station.borne_paiement,
            "nb_bornettes": existing_station.nb_bornettes
        }

        SDAO.StationDAO(path="BDD/BDD.sql").update(id, updated_station)
