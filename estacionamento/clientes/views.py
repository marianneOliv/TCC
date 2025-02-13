from django.shortcuts import render, redirect 
from .models import Cliente
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from estacionamentos.models import Estacionamento , Vaga
from .forms import ClienteForm
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import requests
import asyncio
from asgiref.sync import sync_to_async
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def loginCliente(request):
    print("Chegou no loginCliente")  

    if request.method == 'POST':
        print("Requisição POST recebida")  
        print (request.POST)
        
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print(f"Email: {email}, Senha: {senha}")  

        if email and senha:
            print(f"Tentando autenticar o usuário {email}") 
            usuario = authenticate(request, email=email, password=senha)
            
            if usuario is not None:
                print(f"Usuário autenticado: {usuario}")  
                login(request, usuario)
                return redirect('buscarEstacionamento')  
            else:
                messages.error(request, "Credenciais inválidas. Tente novamente.")
                return render(request, 'clientes/loginCliente.html')

        else:
            messages.error(request, "Por favor, preencha todos os campos.")
            return render(request, 'clientes/loginCliente.html')

    return render(request, 'clientes/loginCliente.html')


def cadastroCliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha1 = request.POST.get('password1')
        senha2 = request.POST.get('password2')

        if senha1 != senha2:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'clientes/cadastroCliente.html')

        if Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, "Este CPF já está cadastrado.")
            return render(request, 'clientes/cadastroCliente.html')

        if Cliente.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
            return render(request, 'clientes/cadastrCliente.html')

        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email, senha=senha1)
        cliente.set_password(senha1) 
        cliente.save()

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('loginCliente')  
    return render(request, 'clientes/cadastroCliente.html')

def buscarEstacionamento(request):
    print("chamou buscar estacionamento")
    if not hasattr(request.user, 'cliente'):
        return redirect('home')  
    endereco = None
    estacionamentos = []

    if request.method == 'POST':
        cep = request.POST.get('cep')
        if not cep or cep.strip() == "":
            return render(request, 'clientes/buscarEstacionamento.html', {
                'erro': 'Por favor, insira um CEP válido.'
            })

        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        print("chamou api de enderecos")

        if response.status_code == 200:
            endereco = response.json()

            if "logradouro" not in endereco:
                return render(request, 'clientes/buscarEstacionamento.html', {
                    'erro': 'CEP não encontrado ou inválido.'
                })

            estacionamentos = Estacionamento.objects.filter(cep=cep)
        return render(request, 'clientes/buscarEstacionamento.html', {
            'endereco': endereco,
            'estacionamentos': estacionamentos
        })

    return render(request, 'clientes/buscarEstacionamento.html')    

import logging

logger = logging.getLogger(__name__)


def atualizar_vagas(request, estacionamento_id):  # Agora aceita o estacionamento_id
    print(f"Chamou atualizar_vagas para estacionamento {estacionamento_id}")

    try:
        # Faz a requisição para o ESP32
        print("Fazendo requisição para o ESP32...")
        response = requests.get('http://localhost:8180/status')  # Verifique se o IP está correto
        print(f"Resposta bruta do ESP32: {response.text}")

        if response.status_code != 200:
            return JsonResponse({'success': False, 'error': 'Falha na requisição ao ESP32'})

        dados_esp32 = response.json()
        print(f"Dados do ESP32: {dados_esp32}")

        # Atualiza o estacionamento com a nova quantidade de vagas
        estacionamento = Estacionamento.objects.get(id=estacionamento_id)
        estacionamento.vagas = dados_esp32.get('vagas', estacionamento.vagas)  # Pegando "vagas" do JSON
        estacionamento.save()

        print(f"Estacionamento atualizado. Novas vagas: {estacionamento.vagas}")

        return JsonResponse({
            'success': True,
            'vagas': estacionamento.vagas
        })

    except Exception as e:
        print(f"Erro ao atualizar vagas: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
