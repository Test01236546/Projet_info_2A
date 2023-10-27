from AbstractDAO import DAO

class TempsDAO(DAO): 
    def __init__(self, id_temps):
        self.id_temps=id_temps
        
       def create(self, station):
        pass

    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def update(self, station):
        pass

    @abstractmethod
    def delete(self, station):
        pass

    @abstractmethod
    def injest(self, station):
        pass
