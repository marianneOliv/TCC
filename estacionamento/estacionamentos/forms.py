from django import forms
from .models import Estacionamento, Endereco, Vaga, Comodidade
from django.contrib.auth import get_user_model

class EstacionamentoForm(forms.ModelForm):
    razao_social = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnpj = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_hora_abertura = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    data_hora_fechamento = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Estacionamento
        fields = ['razao_social', 'cnpj', 'data_hora_abertura', 'data_hora_fechamento']


class EnderecoForm(forms.ModelForm):
    cep = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    logradouro = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'cidade', 'estado']


class VagaForm(forms.ModelForm):
    quantidade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    status = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Vaga
        fields = ['quantidade', 'status']


class ComodidadeForm(forms.ModelForm):
    tipo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Comodidade
        fields = ['tipo', 'descricao', 'estado', 'cep']


from django import forms
from .models import Estacionamento

class CompletarCadastroEstacionamentoForm(forms.ModelForm):
    cep = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    rua = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}), required=False)
    cidade = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}), required=False)
    estado = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}), required=False)
    comodidades = forms.MultipleChoiceField(
        choices=[('cameras', 'Câmeras de Segurança'), 
                 ('wi_fi', 'Wi-Fi'),
                 ('vagas_handicap', 'Vagas para Deficientes'),
                 ('carregadores', 'Carregadores de Carro Elétrico')],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        required=True
    )
    data_hora_abertura = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}), required=True)
    data_hora_fechamento = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = Estacionamento
        fields = ['cep', 'rua', 'cidade', 'estado', 'comodidades', 'data_hora_abertura', 'data_hora_fechamento']
