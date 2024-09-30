from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca_de/', views.about, name='acerca_de'),
    path('eventos/', views.eventos, name='eventos'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('alumnos2/', views.alumnos2, name='alumnos2'),
    path('contactos/', views.contacto_view, name='contactos'),
    path('contactos2/', views.contacto_confirmacion, name='contacto_confirmacion'),
    path('academico/', views.academico, name='academico'),
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('eventos/', views.eventos, name='lista_eventos'),
    path('admisiones/', views.admisiones, name='admisiones'),
    path('logout/', exit, name='exit'),
    path('eventos2/', views.lista_eventos, name='lista_eventos'),
    path('colegio/', views.colegio, name='colegio'),
    path('familia_proa/', views.familia, name='familia'),
    path('proa/', views.proa, name='proa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
