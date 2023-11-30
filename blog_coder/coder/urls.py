from django.urls import path
from .views import index, post

urlpatterns = [
    # visualización de la home
    path("", index, name="index"),
    # visualización de un articulo
    path("article/<slug>", post, name="article"),
]
