from django.contrib import admin
from .models import Canhoto

@admin.register(Canhoto)
class CanhotoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'data',
        'valor',
        'tipo',
        'conferencia',
    )
    search_fields=('codigo',)