from AbstractDAO import AbstractDAO
from abc import abstractmethod
class TempsDAO(AbstractDAO): 
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
