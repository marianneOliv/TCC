from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from estacionamentos.models import Estacionamento
from .forms import EstacionamentoForm
from .forms import CompletarCadastroEstacionamentoForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Estacionamento, UsuarioEstacionamento, Vaga , Comodidade , Endereco
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


ESP32_URL = "http://localhost:8180/toggle/1"  # Ajuste para o IP do seu ESP32


def home(request):
    return render(request, 'home.html')

def loginEstacionamento(request):
    print("Chegou no loginEstacionamento")  

    if request.method == 'POST':
        print("Requisição POST recebida")  
        
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print(f"Email: {email}, Senha: {senha}")  

        if email and senha:
            print(f"Tentando autenticar o usuário  {email}")
            usuario = authenticate(request, email=email, password=senha)
            
            if usuario is not None:
                print(f"Usuário autenticado: {usuario}")  
                login(request, usuario)
                return redirect('completarCadastro')  
            else:
                messages.error(request, "Credenciais inválidas. Tente novamente.")
                return render(request, 'estacionamentos/loginEstacionamento.html')

        else:
            messages.error(request, "Por favor, preencha todos os campos.")
            return render(request, 'estacionamentos/loginEstacionamento.html')

    return render(request, 'estacionamentos/loginEstacionamento.html')


def cadastroEstacionamento(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        razao_social = request.POST.get('razao_social')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('password2')

        if senha1 != senha2:
            messages.error(request, "As senhas não coincidem.")
            print(f"senhas: {senha1}")
            print(f"senhas: {senha2}")

            return render(request, 'estacionamentos/cadastroEstacionamento.html')

        if UsuarioEstacionamento.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
            return render(request, 'estacionamentos/cadastroEstacionamento.html')

        usuario = UsuarioEstacionamento.objects.create_user(username=email, email=email, password=senha1)
        # estacionamento = Estacionamento.objects.create(user=usuario, cnpj=cnpj, razao_social=razao_social)

        estacionamento = Estacionamento.objects.create(
            user=usuario,
            cnpj=cnpj,
            razao_social=razao_social
        )

        messages.success(request, "Pré-cadastro realizado com sucesso! Complete seu cadastro.")
        
        return redirect('completarCadastro', estacionamento_id=estacionamento.id)

    return render(request, 'estacionamentos/cadastroEstacionamento.html')

def completarCadastro(request, estacionamento_id):
    estacionamento = get_object_or_404(Estacionamento, id=estacionamento_id)

    if request.method == 'POST':
        data_hora_abertura = request.POST.get('data_hora_abertura')
        data_hora_fechamento = request.POST.get('data_hora_fechamento')
       
        cep = request.POST.get('cep')

        comodidades = request.POST.getlist('comodidades')
        quantidade_vagas = request.POST.get('quantidade_vagas')

        estacionamento.data_hora_abertura = data_hora_abertura
        estacionamento.data_hora_fechamento = data_hora_fechamento

        estacionamento.cep = cep 
        estacionamento.vagas = quantidade_vagas


        for comodidade_nome in comodidades:
            comodidade = Comodidade(nome=comodidade_nome, estacionamento=estacionamento)
            comodidade.save()

        if quantidade_vagas:  
            try:
                estacionamento.vagas = int(quantidade_vagas)  
            except ValueError:
                
                estacionamento.vagas = 3  
        else:
            estacionamento.vagas = 3  
        estacionamento.save()
        print(f"CEP recebido: {cep}")

        messages.success(request, "Cadastro finalizado com sucesso!")
        return redirect('completarCadastro', estacionamento_id=estacionamento.id)

    return render(request, 'estacionamentos/completarCadastro.html', {'estacionamento': estacionamento})

@login_required
def gerenciarEstacionamento(request, estacionamento_id):
    estacionamento = get_object_or_404(Estacionamento, id=estacionamento_id)
    
    return render(request, 'estacionamentos/gerenciarEstacionamento.html', {'estacionamento': estacionamento})

