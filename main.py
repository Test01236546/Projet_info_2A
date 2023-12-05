# import sys
# sys.path.append('C:/Users/jerem/OneDrive/Documents/GitHub/Projet_info_2A/Projet_info_2A-7')

from src.API import StationAPI, app 
from fastapi import FastAPI

import requests as r 
from pydantic import BaseModel
import uvicorn
from datetime import datetime
import time
import src.Service.Fonctionnalites as F
from geopy.geocoders import Nominatim 


import src.Service.Service as sv 
import src.Service.fonctions_intermédiaires as fi

from src.BDD.constantes import BDD_PATH
from src.BDD import classBDD as cBDD


if __name__ == "__main__":
    # Créer la BDD
    db_manager = cBDD.BDD_Manager(BDD_PATH)
    cBDD.BDD_Manager(BDD_PATH).create_stations_table()
    Instance_Service = sv.Service()
    
    fi.periodic(Instance_Service,1*60*60,60) #ingest pendant 1*60*60 secs avec des pauses de 60 secs


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

# if __name__ == "__main__":
#     service = sv.Service()      
#     service.ingest()


