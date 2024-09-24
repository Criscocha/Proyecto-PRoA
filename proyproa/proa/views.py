from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import ContactoForm
from .models import Evento
from .forms import EventoForm

# 
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def eventos(request):
    return render(request,'eventos.html')

def alumnos(request):
    return render(request,'alumnos.html')

def alumnos2(request):
    return render(request,'alumnos2.html')

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    
    contexto = {
        'form': form,
        'correos_institucionales': {
            'Directora': 'imeloncelli@escuelasproa.edu.ar',
            'Secretaria': 'mlvera@escuelasproa.edu.ar',
            'Coordinadora': 'mabelenseghezzi@escuelasproa.edu.ar',
            'Preceptora primer ciclo': 'jbarbieri@escuelasproa.edu.ar',
            'Preceptor segundo ciclo': 'edgarcorrea@escuelasproa.edu.ar',
            'Consultas': 'consultas_proavdt@escuelasproa.edu.ar',
        },
        'redes_sociales': {
            'WhatsApp': '03524-473666',
            'Facebook': 'https://www.facebook.com/profile.php?id=100090921822713&mibextid=ZbWKwL',
            'Instagram': 'https://www.instagram.com/proa.vadeltotoral?igsh=N2w4MnM2eWwwaTF5'
        }
    }
    return render(request, 'contactos.html', contexto)

def contacto_confirmacion(request):
    return render(request, 'contacto_confirmacion.html')

def academico(request):
    return render(request,'academico.html')

def admisiones(request):
    return render(request,'admisiones.html')

# <!-- @login_required  --> Vista que se debe sacar
def exit(request):
    logout(request)
    return redirect('index')

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('eventos')  
    else:
        form = EventoForm()
    
    return render(request, 'crear_evento.html', {'form': form})

def lista_eventos(request):
    eventos_vigentes = Evento.objects.filter(vigente=True)
    return render(request, 'eventos.html', {'eventos': eventos_vigentes})

def colegio(request):
    return render(request,'colegio.html')
def familia(request):
    return render(request,'familia.html')