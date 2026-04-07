from django.contrib import admin
from .models import Artigo, Comentario


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'corpo')
    list_filter = ('autor',)
    raw_id_fields = ('autor',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome_autor', 'artigo', 'data_publicacao')
    list_filter = ('artigo',)
    search_fields = ('nome_autor', 'texto')