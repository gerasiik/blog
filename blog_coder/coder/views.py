from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import PostForm


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


def fields(request):
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
        request, "coder/fields.html", {"miFormulario": miFormulario, "posts": posts}
    )


def crud(request):
    return render(request, "coder/crud.html")
