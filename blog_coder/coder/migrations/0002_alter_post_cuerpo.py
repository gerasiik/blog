# Generated by Django 4.2.7 on 2023-12-03 00:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]