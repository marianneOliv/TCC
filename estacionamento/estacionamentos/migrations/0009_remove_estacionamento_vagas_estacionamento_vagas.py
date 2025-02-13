# Generated by Django 4.2.19 on 2025-02-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamentos', '0008_estacionamento_vagas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionamento',
            name='vagas',
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='vagas',
            field=models.ManyToManyField(blank=True, related_name='estacionamentos', to='estacionamentos.vaga'),
        ),
    ]
