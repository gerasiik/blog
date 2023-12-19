from django.shortcuts import render, redirect
from .models import Post, Avatar
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import PostForm, AvatarFormulario
from django.urls import reverse


# bloquear contenido no autorizado
from django.contrib.auth.decorators import login_required

# login y registro
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, logout

# formulario para editar  perfil
from coder.forms import UserEditForm

# avatar
from django.contrib.auth.models import User

# Create your views here.
# def index(request):
#     return render(request, "coderBlog/index.html")


def index(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.all()  # sirve para traer todos los posts
    if queryset:  # sirve para buscar
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(subtitulo__icontains=queryset)
        ).distinct()  # sirve para buscar el distinct sirve para traer los distintos post
    return render(request, "coder/index.html", {"posts": posts})


def post(request, slug):  # este es el slug para redirigir
    post = get_object_or_404(Post, slug=slug)
    return render(request, "coder/article.html", {"post": post})


@login_required
def fields(request):
    # imprime el avatar
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None

    if avatares.exists():
        url_avatar = avatares[0].imagen.url
    # imprime el avatar

    # creacion de formulario
    posts = Post.objects.all()

    if request.method == "POST":
        # Si hay un ID de post en la solicitud, se trata de una actualización
        post_id = request.POST.get("post_id")
        if post_id:
            post = get_object_or_404(Post, id=post_id)
            miFormulario = PostForm(request.POST, request.FILES, instance=post)
        else:
            # Si no hay ID, se trata de una creación
            miFormulario = PostForm(request.POST, request.FILES)

        if miFormulario.is_valid():
            miFormulario.save()
            return redirect(
                "http://127.0.0.1:8000/fields/"
            )  # Reemplaza con la URL deseada
    else:
        miFormulario = PostForm()

    return render(
        request,
        "coder/fields.html",
        {"url": url_avatar, "miFormulario": miFormulario, "posts": posts},
    )  # Se pone este contexto "url": url_avatar para imprimir el avatar


# crud de post o enntradas


# Leer
def leerEntradas(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None

    if avatares.exists():
        url_avatar = avatares[0].imagen.url

    entradas = Post.objects.all()  # trae todas las entradas
    contexto = {
        "entradas": entradas,
        "url": url_avatar,
    }  # el contexto sirve para imprimir las entradas
    return render(request, "coder/crud.html", contexto)


# Eliminar
def eliminarEntrada(request, titulo):
    entrada = Post.objects.get(titulo=titulo)
    entrada.delete()
    url = reverse("EliminarEntradas", args=[titulo])
    # vuelvo al menú
    entradas = Post.objects.all()  # trae todas las entradas
    contexto = {"entradas": entradas}  # el contexto sirve para imprimir las entradas
    return render(request, "coder/crud.html", contexto)


def editarPost(request, titulo):
    post = Post.objects.get(titulo=titulo)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(
                "/fields/"
            )  # Cambia 'nombre_de_la_otra_pagina' al nombre de la URL o ruta deseada
    else:
        form = PostForm(instance=post)

    return render(
        request, "coder/editarPost.html", {"form": form, "post": post, "titulo": titulo}
    )


# Login


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(
                    request,
                    "coder/bienvenido.html",
                    {"mensaje": f"Bienvenido {usuario}"},
                )
            else:
                return render(
                    request,
                    "coder/index.html",
                    {"mensaje": "Error, datos incorrectos"},
                )
        else:
            return render(
                request, "coder/error.html", {"mensaje": "Error, formulario erroneo"}
            )
    form = AuthenticationForm()
    return render(request, "coder/login.html", {"form": form})


# registro


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(
                request, "coder/usuario_creado.html", {"mensaje": "Usuario creado :)"}
            )
    else:
        form = UserCreationForm()
    return render(request, "coder/register.html", {"form": form})


# Editar perfil


def editarPerfil(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None

    if avatares.exists():
        url_avatar = avatares[0].imagen.url
    # Instancia login
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]

            # Solo actualiza la contraseña si se proporciona una nueva
            nueva_contraseña = informacion.get("password", None)
            if nueva_contraseña:
                usuario.set_password(nueva_contraseña)

            usuario.last_name = informacion["last_name"]
            usuario.first_name = informacion["first_name"]
            usuario.save()
            return render(request, "coder/bienvenido.html")
    else:
        miFormulario = UserEditForm(instance=usuario)
    return render(
        request,
        "coder/editarPerfil.html",
        {"url": url_avatar, "miFormulario": miFormulario, "usuario": usuario},
    )


def agregarAvatar(request):
    # imprime el avatar
    avatares = Avatar.objects.filter(user=request.user.id)
    url_avatar = None

    if avatares.exists():
        url_avatar = avatares[0].imagen.url
    # imprime el avatar

    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data["imagen"])
            avatar.save()
            return render(request, "coder/bienvenido.html")
    else:
        miFormulario = AvatarFormulario()
    return render(
        request,
        "coder/cambiarAvatar.html",
        {"url": url_avatar, "miFormulario": miFormulario},
        # Se pone este contexto "url": url_avatar para imprimir el avatar
    )
