# Generated by Django 4.2.19 on 2025-02-11 14:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=200, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18)),
                ('razao_social', models.CharField(max_length=100)),
                ('data_hora_abertura', models.TimeField(blank=True, null=True)),
                ('data_hora_fechamento', models.TimeField(blank=True, null=True)),
                ('comodidades', models.ManyToManyField(blank=True, related_name='estacionamentos', to='estacionamentos.comodidade')),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estacionamentos.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('status', models.CharField(default='livre', max_length=10)),
                ('estacionamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vagas_set', to='estacionamentos.estacionamento')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioEstacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('senha', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(blank=True, related_name='usuario_estacionamento_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='usuario_estacionamento_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estacionamentos.usuarioestacionamento'),
        ),
        migrations.AddField(
            model_name='estacionamento',
            name='vagas',
            field=models.ManyToManyField(blank=True, related_name='estacionamentos', to='estacionamentos.vaga'),
        ),
        migrations.AddField(
            model_name='comodidade',
            name='estacionamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comodidades_set', to='estacionamentos.estacionamento'),
        ),
    ]
