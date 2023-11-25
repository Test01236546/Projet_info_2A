import unittest
from src.DAO.AbstractDAO import AbstractDAO

class TestAbstractDAO(unittest.TestCase):
    def test_create_not_implemented(self):
        dao = AbstractDAO()

        with self.assertRaises(NotImplementedError):
            dao.create(None)

    def test_read_not_implemented(self):
        dao = AbstractDAO()

        with self.assertRaises(NotImplementedError):
            dao.read(None)

    def test_update_not_implemented(self):
        dao = AbstractDAO()

        with self.assertRaises(NotImplementedError):
            dao.update(None)

    def test_delete_not_implemented(self):
        dao = AbstractDAO()

        with self.assertRaises(NotImplementedError):
            dao.delete(None)
    
    def test_close(self):
        # On s'assure que la connexion est ouverte avant de fermer
        assert AbstractDAO.conn is not None

        # Utilisation de la méthode close pour fermer la connexion
        AbstractDAO.close()

        # On s'assure que la connexion est fermée après l'appel à close
        assert AbstractDAO.conn is None

if __name__ == '__main__':
    unittest.main()