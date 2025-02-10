from django.urls import path
from .views import cadastroEstacionamento

urlpatterns = [
    path('cadastroEstacionamento/', cadastroEstacionamento, name='cadastroEstacionamento'),
]
