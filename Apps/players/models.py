from django.db import models
from Apps.teams.models import Team
from .managers import *


# Create your models here.
class Player(models.Model):

    POSITION_CHOICES = (
        ('0', 'DEFENSA CENTRAL'),
        ('1', 'DEFENSOR LATERAL'),
        ('2', 'DEFENSOR LIBRE POR BANDA'),
        ('3', 'DEFENSOR MEDIO CAMPO'),
        ('4', 'CENTROCAMPISTA DEFENSIVO'),
        ('5', 'MEDIOCAMPISTA CENTRAL'),
        ('6', 'MEDIOCAMPISTA EXTERNO'),
        ('7', 'MEDIOCAMPISTA OFENSIVO'),
        ('8', 'LATERAL VOLANTE'),
        ('9', 'VOLANTE DE CONTENCION'),
        ('10', 'VOLANTE DE CORTE'),
        ('11', 'VOLANTE DE SALIDA'),
        ('12', 'VOLANTE EXTERNO'),
        ('13', 'VOLANTE MIXTO'),
        ('14', 'VOLANTE DE ENLACE'),
        ('15', 'VOLANTE DE LLEGADA'),
        ('16', 'MEDIA PUNTA'),
        ('17', 'SEGUNDO DELANTERO'),
        ('18', 'DELANTERO'),
        ('19', 'PUNTERO'),
        ('20', 'EXTREMO'),
        ('21', 'DELANTERO CENTRO'),
    )

    player_name = models.CharField('Name', max_length=50, blank=False)
    player_lastname = models.CharField('Lastname',max_length=50, blank=False)
    birth = models.DateField('Birth', blank=False)
    team_position = models.CharField('Position', blank=False, max_length=2, choices=POSITION_CHOICES)
    team_number = models.IntegerField('Shirt Number', blank=False)
    is_starter = models.BooleanField('Starter',default=False, blank=False)
    #player_photo = models.ImageField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    objects = PlayerManager()

    def __str__(self):
        #return f'{self.id}. {self.player_name}'
        return f'{self.id}. {self.player_name} {self.player_lastname}, {self.birth}'

