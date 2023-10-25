import fastapi
import requests
from pydantic import BaseModel
from Station import Station

def get_coordinates(address):
    url = "https://api.etalab.gouv.fr/geoportail/adresses/v2/?q={}".format(address)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["features"][0]["geometry"]["coordinates"]
    else:
        return None
    

app = fastapi.FastAPI()

@app.get("/closest_station/")
async def get_closest_station(address: Address):
    coordinates = get_coordinates(address.formatted_address)
    if coordinates is not None:
        return get_closest_station(coordinates)
    else:
        return "Aucune station trouvée"

@app.get("/least_frequented_station/")
async def get_least_frequented_station(start_date: str, end_date: str):
    return get_least_frequented_station(start_date, end_date)

@app.get("/most_frequented_district/")
async def get_most_frequented_district(start_date: str, end_date: str):
    return get_most_frequented_district(start_date, end_date)

app.run(debug=True)
