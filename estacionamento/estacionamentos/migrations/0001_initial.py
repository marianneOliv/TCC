# Generated by Django 5.1.5 on 2025-02-09 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comodidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('estado', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18)),
                ('razao_social', models.CharField(max_length=100)),
                ('inscricao_estadual', models.CharField(max_length=20)),
                ('data_hora_abertura', models.DateTimeField()),
                ('data_hora_fechamento', models.DateTimeField()),
                ('comodidades', models.ManyToManyField(blank=True, related_name='estacionamentos', to='estacionamentos.comodidade')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamentos.endereco')),
                ('vagas', models.ManyToManyField(blank=True, to='estacionamentos.vaga')),
            ],
        ),
        migrations.AddField(
            model_name='comodidade',
            name='estacionamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comodidades_set', to='estacionamentos.estacionamento'),
        ),
    ]
