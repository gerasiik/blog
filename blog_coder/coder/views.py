from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.
# def index(request):
#     return render(request, "coderBlog/index.html")


def index(request):
    posts = Post.objects.all()
    return render(request, "coder/index.html", {"posts": posts})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "coder/article.html", {"post": post})
