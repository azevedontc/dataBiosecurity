from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .models import User

UserModel = get_user_model()

class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'id': 'username', 'placeholder': 'Nome de usuario', 'autocomplete': 'off', 'autofocus': 'on'}), required=True,  label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'id': 'password', 'placeholder': 'Senha'}), required=True, label="")    


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
        fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'nascimento', 'endereco', 'contato', 'contato_emergencia', 'rede_social', 'escolaridade', 'aluno_udc', 'genero', 'tipo_sanguineo', 'alergias', 'alergia_descricao', 'raca', 'profissao', 'estado_civil', 'filho', 'qtd_filhos', 'password']
        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'cpf': 'CPF',
            'nascimento': 'Nascimento',
            'endereco': 'Endereço',
            'contato': 'Contato',
            'contato_emergencia': 'Contato emergencial',
            'rede_social': 'Rede social',
            'escolaridade': 'Escolaridade',
            'aluno_udc': 'Aluno da UDC?',
            'genero': 'Gênero',
            'tipo_sanguineo': 'Tipo sanguineo',
            'alergias': 'Alergias',
            'alergia_descricao': 'Alergia descrição',
            'raca': 'raça',
            'profissao': 'Profissão',
            'estado_civil': 'Estado civil',
            'filho': 'Possui filhos?',
            'qtd_filhos': 'Quantidade de filhos*',
            'password': 'Senha',
            'confirmation': 'Confirmação da Senha',
            # Add labels for other fields if needed
        }

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'autocomplete': 'off', 'autofocus': 'on'}), max_length=16, label="Nome de usuário")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'maxlenght': "50", 'autocomplete': 'off'}), label="Nome")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'maxlenght': "50", 'autocomplete': 'off'}), label="Sobrenome")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'autocomplete': 'off'}), label="Email")
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500',}), max_length=14, label="CPF")
    nascimento = forms.DateField(widget=forms.DateInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'type': 'date'}), label="Nascimento")
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500',}), max_length=100, label="Endereço")
    contato = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500',}), max_length=15, label="Contato")
    contato_emergencia = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500',}), max_length=15, label="Contato emergência")
    rede_social = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500',}), max_length=100, required=False, label="Rede social")
    escolaridade = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.ESCOLARIDADE_CHOICES, label="Escolaridade")
    aluno_udc = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.ALUNO_UDC_CHOICES, label="Aluno da UDC")
    genero = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.GENERO_CHOICES, label="Gênero")
    tipo_sanguineo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.TIPO_SANGUINEO_CHOICES, label="Tipo sanguíneo")
    alergias = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.ALERGIAS_CHOICES, label="Alergias")
    alergia_descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), max_length=100, required=False, label="Descrição alergias")
    raca = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.RACA_CHOICES, label="Raça")
    profissao = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500',}), max_length=50, label="Profissão")
    estado_civil = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.ESTADO_CIVIL_CHOICES, label="Estado civil")
    filho = forms.ChoiceField(widget=forms.Select(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), choices=User.FILHO_CHOICES, label="Possuí filhos?")
    qtd_filhos = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500'}), required=False, label="Quantidade de filhos")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'autocomplete': 'off'}), label="Senha")
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'autocomplete': 'off'}), label="Confirme a senha")

    
    def clean_username(self):
        ''' verify is the username is already taken.'''
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_("Nome de usuário já cadastrado"), code="username taken")
        return username
    
    def clean_email(self):
        ''' verify if the email is already registered '''
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("Email já cadastrado."), code="email taken")

        return email

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'].lower(),
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'].lower(),
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
            password=self.cleaned_data['password'],
        )
        user.save()
        return user
    

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'cpf', 'nascimento', 'endereco', 'contato', 'contato_emergencia', 'rede_social', 'escolaridade', 'aluno_udc', 'genero', 'tipo_sanguineo', 'alergias', 'alergia_descricao', 'raca', 'profissao', 'estado_civil', 'filho', 'qtd_filhos')
        exclude = ('password', 'confirmation', 'username')  # Exclude password field from the form
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': '',
            # Add labels for other fields if needed
        }
        help_texts = {}
        label_suffix = ''  # Set label suffix to an empty string to hide all labels

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Nome de usuário'})
        self.fields['first_name'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Nome', 'label': ""})
        self.fields['last_name'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Sobrenome', 'label': ""})
        self.fields['email'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Email', 'label': ""})
        self.fields['cpf'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'CPF', 'label': ""})
        self.fields['nascimento'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'type': 'date', 'label': ""})
        self.fields['endereco'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Endereço', 'label': ""})
        self.fields['contato'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Contato', 'label': ""})
        self.fields['contato_emergencia'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Contato de Emergência', 'label': ""})
        self.fields['rede_social'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Rede Social', 'label': ""})
        self.fields['escolaridade'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['aluno_udc'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['genero'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['tipo_sanguineo'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['alergias'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['alergia_descricao'].widget.attrs.update({'class': 'border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Descrição das Alergias', 'label': ""})
        self.fields['raca'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['profissao'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Profissão', 'label': ""})
        self.fields['estado_civil'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['filho'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'label': ""})
        self.fields['qtd_filhos'].widget.attrs.update({'class': 'my-2 w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-blue-500 focus:ring-blue-500', 'placeholder': 'Quantidade de Filhos', 'label': ""})