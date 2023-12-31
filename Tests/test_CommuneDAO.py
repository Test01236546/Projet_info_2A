import unittest
import sqlite3
from src.DAO.communeDAO import CommuneDAO

class TestCommuneDAO(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect('src.BDD.BDD.sql')  
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE Commune (id_commune TEXT PRIMARY KEY, nom_commune TEXT)")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_create_and_read(self):
        dao = CommuneDAO(self.conn)

        # Création d'une commune pour le test
        commune_data = {'id_commune': '75001', 'nom_commune': 'Paris 1er'}
        dao.create2(commune_data)

        # Vérification de la création
        self.cur.execute("SELECT * FROM Commune WHERE id_commune=?", ('75001',))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result, ('75001', 'Paris 1er'))

        # Test de la méthode read
        commune = dao.read('75001')
        self.assertIsNotNone(commune)
        self.assertEqual(commune, ('75001', 'Paris 1er'))

    def test_update_and_delete(self):
        dao = CommuneDAO(self.conn)

        # Création d'une commune pour le test
        commune_data = {'id_commune': '75001', 'nom_commune': 'Paris 1er'}
        dao.create2(commune_data)

        # Test de la méthode update
        dao.update2({'id_commune': '75001', 'nom_commune': 'Paris Nouveau'})
        updated_commune = dao.read('75001')
        self.assertIsNotNone(updated_commune)
        self.assertEqual(updated_commune, ('75001', 'Paris Nouveau'))

        # Test de la méthode delete
        dao.delete('75001')
        deleted_commune = dao.read('75001')
        self.assertIsNone(deleted_commune)

    def test_upsert2(self):
        dao = CommuneDAO(self.conn)

        # Création d'une commune pour le test
        commune_data = {'id_commune': '75001', 'nom_commune': 'Paris 1er'}
        dao.upsert2(commune_data)

        # Test de la méthode upsert2 pour la mise à jour
        dao.upsert2({'id_commune': '75001', 'nom_commune': 'Paris Nouveau'})
        updated_commune = dao.read('75001')
        self.assertIsNotNone(updated_commune)
        self.assertEqual(updated_commune, ('75001', 'Paris Nouveau'))

        # Test de la méthode upsert2 pour l'insertion
        dao.upsert2({'id_commune': '75002', 'nom_commune': 'Paris 2ème'})
        new_commune = dao.read('75002')
        self.assertIsNotNone(new_commune)
        self.assertEqual(new_commune, ('75002', 'Paris 2ème'))

    def test_close(self):
        # On s'assure que la connexion est ouverte avant de fermer
        assert self.conn is not None

        # Utilisation de la méthode close pour fermer la connexion
        self.conn.close()

        # On s'assure que la connexion est fermée après l'appel à close
        assert self.conn is None    

if __name__ == '__main__':
    unittest.main()