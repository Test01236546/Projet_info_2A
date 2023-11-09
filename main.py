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

import Service as sv 

import json
from BDD.constantes import BDD_PATH

from Service import Station as st
from Service import commune as cm
from Service import Temps as tp
from Service import StationFaits as stf

from DAO import StationDAO as stDAO
from DAO import communeDAO as cmDAO
from DAO import TempsDAO as tpDAO
from DAO import StationFaitsDAO as stfDAO

from BDD import classBDD as cBDD



if __name__ == "__main__":
    
    # Créer la BDD
    db_manager = cBDD.BDD_Manager(BDD_PATH)
    # BDD_Manager(BDD_PATH).create_stations_table()
    
    while True:
        # Mettre à jour les bases de données
        Instance_Service = sv
        # Attendre 1 minute avant de se mettre à jour à nouveau
        time.sleep(60)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

if __name__ == "__main__":
    service = Service()
    service.ingest()


