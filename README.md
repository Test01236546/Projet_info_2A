# Velib' Hunter 🚲🔪

## Objectif 🎯

Bienvenue dans le projet Velib' Hunter 🚲🔪 ! L'objectif de ce projet, sous la houlette du tuteur Samuel GOUTIN, est d'explorer les données d'OpenData Paris pour rendre l'utilisation des Velib' plus pratique et aider la ville de Paris à mieux gérer son parc de vélos.

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
