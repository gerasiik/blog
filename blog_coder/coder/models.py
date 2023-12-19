from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = RichTextField(verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.URLField(default="Pega el link de una imagen")
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor}"

    class Meta:
        verbose_name = "Post"  # traduce el nombre de la app
        verbose_name_plural = "posts"  # traduce el nombre de la app


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
