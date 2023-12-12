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
templates = Jinja2Templates(directory="scripts")
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


    
@app.get("/")
def get_stations():
    return "Working"

@app.get("/stations",description="Permet de récupérer l'ensemble des stations depuis l'API d'OpenData Paris")
def get_stations():
    return F.Fonctionnalites().recup_stations()

@app.get("/stations/closest", description="Permet de récupérer la station la plus proche de la position de l'utilisateur. Exemple d'adresse rentrée : 124 avenue jean jaurès clamart")
def get_closest_station(adresse):
    return F.Fonctionnalites().F1(adresse)

@app.get("/stations/least_frequented", description="Permet de renvoyer la station la moins fréquentée sur une période de temps donnée. L'heure doit être rentrée sous la forme : AAAA-MM-DDTHH:NN:SS+00:00. Exemple : 2023-12-05T20:05:28+01:00 et 2023-12-05T20:06:28+01:00")
def get_least_frequented_station(start_date: str, end_date: str):
    return F.Fonctionnalites().F2(start_date, end_date)

@app.get("/stations/most_frequented_arrondissement", description="Permet de renvoyer l'arrondissement le moins fréquenté sur une période de temps donnée. L'heure doit être rentrée sous la forme : AAAA-MM-DDTHH:NN:SS+00:00. Exemple : 2023-12-05T20:05:28+01:00 et 2023-12-05T20:06:28+01:00")
def get_most_frequented_arrondissement(start_date: str, end_date: str):
    return F.Fonctionnalites().F3(start_date, end_date)

# Fonction Bonus F01
templates = Jinja2Templates(directory="src/scripts")
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

@app.get("/stations/updatestation",response_model=None, description="Permet de modifier le nom d'une station à partir de son id. Exemple d'entrées : id : 16107 changement : Victor Hugo")
def mettre_a_jour(id : str, nouvelles_informations : str):
    return F.Fonctionnalites().F03_modifstation(id, nouvelles_informations) #enlever return et décommenter ligne suivante
    # return JSONResponse(content={"message": "Update successful"})

@app.get("/stations/delatestation",response_model=None, description="Permet de supprimer une station à partir de son id. Exemple d'entrées : id : 16107 ")
def mettre_a_jour(id : str):
    return F.Fonctionnalites().F03_sup_station(id) 

@app.get("/stations/createstation",response_model=None, description="Permet de créer une station. Exemple d'entrées : id : 16107, nom_station: Benjamin Godard - Victor Hugo, coordonnees_station: {'lon': 2.275725, 'lat': 48.865983},capacite : 35,nb_bornettes: 35,numbikesavailable : 1,mechanical : 1,ebike :0,is_returning : OUI,is_renting : OUI,duedate : 2023-12-12T01:48:43+01:00,nom_arrondissement_communes : Paris")
def mettre_a_jour(id : str, nom_station: str, coordonnees_station: str,capacite : int,nb_bornettes: int,numbikesavailable : int,mechanical : int,ebike :int,is_returning : str,is_renting : str,duedate : str,nom_arrondissement_communes : str):
    return F.Fonctionnalites().F03_add_station(id=id,nom_station= nom_station, coordonnees_station=coordonnees_station,capacite=capacite ,nb_bornettes=nb_bornettes,numbikesavailable=numbikesavailable ,mechanical=mechanical ,ebike=ebike,is_returning=is_returning,is_renting=is_renting,duedate=duedate,nom_arrondissement_communes=nom_arrondissement_communes) 
#id : 16107, nom_station: Benjamin Godard - Victor Hugo, coordonnees_station: {'lon': 2.275725, 'lat': 48.865983},capacite : 35,nb_bornettes: 35,numbikesavailable : 1,mechanical : 1,ebike :0,is_returning : OUI,is_renting : OUI,duedate : 2023-12-12T01:48:43+01:00,nom_arrondissement_communes : Paris

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