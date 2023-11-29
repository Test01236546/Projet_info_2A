# Velib' Hunter 🚲🔪

## Objectif 🎯

Bienvenue dans l'application Velib' Hunter 🚲🔪 ! L'objectif de ce projet est d'explorer les données d'OpenData Paris pour rendre l'utilisation des Velib' plus pratique et aider la ville de Paris à mieux gérer son parc de vélos.

## Fonctionnalités Obligatoires 🧐

### F1 : Localiser la station la plus proche avec au moins un vélo disponible

Permet aux utilisateurs de trouver la station la plus proche ayant au moins un vélo disponible. Les coordonnées géographiques peuvent être fournies en utilisant l'API d'Etalab pour transformer une adresse en coordonnées.

### F2 : Identifier la station la moins fréquentée sur une période donnée

Implique de récupérer le nom de la station la moins fréquentée sur une période spécifiée.

### F3 : Déterminer l'arrondissement le plus fréquenté sur une période donnée

Consiste à obtenir le numéro de l'arrondissement le plus fréquenté sur une période de temps définie.

## Fonctionnalités Optionnelles 🚀

### FO1 : Recherche de vélo en temps réel

Amélioration de la F1 en temps réel grâce à une connexion basée sur un WebSocket pour actualiser le nom de la station la plus proche.

### FO2 : Déploiement avec Docker Compose

Conteneurisation de la solution pour faciliter le déploiement en utilisant Docker Compose.

### FO3 : CRUD pour la manipulation de la base de données

Ajout de routes à l'API pour permettre aux utilisateurs de récupérer, supprimer, mettre à jour et ajouter des informations sur une station.

### FO4 : Historisation de la table Station

Utilisation d'une technique de modélisation pour historiser les changements dans les caractéristiques d'une station.

## Outils Utilisés 🛠️

- FastAPI : Librairie pour construire des APIs de manière rapide et efficace.
- SQLite : Système de gestion de base de données pour stocker les informations des stations Velib'.
- Gitlab/Github : Outil de versioning de code en équipe pour assurer la collaboration et le suivi des modifications.

Le projet, guidé par ces objectifs et outils, vise à offrir une solution robuste et pratique pour l'utilisation optimale des vélos Velib' à Paris.


## Tuto Docker (M. DENEUVILLE)
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


## Tutoriel pour installer Docker Desktop (personnel)
[Docker]
Désolé de vous spam 💀, maintenant je vais pouvoir commencer à travailler F02

_Processus installation Docker _(pendant que c'est encore frais dans ma tête) :
1) Installer Docker Desktop
2) Update wsl : wsl.exe --update
3) Vérifier ses distributions Linux (WSL) : wsl -l -v  
4) Installer Ubuntu (ou autre distrib si nécessaire) : wsl.exe --install -d Ubuntu   
(la liste des distrib est accessible via wsl --list --online)
5) Si erreur "Error: 0x800703fa - Press any key to continue" alors mettre à jour WSL puis rentre un username et pw ( jeremie_projet_info vaLL1034 , éventuellement sans 1034)
6) Ouvrir Docker Desktop

PS : 
- voir remarque plus haut pour les path (cf pb de reconnaissance de "docker" dans le terminal)
- pour vérifier si on a une version de docker : docker --version

Lien utiles :
- commandes de bases WSL : https://learn.microsoft.com/fr-fr/windows/wsl/basic-commands
- forum message erreur WSL en ouvrant Docker Desktop (approche BIOS, non utile pour mon cas) : https://forums.docker.com/t/an-unexpected-error-was-encountered-while-executing-a-wsl-command/137525/9
- installer Docker Desktop : https://docs.docker.com/desktop/install/windows-install/
(utile pour manipuler Docker et comprendre le concept)
- télécharger les distribution via site internet : https://learn.microsoft.com/fr-fr/windows/wsl/install-manual#downloading-distributions
- guide bizarre d'installation WSL (un peu bizarre mais peu être utile, pas utilisé) : https://learn.microsoft.com/fr-fr/windows/wsl/install-on-server
- Tutoriel Docker envoyé par M. GOUTIN Samuel : https://fastapi.tiangolo.com/deployment/docker/

## Construire & run son Dockerfile
construction : docker build -t my-fastapi-app .
run : docker run -p 8000:8000 my-fastapi-app