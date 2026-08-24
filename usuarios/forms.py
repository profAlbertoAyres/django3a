from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Aluno


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'cep',
            'endereco',
            'bairro',
            'cidade',
            'estado',
            'celular',
            'nascimento',
            'sexo',
            'objetivo',
        ]
        labels = {
            'endereco':'Endereço'
        }
        widgets = {
            'nascimento':forms.TextInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

