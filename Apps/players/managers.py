from django.db import models
from django.db.models import Q

class PlayerManager(models.Manager):

    # Cual es el promedio de numero de jugadores en cada equipo (AVG-PLAYERS)
    def average_player_for_team(self):
        pass

    # Total de Jugadores que participaran en el campeonato (SUM-PLAYERS)
    def total_players_global(self, model):
        return self.filter().order_by()

    # Cuantos suplentes hay (SUM-PLAYERS)
    def total_second_players(self):
        pass

    # Promedio de suplentes por cada equipo (AVG-PLAYERS)
    def average_second_players(self):
        pass

    # Cual es la edad promedio de los jugadores (AVG-PLAYERS)
    def players_average_age(self):
        pass

    # Quien es el mas Joven (MAX-PLAYERS)
    def youngest_player(self):
        pass

    # Quien es el mas viejo (MIN-PLAYERS)
    def oldest_player(self):
        pass
