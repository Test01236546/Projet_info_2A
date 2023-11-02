from API import StationAPI, app 
from fastapi import FastAPI
from BDD.constantes import BDD_PATH

import requests as r 
from pydantic import BaseModel
from Service.station import Station
import uvicorn
from Service.service import Service
from datetime import datetime
import Service.fonctionnalites as F
from geopy.geocoders import Nominatim 
from BDD.classBDD import BDD_Manager
from DAO.stationDAO import StationDAO

if __name__ == "__main__":
    while True:
        BDD_Manager(BDD_PATH).create_stations_table()
        # Mettre à jour les bases de données
        Service().ingest()
        # Attendre 1 minute avant de se mettre à jour à nouveau
        time.sleep(60)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

if __name__ == "__main__":
    service = Service()
    service.ingest()


