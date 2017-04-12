# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 15:59
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('filtro', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ['nombre'],
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=240)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'comentarios',
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, storage=gdstorage.storage.GoogleDriveStorage(permissions=(gdstorage.storage.GoogleDriveFilePermission(gdstorage.storage.GoogleDrivePermissionRole('reader'), gdstorage.storage.GoogleDrivePermissionType('user'), 'jhjaquintero@gmail.com'),)), upload_to='/geek-post/')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Categoria')),
            ],
            options={
                'ordering': ['-fecha_publicacion'],
                'db_table': 'post',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
