from django.contrib import admin
from forum.models import Denuncia


class DenunciaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['review', 'visto_por']}),
        ('Date information', {'fields': ['desc'], 'classes':['collapse']}),
        ]

    list_display = ['review']
    list_filter = ['visto']

admin.site.register(Denuncia, DenunciaAdmin)