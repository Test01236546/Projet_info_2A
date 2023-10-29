import requests as r
null=None # car dans la base de donnée response 
#url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json?lang=fr&timezone=Europe%2FBerlin"
url =  "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=-1&timezone=Europe%2Fberlin"
response = r.get(url)
if response.status_code == 200:
    data = response.json()
    data_bis=data["results"]
    print(data_bis)
else:
    print("Erreur lors de la requête à l'API.")
    