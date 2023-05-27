from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'descricao', 'foto', "publicado" )
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10
    list_editable = ('publicado',)
    list_filter = ('categoria',)

admin.site.register(Fotografia, ListandoFotografias)
