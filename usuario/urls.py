from django.conf.urls import url
from .views import PerfilUsuario, CrearPerfil

urlpatterns = [
    url(r'^perfil$', PerfilUsuario.as_view(), name='perfil'),
    url(r'^perfil/editar$', CrearPerfil.as_view(), name='editar_perfil')
]
