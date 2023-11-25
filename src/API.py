from fastapi import FastAPI

import requests as r 
from pydantic import BaseModel
from src.Service.Station import Station
import src.DAO.StationDAO as SDAO
import uvicorn
from src.Service.Service import Service
from datetime import datetime
import src.Service.Fonctionnalites as F
from geopy.geocoders import Nominatim 

from fastapi.responses import JSONResponse
from fastapi import WebSocket , Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
import asyncio

app=FastAPI()
# Classe API
class StationAPI():
    def __init__(self):
        super().__init__()
        #self.station = Station()
        self.connection = None

    def station_plus_proche(self, adresse):
        # Récupération des données de l'API
        url = "https://api-adresse.data.gouv.fr/search/?q={}".format(adresse)
        response = r.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data["features"]) == 1:
                position = (data["features"][0]["geometry"]["coordinates"][0], data["features"][0]["geometry"]["coordinates"][1])
                # Appeler la méthode F1() de la classe Fonctionnalites()
                station_proche = F.Fonctionnalites().F1(lat, lon)

                return station_proche
            else:
                raise Exception("L'adresse donnée n'est pas valide")
        else:
            raise Exception("Erreur lors de la récupération des données de l'API Adresse")


    def get_station_la_moins_frequentee(self, date_debut, date_fin):
        # Récupération des données de la base de données
        return dao.least_frequented_station
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM stations WHERE date_update BETWEEN ? AND ? ORDER BY available_bikes DESC", (date_debut, date_fin))
        data = cursor.fetchone()
        cursor.close()

        # Retour de la station la moins fréquentée
        return data[0] if data is not None else None

    def get_arrondissement_le_plus_frequente(self, date_debut, date_fin):
        # Récupération des données de la base de données
        return dao.most_frequented_arr()

        cursor = self.connection.cursor()
        cursor.execute("SELECT arrondissement, COUNT(*) AS nb_usagers FROM stations WHERE date_update BETWEEN ? AND ? GROUP BY arrondissement ORDER BY nb_usagers DESC", (date_debut, date_fin))
        data = cursor.fetchone()
        cursor.close()

        # Retour de l'arrondissement le plus fréquenté
        return data[0] if data is not None else None
    
    
@app.get("/")
def get_stations():
    return "Working"

@app.get("/stations",description="Permet de récupérer l'ensemble des stations depuis l'API d'OpenData Paris")
def get_stations():
    return F.Fonctionnalites().recup_stations()

@app.get("/stations/closest", description="Permet de récupérer la station la plus proche de la position de l'utilisateur. Exemple d'adresse rentrée : 124 avenue jean jaurès clamart")
def get_closest_station(adresse):
    return F.Fonctionnalites().F1(adresse)

@app.get("/stations/least_frequented", description="Permet de renvoyer la station la moins fréquentée sur une période de temps donnée. L'heure doit être rentrée sous la forme : AAAA-MM-DDTHH:NN:SS+00:00. Exemple : 2023-07-25T12:08:24+02:00 et 2023-11-14T12:02:55+01:00")
def get_least_frequented_station(start_date: str, end_date: str):
    return F.Fonctionnalites().F2(start_date, end_date)

@app.get("/stations/most_frequented_arrondissement", description="Permet de renvoyer l'arrondissement le moins fréquenté sur une période de temps donnée. L'heure doit être rentrée sous la forme : AAAA-MM-DDTHH:NN:SS+00:00. Exemple : 2023-07-25T12:08:24+02:00 et 2023-11-14T12:02:55+01:00")
def get_most_frequented_arrondissement(start_date: str, end_date: str):
    return F.Fonctionnalites().F3(start_date, end_date)

# Fonction Bonus F01
templates = Jinja2Templates(directory="scripts")
@app.get("/nearestbike/{adresse}")  #endpoint de presentation
async def get(request: Request, adresse: str):
    return templates.TemplateResponse("ws.html", {"request": request, "adresse": adresse})

@app.websocket("/ws")     #endpoint qui gère les connexions WebSocket et envoyer périodiquement des informations de la sttaion la plus proche à l'utilisateur à partir de l'adresse initiale qu'il a rentrée
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    adresse_en_cours = await websocket.receive_text()
    while True:
        station_bis = F.Fonctionnalites().F1(adresse_en_cours)
        await websocket.send_text(f"Last position was: {adresse_en_cours} ({datetime.now()}). Station info: {station_bis}")
        await asyncio.sleep(2)  #reactualise toutes les 2 secondes
#Fin fonction Bonus F01

@app.get("/stations/updatestation",response_model=None, description="Permet de modifier les caractéristiques d'une station à partir de son id. Exemple d'entrées : id : 16107 changement :{\"stationcode\": \"16107\", \"name\": \"Benjamin Godard - Victor Hugo\", \"is_installed\": \"OUI\", \"capacity\": 35, \"numdocksavailable\": 14, \"numbikesavailable\": 21, \"mechanical\": 5, \"ebike\": 16, \"is_renting\": \"OUI\", \"is_returning\": \"OUI\", \"duedate\": \"2023-11-20T13:18:42+00:00\", \"coordonnees_geo\": {\"lon\": 2.275725, \"lat\": 48.865983}, \"nom_arrondissement_communes\": \"Paris\", \"code_insee_commune\": null}")
def mettre_a_jour(id : str, nouvelles_informations : Station):
    F.Fonctionnalites().F03(id, nouvelles_informations)
    return JSONResponse(content={"message": "Update successful"})

@app.get("/stations/updatestationfait",response_model=None, description="Permet de modifier les caractéristiques non fixes d'une station à partir de son id. Exemple d'entrées : id : 16107 changement :{\"stationcode\": \"16107\", \"name\": \"Benjamin Godard - Victor Hugo\", \"is_installed\": \"OUI\", \"capacity\": 35, \"numdocksavailable\": 14, \"numbikesavailable\": 21, \"mechanical\": 5, \"ebike\": 16, \"is_renting\": \"OUI\", \"is_returning\": \"OUI\", \"duedate\": \"2023-11-20T13:18:42+00:00\", \"coordonnees_geo\": {\"lon\": 2.275725, \"lat\": 48.865983}, \"nom_arrondissement_communes\": \"Paris\", \"code_insee_commune\": null}")
def mettre_a_jour(id : str, nouvelles_informations : Station):
    F.Fonctionnalites().F03(id, nouvelles_informations)
    return JSONResponse(content={"message": "Update successful"})

def get_position_from_address(address):
    # Récupération des données de l'API
    url = "https://api-adresse.data.gouv.fr/search/?q={}".format(address)
    response = r.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data["features"]) == 1:
            position = (data["features"][0]["geometry"]["coordinates"][0], data["features"][0]["geometry"]["coordinates"][1])
            return position
        else:
            raise Exception("L'adresse donnée n'est pas valide")
    else:
        raise Exception("Erreur lors de la récupération des données de l'API Adresse")

#if __name__ == "__main__":
#    position = get_position_from_address(address)
#    print(position)