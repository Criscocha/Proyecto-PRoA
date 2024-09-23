from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca_de/', views.about, name='acerca_de'),
    path('eventos/', views.eventos, name='eventos'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('alumnos2/', views.alumnos2, name='alumnos2'),
    path('contactos/', views.contacto_view, name='contactos'),
    path('contactos2/', views.contacto_confirmacion, name='contacto_confirmacion'),
    path('academico/', views.academico, name='academico'),
    path('admisiones/', views.admisiones, name='admisiones'),
    path('logout/', exit, name='exit'),
]
