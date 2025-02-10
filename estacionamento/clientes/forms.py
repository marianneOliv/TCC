from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(UserCreationForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email', 'senha']
