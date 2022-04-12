from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
# Definir el modelo de usuario en nuestro sistema
class UserProfileManager(BaseUserManager):
    '''Manager perfiles de usuario'''

    def create_user(self, email, name, password=None):
        '''Crear nuevo user profile'''
        if not email:
            raise ValueError('Usuario debe tener un Email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db) # Guardar usuario

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractUser, PermissionsMixin):
    '''Model system users'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Obtener nombre completo del usuario'''
        return self.name

    def get_short_name(self):
        '''Obtener nombre corto del usuario'''
        return self.name

    def __str__(self):
        '''retornar cadena representando nuestro usuario'''
        return self.email


class Team(models.Model):
    team_name = models.CharField('Team Name', max_length=50, unique=True, blank=False)
    #flag = models.ImageField()
    #shield = models.ImageField()

    def __str__(self):
        return f'{self.id}. {self.team_name}'






