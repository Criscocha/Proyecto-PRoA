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

def contactos(request):
    return render(request,'contactos.html')

def academico(request):
    return render(request,'academico.html')