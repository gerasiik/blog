from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Post"  # traduce el nombre de la app
        verbose_name_plural = "posts"  # traduce el nombre de la app
