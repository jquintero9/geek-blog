#!usr/local/bin
# coding: latin-1

from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .utils import encode
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

"""
Se crean los permisos y la instancia del almacenamiento de Google Drive
para guardar las imagenes de los posts.
"""
permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "jhjaquintero@gmail.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))


class Categoria(models.Model):

    """
    Representa la categoria de los artículos.
    """

    nombre = models.CharField(max_length=30)
    filtro = models.CharField(max_length=30)
    descripcion = models.TextField()

    class Meta:
        db_table = 'categorias'
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('post:categoria', kwargs={'categoria': self.filtro})


class Post(models.Model):
    """
    Representa los post del blog.
    """

    titulo = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    imagen = models.ImageField(upload_to="/geek-post/",
        storage=gd_storage,
        null=True,
        blank=True,
    )
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'
        ordering = ['-fecha_publicacion']

    def get_introduccion(self):
        n = 200
        introduccion = ""
        for i in range(n):
            try:
                introduccion += self.contenido[i]
            except IndexError:
                break
        introduccion += " [...]"

        return introduccion

    def get_absolute_url(self):
        return reverse('post:ver', kwargs={'slug': self.slug})

    def get_id(self):
        return encode(str(self.id))


    def __unicode__(self):
        return self.titulo


def create_slug(instance, new_slug=None):
    slug = slugify(instance.titulo)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)


class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comentario = models.CharField(max_length=240)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comentarios'
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'

    def __unicode__(self):
        return '%s - %s - %s' % (self.usuario, self.post, self.comentario)
