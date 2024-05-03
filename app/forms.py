from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .models import User

UserModel = get_user_model()

class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'field__input', 'id': 'username', 'placeholder': 'Username', 'autocomplete': 'off', 'autofocus': 'on'}), required=True,  label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field__input', 'id': 'password', 'placeholder': 'Password'}), required=True, label="")    


# class Register_form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username", "first_name", "last_name", "email", "password"]

#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'field__input', 'placeholder': 'Username', 'autocomplete': 'off', 'autofocus': 'on'}), max_length=16, label="")
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field__input', 'placeholder': 'First name', 'maxlenght': "50", 'autocomplete': 'off'}), label="")
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field__input',  'placeholder': 'Last name', 'maxlenght': "50", 'autocomplete': 'off'}), label="")
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'field__input', 'placeholder': 'Email', 'autocomplete': 'off'}), label="")
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field__input', 'placeholder': 'Password', 'autocomplete': 'off'}), label="")
#     confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field__input', 'placeholder': 'Confirmation', 'autocomplete': 'off'}), label="")    
    
#     def clean_username(self):
#         ''' verify is the username is already taken.'''
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError(_("Username already taken"), code="username taken")
#         return username
    
#     def clean_email(self):
#         ''' verify if the email is already registered '''
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError(_("Email has already been taken."), code="email taken")

#         return email

#     def save(self):
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'].lower(),
#             first_name=self.cleaned_data['first_name'],
#             last_name=self.cleaned_data['last_name'],
#             email=self.cleaned_data['email'].lower(),
#             password=self.cleaned_data['password']
#         )
#         user.save()
#         return user

from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm

class Register_form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'cpf', 'nascimento', 'endereco', 'contato', 'contato_emergencia', 'rede_social', 'escolaridade', 'aluno_udc', 'genero', 'tipo_sanguineo', 'alergias', 'alergia_descricao', 'raca', 'profissao', 'estado_civil', 'filho', 'qtd_filhos']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'field__input', 'placeholder': 'Nome de usuario', 'autocomplete': 'off', 'autofocus': 'on'}), max_length=16, label="")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field__input', 'placeholder': 'Nome', 'maxlenght': "50", 'autocomplete': 'off'}), label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'field__input', 'placeholder': 'Email', 'autocomplete': 'off'}), label="")
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}), max_length=14, label="")
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), label="")
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}), max_length=100, label="")
    contato = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contato'}), max_length=15, label="")
    contato_emergencia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contato de Emergência'}), max_length=15, label="")
    rede_social = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rede Social'}), max_length=100, required=False, label="")
    escolaridade = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.ESCOLARIDADE_CHOICES, label="")
    aluno_udc = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.ALUNO_UDC_CHOICES, label="")
    genero = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.GENERO_CHOICES, label="")
    tipo_sanguineo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.TIPO_SANGUINEO_CHOICES, label="")
    alergias = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.ALERGIAS_CHOICES, label="")
    alergia_descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrição das Alergias'}), max_length=100, required=False, label="")
    raca = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.RACA_CHOICES, label="")
    profissao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profissão'}), max_length=50, label="")
    estado_civil = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.ESTADO_CIVIL_CHOICES, label="")
    filho = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=User.FILHO_CHOICES, label="")
    qtd_filhos = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de Filhos'}), required=False, label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field__input', 'placeholder': 'Password', 'autocomplete': 'off'}), label="")
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field__input', 'placeholder': 'Confirmation', 'autocomplete': 'off'}), label="")

    
    def clean_username(self):
        ''' verify is the username is already taken.'''
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_("Username already taken"), code="username taken")
        return username
    
    def clean_email(self):
        ''' verify if the email is already registered '''
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("Email has already been taken."), code="email taken")

        return email

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'].lower(),
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'].lower(),
            password=self.cleaned_data['password'],
            cpf=self.cleaned_data['cpf'],
            nascimento=self.cleaned_data['nascimento'],
            endereco=self.cleaned_data['endereco'],
            contato=self.cleaned_data['contato'],
            contato_emergencia=self.cleaned_data['contato_emergencia'],
            rede_social=self.cleaned_data['rede_social'],
            escolaridade=self.cleaned_data['escolaridade'],
            aluno_udc=self.cleaned_data['aluno_udc'],
            genero=self.cleaned_data['genero'],
            tipo_sanguineo=self.cleaned_data['tipo_sanguineo'],
            alergias=self.cleaned_data['alergias'],
            alergia_descricao=self.cleaned_data['alergia_descricao'],
            raca=self.cleaned_data['raca'],
            profissao=self.cleaned_data['profissao'],
            estado_civil=self.cleaned_data['estado_civil'],
            filho=self.cleaned_data['filho'],
            qtd_filhos=self.cleaned_data['qtd_filhos'],
        )
        user.save()
        return user
    

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'cpf', 'nascimento', 'endereco', 'contato', 'contato_emergencia', 'rede_social', 'escolaridade', 'aluno_udc', 'genero', 'tipo_sanguineo', 'alergias', 'alergia_descricao', 'raca', 'profissao', 'estado_civil', 'filho', 'qtd_filhos')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome de usuário'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sobrenome'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CPF'})
        self.fields['nascimento'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Endereço'})
        self.fields['contato'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contato'})
        self.fields['contato_emergencia'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contato de Emergência'})
        self.fields['rede_social'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Rede Social'})
        self.fields['escolaridade'].widget.attrs.update({'class': 'form-control'})
        self.fields['aluno_udc'].widget.attrs.update({'class': 'form-control'})
        self.fields['genero'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo_sanguineo'].widget.attrs.update({'class': 'form-control'})
        self.fields['alergias'].widget.attrs.update({'class': 'form-control'})
        self.fields['alergia_descricao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição das Alergias'})
        self.fields['raca'].widget.attrs.update({'class': 'form-control'})
        self.fields['profissao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Profissão'})
        self.fields['estado_civil'].widget.attrs.update({'class': 'form-control'})
        self.fields['filho'].widget.attrs.update({'class': 'form-control'})
        self.fields['qtd_filhos'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Quantidade de Filhos'})