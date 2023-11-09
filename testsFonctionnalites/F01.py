import requests as r
import geopy.distance
import asyncio
import websockets

class VeloFinder:
    async def F01(self, address):
        async def get_coordinates_from_address(address):
            url = f"https://api-adresse.data.gouv.fr/search/?q={address}&limit=1"
            response = await r.get(url)

            if response.status_code == 200:
                data = response.json()
                if data['features']:
                    lon, lat = data['features'][0]['geometry']['coordinates']
                    return lat, lon
                else:
                    return None, None
            else:
                return None, None

        async def find_closest_station(lat, lon):
            url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"
            response = await r.get(url)

            if response.status_code == 200:
                stations_data = response.json()
                stations_utilisables = [station for station in stations_data['results'] if station["is_installed"] == "OUI" and station['is_renting'] == "OUI" and station['numbikesavailable'] >= 1]

                if stations_utilisables:
                    distances = []
                    for station in stations_utilisables:
                        distance = geopy.distance.distance((lon, lat), (station['coordonnees_geo']['lon'], station['coordonnees_geo']['lat'])).km
                        distances.append((distance, station['name']))

                    return min(distances, key=lambda station: station[0])[1]

                else:
                    return "Aucune station avec un vélo disponible à proximité."

            else:
                return "Erreur lors de la requête à l'API."

        async def update_closest_station():
            async with websockets.connect('ws://localhost:8765') as websocket:
                address = await websocket.recv()
                lat, lon = await get_coordinates_from_address(address)
                closest_station = await find_closest_station(lat, lon)
                await websocket.send(closest_station)

        # Lancement de la mise à jour en temps réel de la station la plus proche
        asyncio.get_event_loop().run_until_complete(update_closest_station())
        
if __name__ == "__main__":
    async def serve(websocket, path):
        # Envoie de l'adresse de l'utilisateur
        await websocket.send("8 Rue de Londres, Paris")

    # Lancement du serveur WebSocket
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(serve, 'localhost', 8765)
    )
    asyncio.get_event_loop().run_forever()

