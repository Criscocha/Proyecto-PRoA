from django import forms
from .models import Contacto
from .models import Logro
from .models import Evento

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Tu correo'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Tu mensaje'}),
        }
        

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'imagen', 'vigente']


class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro 
        fields = ['nombre', 'descripcion']