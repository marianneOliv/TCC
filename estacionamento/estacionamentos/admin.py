from django.contrib import admin
from .models import Endereco, Estacionamento, Comodidade, Vaga

admin.site.register(Endereco)
admin.site.register(Estacionamento)
admin.site.register(Comodidade)
admin.site.register(Vaga)
