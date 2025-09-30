from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

class Videojuego(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    resumen = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    palabras_clave = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.URLField(help_text="URL de la imagen del videojuego")
    link_steam = models.URLField(help_text="Enlace a la página de Steam")

    def __str__(self):
        return self.nombre
