import sqlite3
import Service.commune as cm

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

    def create2(self,dict):
        Commune_to_add = cm.Commune(dict['code_insee_commune'],dict['name'])
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

    def delete(self, id_commune):
        """
        Supprime une commune de la base de données en fonction de son identifiant.

        Args:
            id_commune (str): L'identifiant de la commune à supprimer.
        """
        self.cur.execute("DELETE FROM Commune WHERE id_commune=?", (id_commune,))
        self.conn.commit()
        print("Commune supprimée")


