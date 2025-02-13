# estacionamento/urls.py

from django.contrib import admin
from django.urls import path
from clientes import views as clientes_views  # Importe as views da sua aplicação
from django.contrib.auth import views as auth_views
from estacionamentos import views as estacionamentos_views



urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', clientes_views.home, name='home'), 
   
    path('loginCliente/', clientes_views.loginCliente, name='loginCliente'),
    path('loginEstacionamento/', estacionamentos_views.loginEstacionamento, name='loginEstacionamento'),
    
    path('cadastroCliente/', clientes_views.cadastroCliente, name='cadastroCliente'),
    path('buscarEstacionamento/',clientes_views.buscarEstacionamento, name='buscarEstacionamento'),
    
    path('cadastroEstacionamento/' , estacionamentos_views.cadastroEstacionamento, name='cadastroEstacionamento' ),
    path('completarCadastro/<int:estacionamento_id>/', estacionamentos_views.completarCadastro, name='completarCadastro'),

    path('gerenciarEstacionamento/<int:estacionamento_id>' , estacionamentos_views.gerenciarEstacionamento, name='gerenciarEstacionamento' ),
    path('atualizar_vagas/<int:estacionamento_id>/', clientes_views.atualizar_vagas, name='atualizar_vagas'),
]
