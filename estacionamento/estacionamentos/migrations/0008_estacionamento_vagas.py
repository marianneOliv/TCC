# Generated by Django 4.2.19 on 2025-02-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamentos', '0007_rename_vagas_estacionamento_vagas_disponiveis'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamento',
            name='vagas',
            field=models.IntegerField(default=0),
        ),
    ]
