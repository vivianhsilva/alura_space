from django.contrib import admin
from galeria.models import Fotografia

class listandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "legenda", "publicada")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("nome","legenda")
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, listandoFotografias)
