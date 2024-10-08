from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    vigente = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='eventos_imagenes/', blank=True, null=True)
    

    def __str__(self):
        return self.titulo
    


class Logro(models.Model):
    nombre = models.CharField(max_length=255)  # Asegúrate de que este campo esté definido
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
