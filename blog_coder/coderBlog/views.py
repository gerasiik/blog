from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
# def index(request):
#     return render(request, "coderBlog/index.html")


class HomeView(ListView):
    model = Post
    template_name = "coderBlog/index.html"


class ArticleView(DetailView):
    model = Post
    template_name = "coderBlog/article.html"
