from django.contrib import admin
from django.utils.html import format_html
from .models import Documento, Empresa

class DocumentoInline(admin.StackedInline):
    verbose_name = "Documento"
    model = Documento
    extra = 3

class EmpresaAdmin(admin.ModelAdmin):
    def indicado(self, obj):
        colors = {
            'S': 'green',
            'N': 'red'
        }
        return format_html(
        '<b style="color:{}; background:{}">{}</b>',
        colors[obj.indicado],
        colors[obj.indicado], 
        obj.indicado + obj.indicado,
    )
    list_display = ['razao_social', 'indicado', 'data_da_visita', 'briefing']
    list_filter = ('razao_social', 'data_da_visita')
    search_fields = ['razao_social', 'endereco']
    inlines = [DocumentoInline]

admin.site.register(Empresa, EmpresaAdmin)
admin.site.site_header = 'Controle de Visitas - GrupoGP'
admin.site.site_title = 'Sistema de Controle de Visitas'