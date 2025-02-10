from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=200, unique=True)  # Email deve ser único
    senha = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    groups = models.ManyToManyField('auth.Group', related_name='usuario_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='usuario_set', blank=True)

class Cliente(Usuario):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=100)
