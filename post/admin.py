from django.contrib import admin
from .models import Post, Categoria, Comentario


class ArticuloAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'ultima_actualizacion', 'fecha_publicacion', 'categoria']
    list_display_links = ['ultima_actualizacion']
    list_editable = ['titulo']
    list_filter = ['fecha_publicacion']
    search_fields = ['titulo', 'contenido']

    class Meta:
        model = Post


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'descripcion']

    class Meta:
        model = Categoria


admin.site.register(Post, ArticuloAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Comentario)
