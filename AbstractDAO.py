from abc import ABC, abstractmethod

class StationDAO(ABC):
    @abstractmethod
    def create(self, station):
        """Crée une nouvelle station dans la base de données.

        Args:
            station: La station à créer.

        Returns:
            None.

        Raises:
            Exception: Si la station n'est pas valide.
        """
        if not station.is_valid():
            raise Exception("La station n'est pas valide")

        # Exécution de la requête SQL
        sql = """
            INSERT INTO stations (name, arrondissement, date_update)
            VALUES (?, ?, ?)
        """
        values = (station.name, station.arrondissement, station.date_update)
        self.execute(sql, values)        


    @abstractmethod
    def update(self, station):
        """Met à jour une station dans la base de données.

        Args:
            station: La station à mettre à jour.

        Returns:
            None.

        Raises:
            Exception: Si la station n'est pas valide.
        """
        if not station.is_valid():
            raise Exception("La station n'est pas valide")

        # Exécution de la requête SQL
        sql = """
            UPDATE stations
            SET name = ?, arrondissement = ?, date_update = ?
            WHERE id = ?
        """
        values = (station.name, station.arrondissement, station.date_update, station.id)
        self.execute(sql, values)

    def delete_station(self, station_id: int) -> None:
        """Supprime une station de la base de données.

        Args:
            station_id: L'identifiant de la station à supprimer.

        Returns:
            None.
        """

        # Exécution de la requête SQL
        sql = """
            DELETE FROM stations
            WHERE id = ?
        """
        values = (station_id,)
        self.execute(sql, values)

    @abstractmethod
    def delete(self, station):
        """Supprime une station de la base de données.

        Args:
            station_id: L'identifiant de la station à supprimer.

        Returns:
            None.
        """

        # Exécution de la requête SQL
        sql = """
            DELETE FROM stations
            WHERE id = ?
        """
        values = (station_id,)
        self.execute(sql, values)

