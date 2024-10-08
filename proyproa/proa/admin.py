from django.contrib import admin
from .models import Contacto
from .models import Evento, Noticia


# Register your models here.
admin.site.register(Contacto)
admin.site.register(Evento)
admin.site.register(Noticia)