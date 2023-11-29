from django.urls import path

# from . import views
from .views import HomeView,ArticleView

urlpatterns = [
    # path("", views.index, name="index"),
    path("", HomeView.as_view(), name="index"),
    path('article/<int:pk>/', ArticleView.as_view(), name='article-detail')
]
