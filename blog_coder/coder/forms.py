from django import forms

# Importar ckeditor widget
from ckeditor.widgets import CKEditorWidget
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen", "slug")
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
            "autor": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            # widget de ckeditor
            "cuerpo": CKEditorWidget(),
        }

    # Agrega este método para permitir la carga de archivo
