from django.conf.urls import url
from .views import (
    ListaPost,
    ListaPostCategoria,
    CrearPost,
    VerPost,
    EditarPost,
    EliminarPost,
    comentar,
)

urlpatterns = [
    url(r'^$', ListaPost.as_view(), name='lista'),
    url(r'^categoria/(?P<categoria>[a-z]+)$', ListaPostCategoria.as_view(), name='categoria'),
    url(r'^post/crear$', CrearPost.as_view(), name='crear'),
    url(r'^post/(?P<slug>[a-z0-9\-]+)$', VerPost.as_view(), name='ver'),
    url(r'^post/procesar_comentario$', comentar),
    url(r'^post/(?P<pk>\d+)/editar$', EditarPost.as_view(), name='editar'),
    url(r'^post/(?P<pk>\d+)/eliminar$', EliminarPost.as_view(), name='eliminar'),
]
