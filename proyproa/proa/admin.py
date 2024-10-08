from django.contrib import admin
from .models import Contacto
from .models import Evento
from .models import Logro


# Register your models here.
admin.site.register(Contacto)
admin.site.register(Evento)
admin.site.register(Logro)
