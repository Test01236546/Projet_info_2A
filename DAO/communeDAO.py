import sqlite3
import Service.commune as cm
import Service.fonctions_intermédiaires as fi

class CommuneDAO:
    """
    Crée la classe CommuneDAO qui permet de mettre à jour la table Commune dans la base de données
    """
    def __init__(self,path):
        """
        Initialise un objet d'accès aux données (DAO) pour la gestion des communes dans une base de données SQLite.

        Args:
            path (str): Le chemin du fichier de base de données SQLite.
        """

        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self,commune):
        """
        Insère une nouvelle commune dans la base de données.

        Args:
            commune (Commune): L'objet Commune à insérer dans la base de données.
        """
        self.cur.execute("""
        INSERT INTO Commune VALUES (?, ?)
        """, (commune.id_commune, commune.nom_commune))
        self.conn.commit()
        print("Commune créée")

    def create2(self,dictionnaire):
        Commune_to_add = cm.Commune(fi.codeInsee_to_code(dictionnaire['stationcode']),dict['name'])
        self.cur.execute("""
        INSERT INTO Commune VALUES (?, ?)
        """, (Commune_to_add.id_commune, Commune_to_add.nom_commune))
        self.conn.commit()
        


    def read(self, id_commune):
        """
        Recherche une commune dans la base de données en fonction de son identifiant.

        Args:
            id_commune (str): L'identifiant de la commune à rechercher.

        Returns:
            tuple or None: Un tuple contenant les données de la commune trouvée (id_commune, nom_commune) ou None si la commune n'a pas été trouvée.
        """
        self.cur.execute("SELECT * FROM Commune WHERE id_commune=?", (id_commune,))
        commune = self.cur.fetchone()
        if commune:
            print("Commune trouvée:", commune)
            return commune
            # return Commune(*commune_data) si on ne manipulait pas déja des communes
        else:
            print("Commune non trouvée")
            return None
        

    def update(self, id_commune, new_data):
        """
        Met à jour les informations d'une commune dans la base de données.

        Args:
            id_commune (str): L'identifiant de la commune à mettre à jour.
            new_data (Commune): L'objet Commune contenant les nouvelles données.

        Note:
            Seule la modification du nom de la commune est prise en charge dans cette méthode.
        """
        self.cur.execute("""
        UPDATE Commune SET nom_commune=? WHERE id_commune=?
        """, (new_data.nom_commune, id_commune))
        self.conn.commit()
        print("Commune mise à jour")
    
    
    def update2(self, dictionnaire):
        """
        Met à jour les informations d'une commune dans la base de données en utilisant les données fournies dans un dictionnaire.

        Args:
            dictionnaire (dict): Un dictionnaire contenant les nouvelles données de la commune.
        """
        # Supposons que les clés du dictionnaire correspondent aux attributs de l'objet Commune
        Commune_to_update = cm.Commune(fi.codeInsee_to_code(dictionnaire['stationcode']),dictionnaire['name'])

        # Mise à jour de l'enregistrement dans la base de données
        self.cur.execute("""
        UPDATE Commune SET nom_commune=? WHERE id_commune=?
        """, (Commune_to_update.nom_commune, Commune_to_update.id_commune))
        self.conn.commit()
        print(f"Commune {Commune_to_update.id_commune} mise à jour")


    def delete(self, id_commune):
        """
        Supprime une commune de la base de données en fonction de son identifiant.

        Args:
            id_commune (str): L'identifiant de la commune à supprimer.
        """
        self.cur.execute("DELETE FROM Commune WHERE id_commune=?", (id_commune,))
        self.conn.commit()
        print("Commune supprimée")


    def upsert2(self, dictionnaire):
        """
        Met à jour une commune si elle existe, sinon insère une nouvelle commune en utilisant un dictionnaire.

        Args:
            dictionnaire (dict): Un dictionnaire contenant les données de la commune.
        """
        # Création d'une instance de Commune avec les données du dictionnaire
        Commune_to_upsert = cm.Commune(
            fi.codeInsee_to_code(dictionnaire['stationcode']),
            dictionnaire['nom_arrondissement_communes']
        )

        # Tentative de mise à jour
        self.cur.execute("""
        UPDATE Commune SET nom_commune=? WHERE id_commune=?
        """, (
            Commune_to_upsert.nom_commune,
            Commune_to_upsert.id_commune
        ))

        # Vérification si la mise à jour a affecté des lignes
        if self.cur.rowcount == 0:
            # Aucune ligne mise à jour, donc insertion
            self.cur.execute("""
            INSERT INTO Commune VALUES (?, ?)
            """, (
                Commune_to_upsert.id_commune,
                Commune_to_upsert.nom_commune
            ))

        self.conn.commit()
        # print(f"Commune pour l'identifiant {Commune_to_upsert.id_commune} mise à jour ou insérée")


    def close(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

