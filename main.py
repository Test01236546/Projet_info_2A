from fastapi import FastAPI


# On instancie le webservice
app = FastAPI()

# Création d'un enpoint qui répond à la méthode GET à l'adresse "/" qui va retourne le message "Hello World"
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Lancement de l'application sur le le port 80
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)