from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def eventos(request):
    return render(request,'eventos.html')

def alumnos(request):
    return render(request,'alumnos.html')

from django.shortcuts import render, redirect
from .forms import ContactoForm

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
def inscripciones(request):
    return render(request,'inscripciones.html')
def cambio(request):
    return render(request,'cambio.html')