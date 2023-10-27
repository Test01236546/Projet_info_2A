null = None
stations_data = [{"stationcode": "31104", "name": "Mairie de Rosny-sous-Bois", "is_installed": "OUI", "capacity": 30, "numdocksavailable": 14, "numbikesavailable": 15, "mechanical": 4, "ebike": 11, "is_renting": "OUI", "is_returning": "OUI", "duedate": "2023-10-25T16:09:19+02:00", "coordonnees_geo": {"lon": 2.4865807592869, "lat": 48.871256519012}, "nom_arrondissement_communes": "Rosny-sous-Bois", "code_insee_commune": null},{"stationcode": "16107", "name": "Benjamin Godard - Victor Hugo", "is_installed": "OUI", "capacity": 35, "numdocksavailable": 27, "numbikesavailable": 8, "mechanical": 5, "ebike": 3, "is_renting": "OUI", "is_returning": "OUI", "duedate": "2023-10-25T16:03:53+02:00", "coordonnees_geo": {"lon": 2.275725, "lat": 48.865983}, "nom_arrondissement_communes": "Paris", "code_insee_commune": null},{"stationcode": "9020", "name": "Toudouze - Clauzel", "is_installed": "OUI", "capacity": 21, "numdocksavailable": 16, "numbikesavailable": 5, "mechanical": 0, "ebike": 5, "is_renting": "OUI", "is_returning": "OUI", "duedate": "2023-10-25T16:09:15+02:00", "coordonnees_geo": {"lon": 2.3373600840568547, "lat": 48.87929591733507}, "nom_arrondissement_communes": "Paris", "code_insee_commune": null}]
#null = None

for station in stations_data:
  station.pop("code_insee_commune", null)
#def keep_all_but_code_insee_commune(station):
#  return {key: value for key, value in station.items() if key != "code_insee_commune"}

#stations_data = [keep_all_but_code_insee_commune(station) for station in stations_data]


print(stations_data)
###################### test 2
import requests
url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json?lang=fr&timezone=Europe%2FBerlin"
response = requests.get(url)