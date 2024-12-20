from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca_de/', views.about, name='acerca_de'),
    path('alumnos/', views.alumnos_view, name='alumnos'), 
    path('logro/<int:logro_id>/', views.logro_view, name='logro_view'),
    path('alumnos2/', views.alumnos2, name='alumnos2'),
    path('contactos/', views.contacto_view, name='contactos'),
    path('contactos2/', views.contacto_confirmacion, name='contacto_confirmacion'),
    path('academico/', views.academico, name='academico'),
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('crear_noticia/', views.crear_noticia, name='crear_noticia'),
    path('admisiones/', views.admisiones, name='admisiones'),
    path('logout/', exit, name='exit'),
    path('eventos2/', views.lista_eventos, name='lista_eventos'),
    path('colegios_proa/', views.colegios, name='colegios_proa'),
    path('proa/', views.proa, name='proa'),
    path('programa/', views.programa, name='programa'),
    path('objetivos_y_valores/', views.objetivos, name='objetivos'),
    path('trayectoria/', views.trayectoria, name='trayectoria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
