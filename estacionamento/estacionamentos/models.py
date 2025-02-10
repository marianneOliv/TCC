from django.db import models
from clientes.models import Usuario  
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class Endereco(models.Model):
    cep = models.CharField(max_length=8, null=True, blank=True)
    logradouro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f'{self.logradouro}, {self.cidade} - {self.estado}'


class UsuarioEstacionamento(AbstractUser):
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=200, unique=True)  
    senha = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    groups = models.ManyToManyField('auth.Group', related_name='usuario_estacionamento_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='usuario_estacionamento_set', blank=True)


class Estacionamento(models.Model):
    user = models.OneToOneField(UsuarioEstacionamento, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=100)
    
    data_hora_abertura = models.TimeField(null=True, blank=True)  # Permite ficar vazio
    data_hora_fechamento = models.TimeField(null=True, blank=True)
    
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE , null=True)
    vagas = models.ManyToManyField('Vaga', blank=True)
    comodidades = models.ManyToManyField('Comodidade', related_name="estacionamentos", null=True , blank=True)


    def __str__(self):
        return self.razao_social

class Comodidade(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE, related_name="comodidades_set")
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)

class Vaga(models.Model):
    quantidade = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantidade} vagas - {self.status}"
