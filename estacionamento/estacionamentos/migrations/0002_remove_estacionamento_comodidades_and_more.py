# Generated by Django 4.2.19 on 2025-02-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionamento',
            name='comodidades',
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='comodidades',
            field=models.TextField(blank=True),
        ),
    ]
