from django.urls import path

# logout
from django.contrib.auth.views import LogoutView

from .views import (
    index,
    post,
    leerEntradas,
    fields,
    eliminarEntrada,
    editarPost,
    login_user,
    register,
    editarPerfil,
)

urlpatterns = [
    # visualización de la home
    path("", index, name="index"),
    path("fields/", fields, name="fields"),
    path("leerEntradas", leerEntradas, name="LeerEntradas"),
    path("eliminarEntradas/<str:titulo>/", eliminarEntrada, name="EliminarEntradas"),
    path("editarEntradas/<str:titulo>/", editarPost, name="EditarEntradas"),
    # visualización de un articulo
    path("article/<slug>", post, name="article"),
    # login y registro
    path("login/", login_user, name="login"),
    path("register/", register, name="register"),
    # logout
    path(
        "logout/", LogoutView.as_view(template_name="coder/logout.html"), name="logout"
    ),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
]
