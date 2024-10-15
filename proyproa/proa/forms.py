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
        
from .models import Evento, Noticia

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'vigente']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Widget de tipo fecha
        }


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'fecha', 'imagen']
        widgets = {
            'fecha': forms.DateInput(attrs={
                'type': 'text',  # Usamos tipo 'text' para poder aplicar un widget de calendario
                'class': 'datepicker',
                'placeholder': 'Selecciona una fecha'
            }),
        }

class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro 
        fields = ['nombre', 'descripcion']
