from django.urls import path
from .views import index, post, crud, fields

urlpatterns = [
    # visualización de la home
    path("", index, name="index"),
    path("fields/", fields, name="fields"),
    path("crud/", crud, name="crud"),
    # visualización de un articulo
    path("article/<slug>", post, name="article"),
]
