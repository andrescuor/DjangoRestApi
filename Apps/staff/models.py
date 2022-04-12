from django.db import models
from Apps.teams.models import Team
# Create your models here.


class Staff(models.Model):

    ROL_CHOICES = (
        ('0', 'TECNICO'),
        ('1', 'MEDICO'),
        ('2', 'PREPARADOR'),
    )
    staff_name = models.CharField('Nombre', max_length=50, blank=False)
    staff_lastname = models.CharField('Apellido', max_length=50, blank=False)
    birth = models.DateField('Fecha Nacimiento', blank=False)
    nationality = models.CharField('Nacionalidad', max_length=50, blank=False)
    rol = models.CharField('Rol', max_length=1, choices=ROL_CHOICES, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.staff_name}, {self.nationality}'
