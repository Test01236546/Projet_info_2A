from abc import ABC, abstractmethod

# il faudait faire raise error si les class fille n'ont pas les méthodes

class StationDAO(ABC):
    @abstractmethod
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
    def insert(self, station):
        pass
