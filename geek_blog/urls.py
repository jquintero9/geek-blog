from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('post.urls', namespace='post')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
]
