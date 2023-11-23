### Docker

* Installer Docker Desktop for Windows
	* https://www.docker.com/products/docker-desktop/
	
* `docker pull hello-world` pour télécharger l’image hello-world
* `docker images` pour lister les images
* `docker run hello-world` pour démarrer le conteneur de l’image
* `docker run -d -p 8080:80 nginx`
	* lancer un serveur nginx
	* `-d` pour détacher le conteneur du processus principal de la console
	* `-p 8080:80` : transférer le trafic du port 8080 vers le port 80 du conteneur
	* http://127.0.0.1:8080
	* `docker exec -ti <id> bash` pour ouvrir un shell sur le conteneur
* `docker ps -a` pour lister tous les containers
* `docker stop <id or name>` pour arrêter un conteneur
* `docker rm <id or name>` pour supprimer un conteneur
* `docker rmi <id or name>` pour supprimer une image


### Images PostgreSQL et PGAdmin

https://github.com/khezen/compose-postgres/tree/master
https://thomasperrot.medium.com/installer-postgresql-et-pgadmin-avec-docker-sur-windows-ff5d49dadba9

* Créer un fichier docker-compose.yml
* Se postionner dans le dossier puis :
	* `docker-compose up -d`
	* `docker-compose stop` pour arrêter les conteneurs
* `docker exec -it postgres_container bash`
	* `psql -h localhost -p 5432 -U ludo -W` pour se connecter à la bdd
* http://localhost:5050/ pour ouvrir pgadmin
	* créer la connexion
	
### Create PostgreSQL database and fill it

https://levelup.gitconnected.com/creating-and-filling-a-postgres-db-with-docker-compose-e1607f6f882f