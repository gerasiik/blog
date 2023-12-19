from django import forms

# Importar ckeditor widget
from ckeditor.widgets import CKEditorWidget
from .models import Post, Avatar

# editar perfil
from django.contrib.auth.forms import UserCreationForm  # Agrega esta línea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


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

    # formulario para editar perfil


class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        ]
        help_texts = {k: "" for k in fields}


# formulario para editar perfil
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir la contraseña", widget=forms.PasswordInput
    )
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "last_name",
            "first_name",
        ]
        help_texts = {k: "" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["imagen"]
