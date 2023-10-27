from abc import ABC, abstractmethod

# il faudait faire raise error si les class fille n'ont pas les méthodes rtt

class StationDAO(ABC):
    @abstractmethod
    def create(self, station):
        raise NotImplementedError

    @abstractmethod
    def read(self, id):
        raise NotImplementedError

    @abstractmethod
    def update(self, station):
        raise NotImplementedError

    @abstractmethod
    def delete(self, station):
        raise NotImplementedError

    @abstractmethod
    def injest(self, station):
        raise NotImplementedError
