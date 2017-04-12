#!usr/bin/local
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .utils import error_messages, regex
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "jhjaquintero@gmail.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))


class Pais(models.Model):

    nombre = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex=regex['texto'],
                                   message=error_messages['texto'])],
        error_messages={'required': u'¿Cúal es el nombre del país?'},
        unique=True
    )

    class Meta:
        db_table = 'paises'
        ordering = ['nombre']
        verbose_name = "pais"
        verbose_name_plural = 'paises'

    def __unicode__(self):
        return self.nombre


class Ciudad(models.Model):

    nombre = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex=regex['texto'],
                                   message=error_messages['texto'])],
        error_messages={'required': u'¿Cúal es el nombre de la ciudad?'}
    )

    pais = models.ForeignKey('Pais', on_delete=models.CASCADE,
                             error_messages={'required': u'¿Ha que país pertenece la ciudad?'})

    class Meta:
        db_table = 'ciudades'
        ordering = ['nombre']
        verbose_name = 'ciudad'
        verbose_name_plural = 'ciudades'

    def __unicode__(self):
        return self.nombre


class Perfil(models.Model):

    usuario = models.OneToOneField(User, primary_key=True)

    nombres = models.CharField(
        max_length=40,
        validators=[RegexValidator(regex=regex['texto'],
                                   message=error_messages['texto'])],
        error_messages={'required': u'¿Cúal es tu nombre?'}
    )

    apellidos = models.CharField(
        max_length=40,
        validators=[RegexValidator(regex=regex['texto'],
                                   message=error_messages['texto'])],
        error_messages={'required': u'¿Cúal es tu apellido?'}
    )

    ciudad = models.ForeignKey('Ciudad', on_delete=models.PROTECT,
                               error_messages={'required': u'¿Dónde vives?'}
    )

    fecha_nacimiento = models.DateField(
        error_messages={'required': u'¿En qué año naciste'}
    )

    genero = models.CharField(
        max_length=6,
        validators=[RegexValidator(regex=regex['genero'], message=error_messages['genero'])],
        error_messages={'required': u'¿Cúal es tu género?'}
    )

    foto = models.ImageField(upload_to="/perfil/",
        storage=gd_storage,
        width_field=128, height_field=128,
        blank=True
    )

    class Meta:
        db_table = 'perfiles'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'

    def __unicode__(self):
        return self.usuario
