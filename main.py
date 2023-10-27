from api import StationAPI, app 
from fastapi import FastAPI

import requests as r 
from pydantic import BaseModel
from Service.Station import Station
import uvicorn
from Service.Service import Service
from datetime import datetime
import Service.Fonctionnalites as F
from geopy.geocoders import Nominatim 


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

if __name__ == "__main__":
    service = Service()
    service.ingest()