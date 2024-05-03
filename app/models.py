from datetime import timezone
import django
from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils
import django.utils.timezone

# Create your models here.
class User(AbstractUser):
    ''' user model '''
    ESCOLARIDADE_CHOICES = [
        ('fundamental', 'Fundamental'),
        ('medio', 'Médio'),
        ('superior', 'Superior'),
        ('pos_graduacao', 'Pós-graduação'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
    ]

    ALUNO_UDC_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    GENERO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
    ]

    TIPO_SANGUINEO_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    ALERGIAS_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    RACA_CHOICES = [
        ('branca', 'Branca'),
        ('preta', 'Preta'),
        ('parda', 'Parda'),
        ('amarela', 'Amarela'),
        ('indigena', 'Indígena'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
    ]

    FILHO_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    cpf = models.CharField(default="", max_length=14)  # Assuming CPF format ###.###.###-##
    nascimento = models.DateField(default=django.utils.timezone.now())
    endereco = models.CharField(default="", max_length=100)
    contato = models.CharField(default="", max_length=15)  # Assuming a phone number format
    contato_emergencia = models.CharField(default="", max_length=15)  # Assuming a phone number format
    rede_social = models.CharField(max_length=100, blank=True, null=True)  # Assuming a social media handle or profile URL
    escolaridade = models.CharField(default="",max_length=20, choices=ESCOLARIDADE_CHOICES)
    aluno_udc = models.CharField(default="",max_length=3, choices=ALUNO_UDC_CHOICES)
    genero = models.CharField(default="",max_length=10, choices=GENERO_CHOICES)
    tipo_sanguineo = models.CharField(default="",max_length=3, choices=TIPO_SANGUINEO_CHOICES)
    alergias = models.CharField(default="nao", max_length=3, choices=ALERGIAS_CHOICES)
    alergia_descricao = models.CharField(max_length=100, blank=True, null=True)
    raca = models.CharField(default="",max_length=10, choices=RACA_CHOICES)
    profissao = models.CharField(default="", max_length=50)
    estado_civil = models.CharField(default="",max_length=20, choices=ESTADO_CIVIL_CHOICES)
    filho = models.CharField(default="",max_length=3, choices=FILHO_CHOICES)
    qtd_filhos = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.username
