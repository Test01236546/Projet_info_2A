from API import StationAPI, app 
from fastapi import FastAPI

import requests as r 
from pydantic import BaseModel
import uvicorn
from datetime import datetime
import time
# import Service.fonctionnalites as F
from geopy.geocoders import Nominatim 


import Service.Service as sv 

from BDD.constantes import BDD_PATH
from BDD import classBDD as cBDD



if __name__ == "__main__":
    
    # Créer la BDD
    db_manager = cBDD.BDD_Manager(BDD_PATH)
    # BDD_Manager(BDD_PATH).create_stations_table()
    Instance_Service = sv.Service()
    
    while True:
        # Mettre à jour les bases de données
        Instance_Service.ingest()
        # Attendre 1 minute avant de se mettre à jour à nouveau
        time.sleep(60)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

if __name__ == "__main__":
    service = sv.Service()      # A quoi ça sert ?
    service.ingest()


