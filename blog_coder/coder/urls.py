from django.urls import path
from .views import index, post, leerEntradas, fields, eliminarEntrada, editarPost

urlpatterns = [
    # visualización de la home
    path("", index, name="index"),
    path("fields/", fields, name="fields"),
    path("leerEntradas", leerEntradas, name="LeerEntradas"),
    path("eliminarEntradas/<str:titulo>/", eliminarEntrada, name="EliminarEntradas"),
    path("editarEntradas/<str:titulo>/", editarPost, name="EditarEntradas"),
    # visualización de un articulo
    path("article/<slug>", post, name="article"),
]
