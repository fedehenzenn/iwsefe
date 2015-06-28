from django.contrib import admin
from forum.models import Denuncia, Categoria


class DenunciaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['review', 'visto','visto_por']}),
        ('Date information', {'fields': ['desc'], 'classes':['collapse']}),
        ]

    list_display = ['review']
    list_filter = ['visto']

class AdminCategoria(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Denuncia, DenunciaAdmin)
admin.site.register(Categoria, AdminCategoria)